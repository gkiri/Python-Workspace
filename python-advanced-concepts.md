################## Notes for each topic ##################
## Topic-1 : EasyDict

reference : https://github.com/makinacorpus/easydict

* when using dictionary it becomes difficult to use keys and values with brackets
* To make it simplified , lets access each key or value with attributes (like a variable)
* ```  
  >>> from easydict import EasyDict as edict
  >>> d = edict({'foo':3, 'bar':{'x':1, 'y':2}})
  >>> d.foo
  3
  >>> d.bar.x
  1

  >>> d = edict(foo=3)
  >>> d.foo
  3

* Now access easily like -> d.foo  or d.bar.x

Real worl usage : https://github.com/SimonVandenhende/Multi-Task-Learning-PyTorch/blob/e2bcb2ebb72c29ea424b8b251d733a8cddef2214/utils/config.py#L16


## Topic-2 : List Comprehensions

### Doing all processing inside the brackets 
#### Basic for loop
* ```  
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
  newlist = []

  for x in fruits:
    if "a" in x:
      newlist.append(x)

  print(newlist) # ['apple', 'banana', 'mango']

* now lets use list comprehension

* ```
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

  newlist = [x for x in fruits if "a" in x]
  
  print(newlist) #['apple', 'banana', 'mango']
  
#### syntax 

* ```
  newlist = [expression for item in iterable if condition == True]

#### Eg:2 
* ```  
  >>> l = [2, 4, 6, 8, 10, 12]
  >>> [int(i / 2) for i in l]
  [1, 2, 3, 4, 5, 6]
  
* process logic inside block

#### Eg:3
* ```  

  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

  newlist = [x for x in fruits if x != "apple"]

  print(newlist) #o/p =['banana', 'cherry', 'kiwi', 'mango']
  
#### Eg:4

* ```    
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

  newlist = [x for x in fruits]

  print(newlist) #op =['apple', 'banana', 'cherry', 'kiwi', 'mango']
  
#### Eg:5

* ```  
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

  newlist = [x if x != "banana" else "orange" for x in fruits]

  print(newlist) #op =['apple', 'orange', 'cherry', 'kiwi', 'mango'] 
                      #here only when its banana if is tru so x is replaced with orange
                      
                      
## Topic-3 : Dict Comprehensions
### Normal dictionary usage
* ```  
  square_dict = dict()
  for num in range(1, 11):
      square_dict[num] = num*num
  print(square_dict) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

### dictionary comprehension example
* ```  
  square_dict = {num: num*num for num in range(1, 11)}
  
  print(square_dict) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


### Syntax
* ```  
  dictionary = {key: value for vars in iterable}
  
### Eg:1 item price in dollars
* ```    
  
  old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

  dollar_to_pound = 0.76
  new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
  print(new_price) #{'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}

