cmake_minimum_required(VERSION 3.10)
project(yolo CXX C)
#project(main_test CXX)

#set(CMAKE_CXX_STANDARD 11)
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -O3")  #设置c++的编译选项
set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O3 -Wall")  #设置c的编译选项

find_package(OpenCV REQUIRED)

include_directories(
        include/MNN
        include
        ../steering_engine/bcm2835-1.68/Pan-Tilt_HAT_code/RaspberryPi/Servo_Driver/bcm2835/Servo
)

link_directories(lib/)
#link_libraries("/usr/local/lib/libbcm2835.a")

add_executable(yolo src/main.cpp ../steering_engine/bcm2835-1.68/Pan-Tilt_HAT_code/RaspberryPi/Servo_Driver/bcm2835/Servo/PCA9685.c ../steering_engine/bcm2835-1.68/Pan-Tilt_HAT_code/RaspberryPi/Servo_Driver/bcm2835/Servo/DEV_Config.c)
target_link_libraries(yolo MNN ${OpenCV_LIBS} bcm2835)

#add_executable(main_test src/main_test.cpp)
#target_link_libraries(main_test MNN ${OpenCV_LIBS})
