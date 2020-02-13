cmake_minimum_required(VERSION 2.8)
project(classifier)

set(Caffe_Root
        /home/lan/ruanjian/caffe
        )
set(Caffe_INCLUDE_DIRS
        ${Caffe_Root}/include
        ${Caffe_Root}/src
        /usr/local/cuda/include
        )
set(Caffe_LIBRARIES
        caffe
        boost_system
        glog
        )

find_package(OpenCV REQUIRED)
include_directories(
        ${Caffe_INCLUDE_DIRS}
        ${OpenCV_INCLUDE_DIRS}
        ${CMAKE_CURRENT_SOURCE_DIR}
)

link_directories(
        ${Caffe_Root}/build/lib
)

add_library(${PROJECT_NAME} #STATIC | SHARED | MODULE
        ${CMAKE_CURRENT_SOURCE_DIR}/classifier.cpp#把分类器编译成链接库
        )

#target_link_libraries(${PROJECT_NAME}
#	${OpenCV_LIBS}
#)

add_executable(run main.cpp)#把main.cpp编译成可执行文件run
target_link_libraries(run
        ${PROJECT_NAME}
        ${OpenCV_LIBS}
        ${Caffe_LIBRARIES}
        )