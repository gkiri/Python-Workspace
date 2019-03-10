# -*- coding: utf-8 -*-
from lxml import html
import requests
from collections import OrderedDict
import json
import argparse
import re
import sys
# Adjust MAX_RETRY according to the blocking from tripadvisor
MAX_RETRY = 10
RETRY = 0


def clean(text):
    if text:
        # Removing \n \r and \t
        return ' '.join(''.join(text).split()).strip()
    return None


def process_request(url, retry=0):
    """
    Function to process tripadvisor Hotel page
    Args:
        : required param url : url of tripadvisor
    return :
        : parser object
    """
    print("Fetching %s, retry count %s" % (url, retry))
    headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
                "cache-control": "max-age=0",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return {'error': 'Page not found', 'status_code': 404}

    parser = html.fromstring(response.text, url)
    return process_page(parser, url)


def process_page(parser, url):
    global MAX_RETRY
    global RETRY
    script_text = ' '.join(''.join(parser.xpath('//script//text()')).split())
    raw_json = re.findall("define\(\'@ta\/page\-manifest\'\,\[\]\,function\(\)\{return\s+({.*?});\}\);", script_text)
    try:
        json_loaded = json.loads(raw_json[0])
    except Exception as e:
        json_loaded = {}
        if RETRY < MAX_RETRY:
            RETRY = RETRY+1
            # Retrying the same URL
            process_request(url, RETRY)

    XPATH_NAME = '//h1[@id="HEADING"]//text()'
    XPATH_RANK = '//span[contains(@class,"popularity")]//text()'
    XPATH_AMENITIES = "//div[contains(text(),'HOTEL FEATURES')]/following-sibling::div//div[@class='textitem']//text()"
    XPATH_HIGHLIGHTS = '//div[contains(@class,"HighlightedAmenities__amenityItem")]/text()'
    XPATH_OFFICIAL_DESCRIPTION = '//div[contains(text(),"Description")]/following-sibling::div//span[contains(@class,"introText")]/text()'
    XPATH_ADDITIONAL_INFO = "//div[@class='section_content']//div[@class='sub_title']"
    XPATH_FULL_ADDRESS_JSON = '//script[@type="application/ld+json"]//text()'

    raw_name = parser.xpath(XPATH_NAME)
    raw_rank = parser.xpath(XPATH_RANK)
    amenities = parser.xpath(XPATH_AMENITIES)
    raw_highlights = parser.xpath(XPATH_HIGHLIGHTS)
    raw_official_description = parser.xpath(XPATH_OFFICIAL_DESCRIPTION)
    raw_additional_info = parser.xpath(XPATH_ADDITIONAL_INFO)
    raw_address_json = parser.xpath(XPATH_FULL_ADDRESS_JSON)
    name = clean(raw_name)
    rank = clean(raw_rank)
    if not name:
        if RETRY < MAX_RETRY:
            RETRY = RETRY+1
            # Retrying the same URL
            process_request(url, RETRY)
    official_description = clean(raw_official_description)
    cleaned_highlights = filter(lambda x: x != '\n', raw_highlights)
    hotel_rating = 0
    address = {}
    if raw_address_json:
        try:
            parsed_address_info = json.loads(raw_address_json[0])
            rating = parsed_address_info.get('aggregateRating', {})
            address = parsed_address_info.get("address", {})

            hotel_rating = rating.get('ratingValue')
            review_count = rating.get('reviewCount')

            address = {
                        'street_address': address.get('streetAddress'),
                        'region': address.get('addressRegion'),
                        'locality': address.get('addressLocality'),
                        'country': address.get("addressCountry", {}).get("name"),
                        'zipcode': address.get("postalCode")
            }
        except Exception as e:
            review_count = hotel_rating = 0
            raise e
    highlights = ','.join(cleaned_highlights).replace('\n', '')
    ratings = {}

    if json_loaded:
        redux_response = json_loaded['redux']['api']['responses']
        if redux_response:
            for url_ in redux_response.keys():
                if '/data/1.0/location/' in url_:
                    rating_histogram = redux_response.get(url_).get('data').get('rating_histogram', {})
                    ratings = {
                                'Excellent': int(rating_histogram.get('count_5', 0)),
                                'Good': int(rating_histogram.get('count_4', 0)),
                                'Average': int(rating_histogram.get('count_3', 0)),
                                'Poor': int(rating_histogram.get('count_2', 0)),
                                'Terrible': int(rating_histogram.get('count_1', 0))
                    }
    amenity_dict = {'Hotel Amenities': ','.join(amenities)}
    additional_info_dict = OrderedDict()
    for info in raw_additional_info:
        XPATH_INFO_TEXT = ".//text()"

        if info.xpath(XPATH_INFO_TEXT):
            XPATH_INFO_KEY = ".//text()"
            XPATH_INFO_VALUE = './/following-sibling::div[@class="sub_content"][1]//text()'

            raw_info_key = info.xpath(XPATH_INFO_KEY)
            raw_info_value = info.xpath(XPATH_INFO_VALUE)
            if raw_info_value and raw_info_key:
                # cleaning
                raw_info_value = clean(raw_info_value)
                # contact information such as website and email address are encoded by tripadvisor
                if not raw_info_key[0] == 'Contact Information':
                    additional_info_dict.update({raw_info_key[0]: raw_info_value})

    data = {
            'address': address,
            'ratings': ratings,
            'amenities': amenity_dict,
            'official_description': official_description,
            'additional_info': additional_info_dict,
            'rating': float(hotel_rating) if hotel_rating else 0.0,
            'review_count': int(review_count) if review_count else 0,
            'name': name,
            'rank': rank,
            'highlights': highlights,
            'hotel_url': url
    }
        
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Tripadvisor hotel url')
    args = parser.parse_args()
    url = args.url
    scraped_data = process_request(url)
    if scraped_data:
        print("Writing scraped data")
        with open('tripadvisor_hotel_scraped_data.json', 'w') as f:
            json.dump(scraped_data, f, indent=4, ensure_ascii=False)