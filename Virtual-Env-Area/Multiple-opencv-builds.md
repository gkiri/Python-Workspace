# Install Opencv and create Virtualenv for python
* https://www.learnopencv.com/install-opencv-3-4-4-on-ubuntu-16-04/
* install opencv in created folder eg:here installation is folder name

Then Edit CMakeLists.txt with "set(OpenCV_DIR /home/slam/installation/OpenCV-3.4.4/share/OpenCV)" for any package u r building
* EG : I downloaded DBoW package from github ,it has CMakeLists.txt which need opencv for compiling,so i edit that CMakeLists.txt with  set(OpenCV_DIR /home/slam/installation/OpenCV-3.4.4/share/OpenCV)
spo that it knows where to picks Opencv from


Code in CmakeLists.txt
set(OpenCV_DIR /home/slam/installation/OpenCV-3.4.4/share/OpenCV)
find_package(OpenCV 3.0 QUIET)
if(NOT OpenCV_FOUND)
   find_package(OpenCV 2.4.3 QUIET)
   if(NOT OpenCV_FOUND)
      message(FATAL_ERROR "OpenCV > 2.4.3 not found.")
   endif()
endif()


* This waz we can install another opncv of another version still build libraries specifuing respective paths
