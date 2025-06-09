cmake_minimum_required(VERSION 3.8)
project(turtlebro_sim)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch
  config
  map
  urdf
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
