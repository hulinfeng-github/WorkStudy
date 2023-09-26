### cmake `推荐`

- CMakeLists.txt模版

```txt
cmake_minimum_required(VERSION 2.6)
project(your_project)

set(T_NAME  			    "name")
set(T_VERSION   		    "1.0.0.0")
set(T_INCLUDE_DIRECTORIES  	"./include")
set(T_LINK_LIBRARIES   		"-lm -pthread -lyourlib")
set(T_LINK_DIRECTORIES 		"./lib")

aux_source_directory(. SOURCES)
# also
# set(SOURCES a.c b.c)

target_link_libraries(${T_NAME} ${T_LINK_LIBRARIES})
link_directories(${T_LINK_DIRECTORIES})

#############################################
# if you want to build binary, enable this
#############################################

# add_executable(${T_NAME} ${SOURCES})
# install(TARGET ${T_NAME} DESTINATION "${CMAKE_INSTALL_PREFIX}/bin/")

#############################################
# if you want to build static library
#############################################

# add_library(${T_NAME} ${SOURCES})
# install(TARGET ${T_NAME} DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/")
# install(FILES module.h DESTINATION "${CMAKE_INSTALL_PREFIX}/include/")

#############################################
# if you want to build shared library
#############################################

# add_library(${T_NAME} shared ${SOURCES})
# install(TARGET ${T_NAME} DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/")
# install(FILES module.h DESTINATION "${CMAKE_INSTALL_PREFIX}/include/")

# if you have subdirectory
#add_subdirectory(subdir)

```

使用方式:

```shell
$ sudo apt-get install cmake
$ cd project1
$ mkdir build
$ cmake .. -DCMAKE_INSTALL_PREFIX=$HOME/usr/
$ make
$ make install
$ make clean
```

## 构建自己的编译工具

cmake举例说明

将此内容保存至 mycmake 文件，并拷贝至PATH指向的路径, 如 /usr/bin/ 或者 /usr/local/bin 或者 ~/bin/


使用方法:

- build:  在包含CMakeLists.txt的目录中执行： `mycmake` 即可
- clean:  在包含CMakeLists.txt的目录中执行： `mycmake clean` 即可

```bash
#!/bin/bash
build()
{
        [ -f CMakeLists.txt ] || (echo 'CMakeLists.txt does notexist' && exit)
        [ -d build ] || mkdir build
        cd build
        [ -f Makefile ] || cmake .. && make
}

clean()
{
        [ -d build ] && rm -rf build
}

if [ x$1 == xclean ]; then
        clean
else
        build
fi

```