# helloworld-qt-conan

Notes on setting up a Qt5 project for Visual Studio 2019 using prebuilt conan packages from bincrafters.

## Install Visual Studio

## Install conan

Download and install from https://conan.io/downloads.html

Open a VS console and set up profiles to use the detected compiler:

    conan profile new vs19_release --detect
    conan profile new vs19_debug --detect

Manually edit the debug profile `%userprofile%\.conan\profiles\vs19_debug` to set `build_type=Debug`.

Add bincrafters remote:

    conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan

## Build project

`cd` to the checkout directory and install and build project (CMake and Ninja should come from VS in the path):

    conan install -pr vs19_debug -if debug .
    conan build -bf debug .

Run the executable in `debug/bin/helloworldqtconan.exe`.

![Screenshot](https://rkibria.github.io/images/helloworldqtconan.png)
