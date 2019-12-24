# Qt Compilation

## Changelog
- [20190625] re-cross compile qt-5.12.3 source libs and test a Qt application in `Raspberry Pi 3`[more](#Compile-Qt-program-for-Raspberry-Pi-on-Linux-hostadvanced-example).
- [20190626] elaborate the Qt application basic build procedure via command line[more](#Compile-Qt-program-Natively-on-Linux-Hostbasic-example). 
- [20190627] add [outline](#Outline) for Qt cross-compilation.

## Install Qt

[Online Installation](https://doc.qt.io/qt-5/gettingstarted.html#online-installation)

[Offline Installation](https://doc.qt.io/qt-5/gettingstarted.html#offline-installation)

### Platform Requirements

[Qt for Linux/X11](https://doc.qt.io/qt-5/linux.html)


## Cross Compiling

The cross-compilation in Qt application is a significant job that mainly enable you to develop and compile your `Qt` programme on the `linux` host for `embedded` devices target. It will exert maximum resources in the host machine such as CPU to speed up application development.

Before cross compiling a `Qt` application, you need to build `Qt` for a given device, popularly [embedded Linux](https://doc.qt.io/qt-5/embedded-linux.html), through a toolchain and a sysroot. It always comes up a `Qt` application with a dynamically linked `Qt` libraries(`*.so` files). In some cases, [using static linking](https://doc.qt.io/QtForDeviceCreation/qtee-static-linking.html) to `Qt` libraries(`*.a` files) may be preferable.



**references:**
* [Boot to Qt Software Stack](https://doc.qt.io/QtForDeviceCreation/qtb2-index.html)
* [QT Supported Platforms](https://doc.qt.io/qt-5/supported-platforms.html)
* [Qt for Device Creation](https://doc.qt.io/QtForDeviceCreation/index.html)
* [Target Devices](https://doc.qt.io/QtForDeviceCreation/qtdc-supported-platforms.html)
* [Qt for Embedded Linux](https://doc.qt.io/qt-5/embedded-linux.html)
* [Qt Configure Options](https://doc.qt.io/qt-5/configure-options.html#)

### Toolchains

when the host and target architectures are different, it's a cross compiler (e.g. if you develop code
on a Linux machine based on the x86 architecture, but you’re compiling for an ARM target, then you need Linux-based ARM-targeting cross compiler).

conceptions:

*native compilation*

*cross compilation*

[Introduction to cross-compiling for Linux](https://landley.net/writing/docs/cross-compiling.html)

[Toolchains](http://web.eecs.umich.edu/~prabal/teaching/eecs373-f12/notes/notes-toolchain.pdf)



### Outline

The following list summarizes the main steps to cross-compile Qt 5.12.3 for `linux embedded device`, such as `Raspberry Pi`, `Jetson Nano`, while each elaborate step and difference upon various devices could be found in [examples](#Examples). The [Embedded] label means this action is done in the Raspberry Pi, whereas [Host] means it has to be performed in you computer.

1. Prepare the device with new `os` image and firmware – [Embedded]
2. Install development libraries – [Embedded]
3. Prepare target folder – [Embedded]
   The Qt libraries cross-compiled by `Host` will be installed here. And configuration in `step 6` will depend on this. 
4. Download Qt 5.12.3 Source – [Host]
5. Create `sysroot`, working folder and set a toolchain and other tools – [Host]
6. Configure Qt for cross compilation – [Host]
7. Compile, install and deploy Qt libraries – [Host]
8. Compile Qt application – [Host]




## Examples

### Compile Qt program Natively on Linux Host(basic example)

An example, 
Building Qt 5 application `TextFinder` on Linux manually,

```sh
# 1. create build folder in any path
frankchen@:qt-project$ LINUX_RELEASE=build-TextFinder-Desktop_Qt_5_12_3_GCC_64bit-Release
frankchen@:qt-project$ mkdir LINUX_RELEASE

frankchen@:qt-project$ cd LINUX_RELEASE/

# 2. native `qmake` tool use `TextFinder.pro` to create a `Makefile` file in `LINUX_RELEASE`. It will not pollute the `TextFinder` project folder.
frankchen@:$LINUX_RELEASE$ "/home/frankchen/Qt/5.12.3/gcc_64/bin/qmake" /home/frankchen/Documents/qt-project/TextFinder/TextFinder.pro -spec linux-g++ CONFIG+=qtquickcompiler
Info: creating stash file /home/frankchen/Documents/qt-project/build-TextFinder-Desktop_Qt_5_12_3_GCC_64bit-Release/.qmake.stash

frankchen@:$LINUX_RELEASE$ ll
total 80
drwxr-xr-x 2 frankchen frankchen  4096 Jun 12 12:45 ./
drwxr-xr-x 4 frankchen frankchen  4096 Jun 12 12:34 ../
-rw-r--r-- 1 frankchen frankchen 68620 Jun 12 12:45 Makefile
-rw-r--r-- 1 frankchen frankchen   739 Jun 12 12:45 .qmake.stash

# 3. use `Makefile` file to generate the executable application
frankchen@:$LINUX_RELEASE$ "/usr/bin/make" -j4

/home/frankchen/Qt/5.12.3/gcc_64/bin/uic ../TextFinder/textfinder.ui -o ui_textfinder.h
g++ -c -pipe -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_DEPRECATED_WARNINGS -DQT_NO_DEBUG -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_CORE_LIB -I../TextFinder -I. -I../../../Qt/5.12.3/gcc_64/include -I../../../Qt/5.12.3/gcc_64/include/QtWidgets -I../../../Qt/5.12.3/gcc_64/include/QtGui -I../../../Qt/5.12.3/gcc_64/include/QtCore -I. -isystem /usr/include/libdrm -I. -I../../../Qt/5.12.3/gcc_64/mkspecs/linux-g++ -o main.o ../TextFinder/main.cpp
g++ -c -pipe -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_DEPRECATED_WARNINGS -DQT_NO_DEBUG -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_CORE_LIB -I../TextFinder -I. -I../../../Qt/5.12.3/gcc_64/include -I../../../Qt/5.12.3/gcc_64/include/QtWidgets -I../../../Qt/5.12.3/gcc_64/include/QtGui -I../../../Qt/5.12.3/gcc_64/include/QtCore -I. -isystem /usr/include/libdrm -I. -I../../../Qt/5.12.3/gcc_64/mkspecs/linux-g++ -o textfinder.o ../TextFinder/textfinder.cpp
/home/frankchen/Qt/5.12.3/gcc_64/bin/rcc -name textfinder ../TextFinder/textfinder.qrc -o qrc_textfinder.cpp
g++ -pipe -O2 -std=gnu++11 -Wall -W -dM -E -o moc_predefs.h ../../../Qt/5.12.3/gcc_64/mkspecs/features/data/dummy.cpp
g++ -c -pipe -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_DEPRECATED_WARNINGS -DQT_NO_DEBUG -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_CORE_LIB -I../TextFinder -I. -I../../../Qt/5.12.3/gcc_64/include -I../../../Qt/5.12.3/gcc_64/include/QtWidgets -I../../../Qt/5.12.3/gcc_64/include/QtGui -I../../../Qt/5.12.3/gcc_64/include/QtCore -I. -isystem /usr/include/libdrm -I. -I../../../Qt/5.12.3/gcc_64/mkspecs/linux-g++ -o qrc_textfinder.o qrc_textfinder.cpp
/home/frankchen/Qt/5.12.3/gcc_64/bin/moc -DQT_DEPRECATED_WARNINGS -DQT_NO_DEBUG -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_CORE_LIB --include /home/frankchen/Documents/qt-project/build-TextFinder-Desktop_Qt_5_12_3_GCC_64bit-Release/moc_predefs.h -I/home/frankchen/Qt/5.12.3/gcc_64/mkspecs/linux-g++ -I/home/frankchen/Documents/qt-project/TextFinder -I/home/frankchen/Qt/5.12.3/gcc_64/include -I/home/frankchen/Qt/5.12.3/gcc_64/include/QtWidgets -I/home/frankchen/Qt/5.12.3/gcc_64/include/QtGui -I/home/frankchen/Qt/5.12.3/gcc_64/include/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../TextFinder/textfinder.h -o moc_textfinder.cpp
g++ -c -pipe -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_DEPRECATED_WARNINGS -DQT_NO_DEBUG -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_CORE_LIB -I../TextFinder -I. -I../../../Qt/5.12.3/gcc_64/include -I../../../Qt/5.12.3/gcc_64/include/QtWidgets -I../../../Qt/5.12.3/gcc_64/include/QtGui -I../../../Qt/5.12.3/gcc_64/include/QtCore -I. -isystem /usr/include/libdrm -I. -I../../../Qt/5.12.3/gcc_64/mkspecs/linux-g++ -o moc_textfinder.o moc_textfinder.cpp
g++ -Wl,-O1 -Wl,-rpath,/home/frankchen/Qt/5.12.3/gcc_64/lib -o TextFinder main.o textfinder.o qrc_textfinder.o moc_textfinder.o   -L/home/frankchen/Qt/5.12.3/gcc_64/lib -lQt5Widgets -lQt5Gui -lQt5Core -lGL -lpthread   

frankchen@:$LINUX_RELEASE$ ll
total 180
drwxr-xr-x 2 frankchen frankchen  4096 Jun 12 12:50 ./
drwxr-xr-x 4 frankchen frankchen  4096 Jun 12 12:34 ../
-rw-r--r-- 1 frankchen frankchen  3192 Jun 12 12:50 main.o
-rw-r--r-- 1 frankchen frankchen 68620 Jun 12 12:45 Makefile
-rw-r--r-- 1 frankchen frankchen 13712 Jun 12 12:50 moc_predefs.h
-rw-r--r-- 1 frankchen frankchen  3411 Jun 12 12:50 moc_textfinder.cpp
-rw-r--r-- 1 frankchen frankchen 10384 Jun 12 12:50 moc_textfinder.o
-rw-r--r-- 1 frankchen frankchen   739 Jun 12 12:45 .qmake.stash
-rw-r--r-- 1 frankchen frankchen  4029 Jun 12 12:50 qrc_textfinder.cpp
-rw-r--r-- 1 frankchen frankchen  4088 Jun 12 12:50 qrc_textfinder.o
-rwxr-xr-x 1 frankchen frankchen 33928 Jun 12 12:50 TextFinder*
-rw-r--r-- 1 frankchen frankchen 12360 Jun 12 12:50 textfinder.o
-rw-r--r-- 1 frankchen frankchen  2982 Jun 12 12:50 ui_textfinder.h
```

**Note:**
> the linux application `TextFinder` is dynamic linking.
> `-spec spec` indicates that qmake will use spec as a path to platform and compiler information, and ignore the value of QMAKESPEC[more](https://doc.qt.io/qt-5/qmake-running.html#).

### Compile Qt program for Windows on Linux host(basic example)

[Building Qt 5 application for Windows on Linux](https://stackoverflow.com/questions/14170590/building-qt-5-on-linux-for-windows/14170591#14170591)

An example for `TextFinder` project release for `windows` platform manually on `ubuntu` host

**Note:**
> the windows application is static linking.

```sh


```

### Compile C program for `Raspberry Pi` on Linux host(basic example)
If we consider that we are working on two platforms,
1. x86 – 32 or 64 bit i.e. laptop / desktop
2. ARM – Lets say Raspberry Pi

3. Download toolchains and a simple C file.

    ```sh
    frankchen@:raspberrypi$ git clone https://github.com/raspberrypi/tools --depth 1

    frankchen@:raspberrypi$ cat hello.c 
    # include <stdio.h>
    int main() {
        printf("%s\n", "Hello World");
        return 0;
    }

    frankchen@:raspberrypi$ ls
    hello.c  tools

    ```
4. Choose cross compiler in `gcc-linaro-arm-linux-gnueabihf-raspbian`
    
    ```sh
    frankchen@:raspberrypi$ export PATH=$PATH:/home/frankchen/Documents/raspberrypi/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/bin
    frankchen@:raspberrypi$ arm-linux-gnueabihf-gcc -o hello hello.c 
    frankchen@:raspberrypi$ file hello
    hello: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-, for GNU/Linux 2.6.26, BuildID[sha1]=b5d2d491fea9afdf8259aea28f0e6c02929711dc, not stripped
    ```

5. Run the executable file in our ubuntu host

    ```sh
    #install a tool “qemu” 
    frankchen@:raspberrypi$ sudo apt-get install qemu
    frankchen@:raspberrypi$ qemu-arm -L /home/frankchen/Documents/raspberrypi/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/arm-linux-gnueabihf/libc ./hello
    Hello World
    ```

    **Note:**
    > (-L /home/frankchen/Documents/raspberrypi/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/arm-linux-gnueabihf/libc is the `sysroot` provided by the toolchain, which is the environment of the target platform)

    ```sh
    frankchen@:raspberrypi$ arm-linux-gnueabihf-gcc --print-sysroot
    /home/frankchen/Documents/raspberrypi/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/bin/../arm-linux-gnueabihf/libc
    ```

    > For more information, `arm-linux-gnueabihf-gcc --help`

**references:**
* [Difference between native and cross compilation and how to compile simple program for x86 and ARM](https://www.lynxbee.com/difference-between-native-and-cross-compilation-and-how-to-compile-simple-program-for-x86-and-arm/)
* [How to cross compile for ARM](http://www.firmcodes.com/how-to-cross-compile-for-arm/)


### Compile Qt program for `Raspberry Pi` on Linux host(advanced example)

1. Download the new `Raspberry Pi` os [image](https://www.raspberrypi.org/downloads/raspbian/) and flash it into `sd` card, plug sd into host.[Host]

```sh
# download image
frankchen@~: mkdir ~/Documents/raspberrypi/
frankchen@raspberrypi: wget http://director.downloads.raspberrypi.org/raspbian_full/images/raspbian_full-2019-04-09/2019-04-08-raspbian-stretch-full.zip
# unmount the sd disk
frankchen@:raspberrypi$ sudo fdisk -l
...
Disk /dev/sdc: 59.8 GiB, 64155025408 bytes, 125302784 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000

Device     Boot Start       End   Sectors  Size Id Type
/dev/sdc1  *    32768 125302783 125270016 59.8G  7 HPFS/NTFS/exFAT
frankchen@:raspberrypi$ sudo unmount /dev/sdc1
frankchen@:raspberrypi$ sudo unmount /dev/sdc2 (if sdc2 exist)

# flash the image into sd
frankchen@:raspberrypi$ sudo dd bs=4M if=2019-04-08-raspbian-stretch-full.img of=/dev/sdc conv=fsync

```

**Note:**
> not use `noobs` edition

2. Update the `raspberrypi` hardware[Pi]

```sh
pi@raspberrypi:~ $ sudo rpi-update
pi@raspberrypi:~ $ reboot

# after reboot
# enable `ssh`
pi@raspberrypi:~ $ sudo raspi-config
```

**Note:**
> for reboot halt, that the green light is flashing 4 times as pattern, it maybe the `boot` folder delete some files. Copy [boot](https://github.com/raspberrypi/firmware/tree/master/boot) to the `sd` card `boot` folder.

3. Install development libraries[Pi]

```sh
# uncomment the deb-src line in the /etc/apt/sources.list file
pi@raspberrypi:~ $ sudo nano /etc/apt/sources.list

# update and install the required development packages
pi@raspberrypi:~ $ sudo apt-get update
pi@raspberrypi:~ $ sudo apt-get build-dep qt4-x11
pi@raspberrypi:~ $ sudo apt-get build-dep libqt5gui5
pi@raspberrypi:~ $ sudo apt-get install libudev-dev libinput-dev libts-dev libxcb-xinerama0-dev libxcb-xinerama0
```

4. Prepare target folder[Pi]

```sh
pi@raspberrypi:~ $ sudo mkdir /usr/local/qt5pi
pi@raspberrypi:~ $ sudo chown pi:pi /usr/local/qt5pi
```

5. Install Qt source code[Host]

[Install Qt](#install-qt)

[Qt Downloads](https://download.qt.io/archive/qt/)

```sh
frankchen@:raspberrypi$ ll ~/Qt/5.12.3/
total 32
drwxrwxr-x  7 frankchen frankchen 4096 Jun 10 12:58 ./
drwxrwxrwx  8 frankchen frankchen 4096 Jun 10 17:01 ../
drwxrwxr-x 12 frankchen frankchen 4096 Jun 10 12:58 android_arm64_v8a/
drwxrwxr-x 12 frankchen frankchen 4096 Jun 10 12:58 android_armv7/
drwxrwxr-x 12 frankchen frankchen 4096 Jun 10 12:58 android_x86/
drwxrwxr-x 13 frankchen frankchen 4096 Jun 10 12:59 gcc_64/
-rw-rw-r--  1 frankchen frankchen 2165 Apr 16 21:02 sha1s.txt
drwxrwxr-x 45 frankchen frankchen 4096 Jun 14 18:12 Src/
```

6. Create working folder, configure a sysroot, set up the toolchain and other tools[Host]

**workding folder**

```sh
frankchen@~: mkdir -p ~/Documents/raspberrypi/
frankchen@~: cd ~/Documents/raspberrypi/
```

**sysroot**

```sh
frankchen@raspberrypi: mkdir sysroot sysroot/usr sysroot/opt
frankchen@raspberrypi: rsync -avz pi@raspberrypi.local:/lib sysroot
frankchen@raspberrypi: rsync -avz pi@raspberrypi.local:/usr/include sysroot/usr
frankchen@raspberrypi: rsync -avz pi@raspberrypi.local:/usr/lib sysroot/usr
frankchen@raspberrypi: rsync -avz pi@raspberrypi.local:/opt/vc sysroot/opt
```


**toolchain**

```sh
frankchen@raspberrypi: git clone https://github.com/raspberrypi/tools.git
```

**symbolic link tool**

```sh
frankchen@raspberrypi: wget https://raw.githubusercontent.com/riscv/riscv-poky/master/scripts/sysroot-relativelinks.py
frankchen@raspberrypi: chmod +x ./sysroot-relativelinks.py
frankchen@raspberrypi: sudo ./sysroot-relativelinks.py sysroot
```

If you are running on Linux 64bit, install the following package,

```sh
frankchen@raspberrypi: sudo apt-get install lib32z1
```

**RaspberryPi2EGLFS fix**

- Solution 1
Fix Qt qmake configuration bugs for `raspberrypi` which has different names for `EGL` libraries in new stretch version. Looking into `./qtbase/mkspecs/devices/linux-rasp-pi-g++/qmake.conf` file, all references to `-IEGL` and `-LGLESv2` need to be substituted for `-lbrcmEGL` and `-lbrcmGLESv2` respectively.

```sh
frankchen@raspberrypi: git clone https://github.com/oniongarlic/qt-raspberrypi-configuration.git
frankchen@raspberrypi: cd qt-raspberrypi-configuration && make install DESTDIR=~/Qt/5.12.3/Src/
```

- [Solution 2](https://wiki.qt.io/RaspberryPi2EGLFS)











7. Configure Qt for cross-compilation[Host]

```sh
frankchen@:raspberrypi$ cd ~/Qt/5.12.3/Src/
frankchen@:Src$ ll
total 1324
drwxrwxr-x 45 frankchen frankchen   4096 Jun 14 18:12 ./
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:58 ../
-rw-rw-r--  1 frankchen frankchen   2845 Apr 11 13:56 _clang-format
drwxrwxr-x  5 frankchen frankchen   4096 Jun 10 12:57 coin/
-rw-r--r--  1 frankchen frankchen 170637 Jun 14 18:12 config.cache
-rw-r--r--  1 frankchen frankchen 165172 Jun 14 18:29 config.log
-rw-r--r--  1 frankchen frankchen     29 Jun 14 18:29 .config.notes
-rw-r--r--  1 frankchen frankchen    463 Jun 14 18:21 config.opt
-rwxr-xr-x  1 frankchen frankchen     38 Jun 14 18:12 config.status*
-rw-r--r--  1 frankchen frankchen  11294 Jun 14 18:18 config.summary
drwxr-xr-x 65 frankchen frankchen   4096 Jun 14 18:12 config.tests/
-rwxrwxr-x  1 frankchen frankchen   1935 Apr 11 13:56 configure*
-rw-rw-r--  1 frankchen frankchen   1980 Apr 11 13:56 configure.bat
-rw-rw-r--  1 frankchen frankchen     94 Apr 11 13:56 configure.json
-rw-rw-r--  1 frankchen frankchen   9856 Apr 11 13:56 .gitmodules
drwxrwxr-x  9 frankchen frankchen   4096 Jun 10 12:57 gnuwin32/
-rw-rw-r--  1 frankchen frankchen  22961 Apr 11 13:56 LICENSE.FDL
-rw-rw-r--  1 frankchen frankchen  15351 Apr 11 13:56 LICENSE.GPLv2
-rw-rw-r--  1 frankchen frankchen  35641 Apr 11 13:56 LICENSE.GPLv3
-rw-rw-r--  1 frankchen frankchen  26828 Apr 11 13:56 LICENSE.LGPLv21
-rw-rw-r--  1 frankchen frankchen   8174 Apr 11 13:56 LICENSE.LGPLv3
-rw-rw-r--  1 frankchen frankchen  46903 Apr 11 13:56 LICENSE.QT-LICENSE-AGREEMENT-4.0
-rw-r--r--  1 frankchen frankchen 258687 Jun 14 18:29 Makefile
-rw-r--r--  1 frankchen frankchen     22 Jun 14 17:52 .qmake.cache
-rw-r--r--  1 frankchen frankchen   2789 Jun 14 17:52 .qmake.stash
-rw-r--r--  1 frankchen frankchen    117 Jun 14 18:13 .qmake.super
drwxrwxr-x 10 frankchen frankchen   4096 Jun 10 12:56 qt3d/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtactiveqt/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qtandroidextras/
drwxrwxr-x 14 frankchen frankchen   4096 Jun 14 18:13 qtbase/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qtcanvas3d/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtcharts/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtconnectivity/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qtdatavis3d/
drwxrwxr-x 10 frankchen frankchen   4096 Jun 10 12:56 qtdeclarative/
drwxrwxr-x  6 frankchen frankchen   4096 Jun 10 12:56 qtdoc/
-rw-rw-r--  1 frankchen frankchen  65846 Apr 12 02:44 .QT-ENTERPRISE-LICENSE-AGREEMENT
-rw-rw-r--  1 frankchen frankchen  65846 Apr 12 02:44 .QT-FOR-APPLICATION-DEVELOPMENT-LICENSE-AGREEMENT
-rw-rw-r--  1 frankchen frankchen  65846 Apr 12 02:44 .QT-FOR-AUTOMATION-LICENSE-AGREEMENT
-rw-rw-r--  1 frankchen frankchen  46475 Apr 12 02:44 .QT-FOR-AUTOMOTIVE-LICENSE-AGREEMENT
-rw-rw-r--  1 frankchen frankchen  65846 Apr 12 02:44 .QT-FOR-DEVICE-CREATION-LICENSE-AGREEMENT
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtgamepad/
drwxrwxr-x  6 frankchen frankchen   4096 Jun 10 12:56 qtgraphicaleffects/
drwxrwxr-x  6 frankchen frankchen   4096 Jun 10 12:56 qtimageformats/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtlocation/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qtmacextras/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtmultimedia/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qtnetworkauth/
-rw-rw-r--  1 frankchen frankchen   2962 Apr 11 13:56 qt.pro
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qtpurchasing/
drwxrwxr-x  6 frankchen frankchen   4096 Jun 10 12:56 qtquickcontrols/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qtquickcontrols2/
drwxrwxr-x  9 frankchen frankchen   4096 Jun 10 12:56 qtremoteobjects/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtscript/
drwxrwxr-x  9 frankchen frankchen   4096 Jun 10 12:56 qtscxml/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtsensors/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtserialbus/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtserialport/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtspeech/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtsvg/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qttools/
drwxrwxr-x  3 frankchen frankchen   4096 Jun 10 12:56 qttranslations/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qtvirtualkeyboard/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:56 qtwayland/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:56 qtwebchannel/
drwxrwxr-x 10 frankchen frankchen   4096 Jun 10 12:57 qtwebengine/
drwxrwxr-x  5 frankchen frankchen   4096 Jun 10 12:57 qtwebglplugin/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:57 qtwebsockets/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:57 qtwebview/
drwxrwxr-x  7 frankchen frankchen   4096 Jun 10 12:57 qtwinextras/
drwxrwxr-x  6 frankchen frankchen   4096 Jun 10 12:57 qtx11extras/
drwxrwxr-x  8 frankchen frankchen   4096 Jun 10 12:57 qtxmlpatterns/
-rw-rw-r--  1 frankchen frankchen   3842 Apr 11 13:56 README
-rw-rw-r--  1 frankchen frankchen     41 Apr 11 13:56 .tag

# configure `ENV` for later usage in convenience
frankchen@:Src$ export RPI_TOOLCHAIN=/home/frankchen/Documents/raspberrypi/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin/arm-linux-gnueabihf-
frankchen@:Src$ export RPI_SYSROOT=/home/frankchen/Documents/raspberrypi/sysroot

# configure
frankchen@:Src$ ./configure -release \
    -opensource -confirm-license \
    -opengl es2 \
    -device linux-rasp-pi-g++ \
    -device-option CROSS_COMPILE=$RPI_TOOLCHAIN \
    -sysroot $RPI_SYSROOT \
    -make libs \
    -skip qtwayland -skip qtlocation -skip qtscript \
    -prefix /usr/local/qt5pi \
    -extprefix ~/Documents/raspberrypi/qt5pi \
    -hostprefix ~/Documents/raspberrypi/qt5 \
    -no-use-gold-linker -no-gbm -v


```

**Note:**
> using `-skip` to circumvent some modules that have no need to install or have `make` caused errors.
> `extprefix` indicates the host folder path the `qt` libs(these libs are used in `raspberryPi` device) will be installed into. `hostprefix` signs the host directory the `qt` tools(`qmake`, ..etc, these tools are used in `linux` host) will be installed into. [more details](https://doc.qt.io/qt-5/embedded-linux.html#configure-a-specific-device)

8.  Compile Qt source libraries and install them into `host` and `raspberrypi`. [Host]
  
```sh
# it will take couple of hours depending on your host machine
frankchen@:Src$ clean
frankchen@:Src$ make
frankchen@:Src$ make install

# check
frankchen@:raspberrypi$ ll ~/Documents/raspberrypi/qt5
total 20
drwxr-xr-x  5 frankchen frankchen 4096 Jun 21 18:15 ./
drwxr-xr-x  6 frankchen frankchen 4096 Jun 24 09:25 ../
drwxr-xr-x  2 frankchen frankchen 4096 Jun 24 12:24 bin/
drwxr-xr-x  2 frankchen frankchen 4096 Jun 24 12:23 lib/
drwxr-xr-x 81 frankchen frankchen 4096 Jun 24 12:23 mkspecs/
frankchen@:raspberrypi$ ll ~/Documents/raspberrypi/qt5pi/
total 60
drwxr-xr-x  9 frankchen frankchen  4096 Jun 24 12:24 ./
drwxr-xr-x  6 frankchen frankchen  4096 Jun 24 09:25 ../
drwxr-xr-x  2 frankchen frankchen  4096 Jun 24 12:24 bin/
drwxr-xr-x  3 frankchen frankchen  4096 Jun 24 09:25 doc/
drwxr-xr-x 76 frankchen frankchen  4096 Jun 24 12:24 include/
drwxr-xr-x  4 frankchen frankchen 20480 Jun 24 12:24 lib/
drwxr-xr-x 24 frankchen frankchen  4096 Jun 24 09:26 plugins/
drwxr-xr-x 21 frankchen frankchen  4096 Jun 24 12:24 qml/
drwxr-xr-x  2 frankchen frankchen 12288 Jun 24 12:24 translations/

# deploy to `raspberrypi`
frankchen@:raspberrypi$ rsync -avz qt5pi pi@raspberrypi.local:/usr/local

```

9.  Build a `Qt` application for `raspberryPi` on linux host.[Host]

```sh
# ll
frankchen@:qt-project$ ll
total 24
drwxr-xr-x  6 frankchen frankchen 4096 Jun 17 16:34 ./
drwxrwxrwx 24 frankchen frankchen 4096 Jun 13 16:14 ../
drwxrwxr-x  2 frankchen frankchen 4096 Jun 13 15:12 build-TextFinder-Android_for_arm64_v8a_Clang_Qt_5_12_3_for_Android_ARM64_v8a-Release/
drwxr-xr-x  2 frankchen frankchen 4096 Jun 12 12:50 build-TextFinder-Desktop_Qt_5_12_3_GCC_64bit-Release/
drwxr-xr-x  2 frankchen frankchen 4096 Jun 12 16:26 build-TextFinder-Desktop_Qt_5_12_3_Win/
drwxrwxr-x  2 frankchen frankchen 4096 Jun 13 15:12 TextFinder/

# application source
frankchen@:qt-project$ ll TextFinder/
total 144
drwxrwxr-x 2 frankchen frankchen   4096 Jun 13 15:12 ./
drwxr-xr-x 6 frankchen frankchen   4096 Jun 17 16:34 ../
-rw-rw-r-- 1 frankchen frankchen    308 Jun 11 12:48 input.txt
-rw-rw-r-- 1 frankchen frankchen    172 Jun 11 12:28 main.cpp
-rw-rw-r-- 1 frankchen frankchen    807 Jun 11 12:55 textfinder.cpp
-rw-rw-r-- 1 frankchen frankchen    364 Jun 11 12:40 textfinder.h
-rw-r--r-- 1 frankchen frankchen    350 Jun 12 11:41 textfinder_plugin_import.cpp
-rw-rw-r-- 1 frankchen frankchen   1275 Jun 11 12:45 TextFinder.pro
-rw-rw-r-- 1 frankchen frankchen 100907 Jun 13 15:12 TextFinder.pro.user
-rw-rw-r-- 1 frankchen frankchen     88 Jun 11 12:49 textfinder.qrc
-rw-rw-r-- 1 frankchen frankchen   1294 Jun 11 12:43 textfinder.ui
-rw-r--r-- 1 frankchen frankchen   2982 Jun 12 11:42 ui_textfinder.h

# create target build folder
frankchen@:qt-project$ mkdir build-TextFinder-RaspberryPi
frankchen@:qt-project$ cd build-TextFinder-RaspberryPi/

# create `Makefile` file using `qmake` from our previous built `Qt`
frankchen@:build-TextFinder-RaspberryPi$ "/home/frankchen/Documents/raspberrypi/qt5/bin/qmake" /home/frankchen/Documents/qt-project/TextFinder/TextFinder.pro -spec devices/linux-rasp-pi-g++ CONFIG+=qtquickcompiler
Info: creating stash file /home/frankchen/Documents/qt-project/build-TextFinder-RaspberryPi/.qmake.stash
frankchen@:build-TextFinder-RaspberryPi$ ll
total 76
drwxr-xr-x 2 frankchen frankchen  4096 Jun 17 16:36 ./
drwxr-xr-x 7 frankchen frankchen  4096 Jun 17 16:35 ../
-rw-r--r-- 1 frankchen frankchen 62871 Jun 17 16:36 Makefile
-rw-r--r-- 1 frankchen frankchen  2015 Jun 17 16:36 .qmake.stash

# Use `Makefile` to build application
frankchen@:build-TextFinder-RaspberryPi$ make -j4
frankchen@:build-TextFinder-RaspberryPi$ ll
total 160
drwxr-xr-x 2 frankchen frankchen  4096 Jun 17 16:39 ./
drwxr-xr-x 7 frankchen frankchen  4096 Jun 17 16:35 ../
-rw-r--r-- 1 frankchen frankchen  1840 Jun 17 16:39 main.o
-rw-r--r-- 1 frankchen frankchen 62871 Jun 17 16:36 Makefile
-rw-r--r-- 1 frankchen frankchen 12040 Jun 17 16:38 moc_predefs.h
-rw-r--r-- 1 frankchen frankchen  3411 Jun 17 16:38 moc_textfinder.cpp
-rw-r--r-- 1 frankchen frankchen  6804 Jun 17 16:39 moc_textfinder.o
-rw-r--r-- 1 frankchen frankchen  2015 Jun 17 16:36 .qmake.stash
-rw-r--r-- 1 frankchen frankchen  4029 Jun 17 16:38 qrc_textfinder.cpp
-rw-r--r-- 1 frankchen frankchen  3220 Jun 17 16:38 qrc_textfinder.o
-rwxr-xr-x 1 frankchen frankchen 30224 Jun 17 16:39 TextFinder*
-rw-r--r-- 1 frankchen frankchen  9776 Jun 17 16:39 textfinder.o
-rw-r--r-- 1 frankchen frankchen  2982 Jun 17 16:38 ui_textfinder.h
frankchen@:build-TextFinder-RaspberryPi$ file TextFinder 
TextFinder: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-, for GNU/Linux 3.2.0, BuildID[sha1]=fcbc9b1ee203db6b9ae8ff4b9fe783d1183c9775, not stripped

```

**Note:**
> The application `TextFinder` is dymanic linking, if you execute it on a `Raspberrt Pi` device without `Qt` libs, there will be error as following
> `./TextFinder: error while loading shared libraries: libQt5Widgets.so.5: cannot open shared object file: No such file or directory`
> To build a static linking Qt program, seeing [Linking to Static Builds of Qt](https://doc.qt.io/QtForDeviceCreation/qtee-static-linking.html) 

10.  Deploy the application to `raspberrypi` device.

```sh
# on `linux` host
frankchen@:build-TextFinder-RaspberryPi$ rsync TextFinder pi@raspberrypi.local:~/


# on `raspberrypi`
pi@raspberrypi:~ $ ./TextFinder
```


**References:**
* [Cross-compile and deploy Qt 5.12 for Raspberry Pi](https://mechatronicsblog.com/cross-compile-and-deploy-qt-5-12-for-raspberry-pi/)
* [How to cross compile QT for Raspberry Pi 3 on Linux (Ubuntu) for Beginners!](https://medium.com/@amirmann/how-to-cross-compile-qt-for-raspberry-pi-3-on-linux-ubuntu-for-beginners-75acf2a078c)
* [Building Qt 5.12 LTS for Raspberry Pi on Debian Stretch](https://www.tal.org/tutorials/building-qt-512-raspberry-pi)
* [OpenGL ES2 error while Cross Compiling Qt5.11 for Raspbian Stretch with desktop](https://www.raspberrypi.org/forums/viewtopic.php?t=227408)
* [Segmentation fault outside Qt Creator only](https://forum.qt.io/topic/89672/segmentation-fault-outside-qt-creator-only/14)








### Compile Qt program for `nVidia Jetson TX2` on Linux host(advanced example)

There are two major steps:
- build `Qt` for a given `nVidia Jetson TX2` device on Linux host.
- build the `Qt` application using the above comipled `Qt` libs.


1. `Jetson TX2` os image.

    [NVIDIA JetPack Software](https://developer.nvidia.com/embedded/develop/software)

    ```sh
    frankchen@:jetson-tx2$ ll /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/
    total 96
    drwxr-xr-x  21 root      root       4096 Jun 18 16:36 ./
    drwxr-xr-x   6 frankchen frankchen  4096 Mar 13 15:40 ../
    drwxr-xr-x   2 root      root       4096 Feb 20 15:22 bin/
    drwxr-xr-x   3 root      root       4096 Jun 18 16:37 boot/
    drwxr-xr-x   2 root      root       4096 May 18  2018 dev/
    drwxr-xr-x 135 root      root      12288 Jun 18 16:37 etc/
    drwxr-xr-x   2 root      root       4096 Apr 24  2018 home/
    drwxr-xr-x  21 root      root       4096 Jun 18 16:37 lib/
    drwxr-xr-x   2 root      root       4096 Aug  6  2018 media/
    drwxr-xr-x   2 root      root       4096 Apr 27  2018 mnt/
    drwxr-xr-x   3 root      root       4096 Jun 18 16:37 opt/
    drwxr-xr-x   2 root      root       4096 Apr 24  2018 proc/
    -rw-r--r--   1 frankchen frankchen    62 Mar 13 15:40 README.txt
    drwx------   2 root      root       4096 Apr 27  2018 root/
    drwxr-xr-x  16 root      root       4096 Jan  4 09:20 run/
    drwxr-xr-x   2 root      root       4096 Feb 20 15:22 sbin/
    drwxr-xr-x   2 root      root       4096 May 11  2018 snap/
    drwxr-xr-x   2 root      root       4096 Apr 27  2018 srv/
    drwxr-xr-x   2 root      root       4096 Apr 24  2018 sys/
    drwxrwxrwt   2 root      root       4096 Feb 21 19:52 tmp/
    drwxr-xr-x  11 root      root       4096 May 21  2018 usr/
    drwxr-xr-x  15 root      root       4096 Jun 18 16:37 var/

    ```

2. toolchains for `Jetson TX2` on linux. 

    go to [Linaro Download Center](https://releases.linaro.org/components/toolchain/binaries/5.5-2017.10/aarch64-linux-gnu/), find product with title `5.5.0-2017.10-x86_64_arrch64`.

    ```sh
    frankchen@:jetson-tx2$ tar -xvf ~/Downloads/gcc-linaro-5.5.0-2017.10-x86_64_aarch64-linux-gnu.tar.xz
    frankchen@:jetson-tx2$ mv gcc-linaro-7.4.1-2019.02-x86_64_aarch64-linux-gnu/ toolchains/
    frankchen@:jetson-tx2$ ll toolchains/
    total 16
    drwxr-xr-x 4 frankchen frankchen 4096 Jun 20 17:13 ./
    drwxr-xr-x 4 frankchen frankchen 4096 Jun 20 17:01 ../
    drwxr-xr-x 8 frankchen frankchen 4096 Jan 28  2017 gcc-linaro-5.4.1-2017.01-x86_64_aarch64-linux-gnu/
    drwxr-xr-x 8 frankchen frankchen 4096 Jan 23 04:22 gcc-linaro-5.5.0-2017.10-x86_64_aarch64-linux-gnu/

    ```

    symbolic link tool,

    ```sh
    frankchen@:jetson-tx2$ wget https://raw.githubusercontent.com/riscv/riscv-poky/master/scripts/sysroot-relativelinks.py
    frankchen@:jetson-tx2$ chmod +x ./sysroot-relativelinks.py
    frankchen@:jetson-tx2$ sudo ./sysroot-relativelinks.py $TX2_SYSROOT 
    ```

    **Note:**

    ```sh
    # Ubuntu 18.04, the toolchain maybe have errors below
    frankchen@:jetson-tx2$ ./toolchains/bin/aarch64-unknown-linux-gnu-gcc
    aarch64-unknown-linux-gnu-gcc: loadlocale.c:129: _nl_intern_locale_data: Assertion ''cnt < (sizeof (_nl_value_type_LC_TIME) / sizeof (_nl_value_type_LC_TIME[0]))'' failed.
    Aborted (core dumped)
    # Fix
    frankchen@:jetson-tx2$ export LC_ALL=C
    frankchen@:jetson-tx2$ ./toolchains/bin/aarch64-unknown-linux-gnu-gcc
    aarch64-unknown-linux-gnu-gcc: fatal error: no input files
    compilation terminated.
    # Sysroot for the toolchain
    frankchen@:jetson-tx2$ ./toolchains/bin/aarch64-unknown-linux-gnu-gcc --print-sysroot
    /home/frankchen/Documents/jetson-tx2/toolchains/bin/../aarch64-unknown-linux-gnu/sysroot

    ```

3. configure to build `Qt` for `nvidia Jetson TX2` on linux host

    ```sh
    # cd <QT_SRC>
    frankchen@:jetson-tx2$ cd ~/Qt/5.12.3/Src/

    # set ENV
    frankchen@:jetson-tx2$ export TX2_SYSROOT=/home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs
    frankchen@:jetson-tx2$ export TX2_TOOLCHAIN=/home/frankchen/Documents/jetson-tx2/toolchains/gcc-linaro-5.5.0-2017.10-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-

    # configure
    frankchen@:Src$ ./configure -opensource -confirm-license \
        -release \
        -device linux-jetson-tx2-g++ \
        -device-option CROSS_COMPILE=$TX2_TOOLCHAIN \
        -sysroot $TX2_SYSROOT \
        -extprefix ~/Documents/jetson-tx2/qt5-jetson-tx2 \
        -nomake tests -nomake examples \
        -skip qtwayland -skip qtlocation -skip qtscript

    ```

    **Note:**
    > -prefix, -extprefix, and -hostprefix control the intended destination directory of the Qt build. In the above example the ARM build of Qt is expected to be placed in /usr/local/qt5 on the target device. Note that running make install does not deploy anything to the device. Instead, the install step targets the directory specified by extprefix which defaults to sysroot + prefix and is therefore optional. However, in many cases "polluting" the sysroot is not desirable and thus specifying -extprefix becomes important. Finally, -hostprefix allows separating host tools like qmake, rcc, uic from the binaries for the target. When given, such tools will be installed under the specified directory instead of extprefix.


4. make build
    
    ```sh
    frankchen@:Src$ make clean
    frankchen@:Src$ make -j4
    frankchen@:Src$ make install
    # the Qt libs will be installed into  `extprefix` folder
    frankchen@:Src$ ll ~/Documents/jetson-tx2/qt5-jetson-tx2/
    total 64
    drwxr-xr-x 10 frankchen frankchen  4096 Jun 20 19:20 ./
    drwxr-xr-x  4 frankchen frankchen  4096 Jun 20 17:01 ../
    drwxr-xr-x  2 frankchen frankchen  4096 Jun 20 19:20 bin/
    drwxr-xr-x  3 frankchen frankchen  4096 Jun 20 14:11 doc/
    drwxr-xr-x 76 frankchen frankchen  4096 Jun 20 19:20 include/
    drwxr-xr-x  4 frankchen frankchen 20480 Jun 20 19:20 lib/
    drwxr-xr-x 79 frankchen frankchen  4096 Jun 20 19:19 mkspecs/
    drwxr-xr-x 22 frankchen frankchen  4096 Jun 20 19:20 plugins/
    drwxr-xr-x 23 frankchen frankchen  4096 Jun 20 19:20 qml/
    drwxr-xr-x  2 frankchen frankchen 12288 Jun 20 19:20 translations/

    ```


    **Problems:**

    1. errors when building `libwebp`,

    ```sh
    frankchen@:Src$ make
    make[5]: Entering directory '/home/frankchen/Qt/5.12.3/Src/qtimageformats/src/plugins/imageformats/webp'
    /home/frankchen/Documents/jetson-tx2/toolchains/gcc-linaro-5.4.1-2017.01-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-gcc -c -pipe -mtune=cortex-a57.cortex-a53 -march=armv8-a --sysroot=/home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs -O2 -std=gnu11 -fvisibility=hidden -fno-exceptions -Wall -W -D_REENTRANT -fPIC -DQT_DEPRECATED_WARNINGS -DQT_NO_NARROWING_CONVERSIONS_IN_CONNECT -DQT_NO_EXCEPTIONS -D_LARGEFILE64_SOURCE -D_LARGEFILE_SOURCE -DQT_NO_DEBUG -DQT_PLUGIN -DQT_GUI_LIB -DQT_CORE_LIB -I. -I../../../3rdparty/libwebp -I../../../3rdparty/libwebp/src -I../../../3rdparty/libwebp/src/dec -I../../../3rdparty/libwebp/src/enc -I../../../3rdparty/libwebp/src/dsp -I../../../3rdparty/libwebp/src/mux -I../../../3rdparty/libwebp/src/utils -I../../../3rdparty/libwebp/src/webp -I/home/frankchen/Qt/5.12.3/Src/qtbase/include -I/home/frankchen/Qt/5.12.3/Src/qtbase/include/QtGui -I/home/frankchen/Qt/5.12.3/Src/qtbase/include/QtCore -I.moc -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include/libdrm -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include/aarch64-linux-gnu -I/home/frankchen/Qt/5.12.3/Src/qtbase/mkspecs/devices/linux-jetson-tx2-g++ -o .obj/dec_neon.o ../../../3rdparty/libwebp/src/dsp/dec_neon.c
    ../../../3rdparty/libwebp/src/dsp/dec_neon.c: In function 'SimpleHFilter16_NEON':
    ../../../3rdparty/libwebp/src/dsp/dec_neon.c:531:1: internal compiler error: in record_operand_use, at regrename.c:220
    }
    ^

    # enter into the folder to better tackle this issue
    frankchen@:Src$ cd /home/frankchen/Qt/5.12.3/Src/qtimageformats/src/plugins/imageformats/webp
    frankchen@:webp$ make clean
    frankchen@:webp$ /home/frankchen/Documents/jetson-tx2/toolchains/gcc-linaro-5.4.1-2017.01-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-gcc -c -pipe -mtune=cortex-a57.cortex-a53 -march=armv8-a --sysroot=/home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs -O2 -std=gnu11 -fvisibility=hidden -fno-exceptions -Wall -W -D_REENTRANT -fPIC -DQT_DEPRECATED_WARNINGS -DQT_NO_NARROWING_CONVERSIONS_IN_CONNECT -DQT_NO_EXCEPTIONS -D_LARGEFILE64_SOURCE -D_LARGEFILE_SOURCE -DQT_NO_DEBUG -DQT_PLUGIN -DQT_GUI_LIB -DQT_CORE_LIB -I. -I../../../3rdparty/libwebp -I../../../3rdparty/libwebp/src -I../../../3rdparty/libwebp/src/dec -I../../../3rdparty/libwebp/src/enc -I../../../3rdparty/libwebp/src/dsp -I../../../3rdparty/libwebp/src/mux -I../../../3rdparty/libwebp/src/utils -I../../../3rdparty/libwebp/src/webp -I/home/frankchen/Qt/5.12.3/Src/qtbase/include -I/home/frankchen/Qt/5.12.3/Src/qtbase/include/QtGui -I/home/frankchen/Qt/5.12.3/Src/qtbase/include/QtCore -I.moc -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include/libdrm -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include/aarch64-linux-gnu -I/home/frankchen/Qt/5.12.3/Src/qtbase/mkspecs/devices/linux-jetson-tx2-g++ -o .obj/dec_neon.o ../../../3rdparty/libwebp/src/dsp/dec_neon.c
    ../../../3rdparty/libwebp/src/dsp/dec_neon.c: In function 'SimpleHFilter16_NEON':
    ../../../3rdparty/libwebp/src/dsp/dec_neon.c:531:1: internal compiler error: in record_operand_use, at regrename.c:220
    }
    ^
    Please submit a full bug report,
    with preprocessed source if appropriate.
    See <http://gcc.gnu.org/bugs.html> for instructions.


    # possible solution, using the linaro toolchain with new version(5.5.0-2017.10) maybe fix the bug
    frankchen@:webp$ make clean
    frankchen@:webp$ /home/frankchen/Documents/jetson-tx2/toolchains/gcc-linaro-5.5.0-2017.10-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-gcc -c -pipe -mtune=cortex-a57.cortex-a53 -march=armv8-a --sysroot=/home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs -O2 -std=gnu11 -fvisibility=hidden -fno-exceptions -Wall -W -D_REENTRANT -fPIC -DQT_DEPRECATED_WARNINGS -DQT_NO_NARROWING_CONVERSIONS_IN_CONNECT -DQT_NO_EXCEPTIONS -D_LARGEFILE64_SOURCE -D_LARGEFILE_SOURCE -DQT_NO_DEBUG -DQT_PLUGIN -DQT_GUI_LIB -DQT_CORE_LIB -I. -I../../../3rdparty/libwebp -I../../../3rdparty/libwebp/src -I../../../3rdparty/libwebp/src/dec -I../../../3rdparty/libwebp/src/enc -I../../../3rdparty/libwebp/src/dsp -I../../../3rdparty/libwebp/src/mux -I../../../3rdparty/libwebp/src/utils -I../../../3rdparty/libwebp/src/webp -I/home/frankchen/Qt/5.12.3/Src/qtbase/include -I/home/frankchen/Qt/5.12.3/Src/qtbase/include/QtGui -I/home/frankchen/Qt/5.12.3/Src/qtbase/include/QtCore -I.moc -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include/libdrm -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include/aarch64-linux-gnu -I/home/frankchen/Qt/5.12.3/Src/qtbase/mkspecs/devices/linux-jetson-tx2-g++ -o .obj/dec_neon.o ../../../3rdparty/libwebp/src/dsp/dec_neon.c

    ```

    similiar problems found online:
    * (Internal compiler error using -mtune=cortex-a57.cortex-a53 with linaro gcc 5.2.1)[https://bugs.linaro.org/show_bug.cgi?id=2785]
    * (Errors buliding libwebp on NVIDIA TX2 with Linaro gcc-5.4.0 using flags)[https://github.com/opencv/opencv/issues/12322]
    * (internal compiler error in record_operand_use)[https://www.mail-archive.com/gcc-bugs@gcc.gnu.org/msg472065.html]

    1. stdlib.h

    ```sh
    make[3]: Entering directory '/home/frankchen/Qt/5.12.3/Src/qtbase/src/corelib'
    /home/frankchen/Documents/jetson-tx2/toolchains/gcc-linaro-7.4.1-2019.02-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-g++ -pipe -mtune=cortex-a57.cortex-a53 -march=armv8-a --sysroot=/home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs -O3 -std=c++1y -fvisibility=hidden -fvisibility-inlines-hidden -Wall -W -Wvla -Wdate-time -D_REENTRANT -fPIC -DQT_NO_USING_NAMESPACE -DQT_NO_FOREACH -DQT_NO_NARROWING_CONVERSIONS_IN_CONNECT -DQT_BUILD_CORE_LIB -DQT_BUILDING_QT -DQT_NO_CAST_TO_ASCII -DQT_ASCII_CAST_WARNINGS -DQT_MOC_COMPAT -DQT_USE_QSTRINGBUILDER -DQT_DEPRECATED_WARNINGS -DQT_DISABLE_DEPRECATED_BEFORE=0x050000 -D_LARGEFILE64_SOURCE -D_LARGEFILE_SOURCE -DQT_NO_DEBUG -DPCRE2_CODE_UNIT_WIDTH=16 -I. -Iglobal -I../3rdparty/harfbuzz/src -I../3rdparty/md5 -I../3rdparty/md4 -I../3rdparty/sha3 -I../3rdparty -I../3rdparty/double-conversion/include -I../3rdparty/double-conversion/include/double-conversion -I../3rdparty/forkfd -I../3rdparty/tinycbor/src -I../../include -I../../include/QtCore -I../../include/QtCore/5.12.3 -I../../include/QtCore/5.12.3/QtCore -I.moc -I.tracegen -I../3rdparty/pcre2/src -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include/glib-2.0 -I/home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/lib/aarch64-linux-gnu/glib-2.0/include -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include -isystem /home/frankchen/nvidia/nvidia_sdk/JetPack_4.2_Linux_P3310/Linux_for_Tegra/rootfs/usr/include/aarch64-linux-gnu -I../../mkspecs/devices/linux-jetson-tx2-g++ -x c++-header -c global/qt_pch.h -o .pch/Qt5Core.gch/c++
    In file included from /home/frankchen/Documents/jetson-tx2/toolchains/gcc-linaro-7.4.1-2019.02-x86_64_aarch64-linux-gnu/aarch64-linux-gnu/include/c++/7.4.1/bits/stl_algo.h:59:0,
                    from /home/frankchen/Documents/jetson-tx2/toolchains/gcc-linaro-7.4.1-2019.02-x86_64_aarch64-linux-gnu/aarch64-linux-gnu/include/c++/7.4.1/algorithm:62,
                    from global/qglobal.h:142,
                    from global/qt_pch.h:56:
    /home/frankchen/Documents/jetson-tx2/toolchains/gcc-linaro-7.4.1-2019.02-x86_64_aarch64-linux-gnu/aarch64-linux-gnu/include/c++/7.4.1/cstdlib:75:15: fatal error: stdlib.h: No such file or directory
    #include_next <stdlib.h>
                ^~~~~~~~~~
    # possible solution, using the linaro toolchain with new version(5.5.0-2017.10) maybe fix the bug
    ```

5. build a `Qt` application for `Jetson TX2` on linux host

    ```sh
    # cd <Project folder>
    frankchen@:build-TextFinder-JetsonTx2$ cd ~/Documents/qt-project/
    frankchen@:qt-project$ ll
    total 32
    drwxr-xr-x  8 frankchen frankchen 4096 Jun 21 11:00 ./
    drwxrwxrwx 26 frankchen frankchen 4096 Jun 18 17:11 ../
    drwxrwxr-x  2 frankchen frankchen 4096 Jun 13 15:12 build-TextFinder-Android_for_arm64_v8a_Clang_Qt_5_12_3_for_Android_ARM64_v8a-Release/
    drwxr-xr-x  2 frankchen frankchen 4096 Jun 12 12:50 build-TextFinder-Desktop_Qt_5_12_3_GCC_64bit-Release/
    drwxr-xr-x  2 frankchen frankchen 4096 Jun 12 16:26 build-TextFinder-Desktop_Qt_5_12_3_Win/
    drwxr-xr-x  2 frankchen frankchen 4096 Jun 21 11:03 build-TextFinder-JetsonTx2/
    drwxr-xr-x  2 frankchen frankchen 4096 Jun 17 16:39 build-TextFinder-RaspberryPi/
    drwxrwxr-x  2 frankchen frankchen 4096 Jun 13 15:12 TextFinder/

    # create build folder and cd into
    frankchen@:qt-project$ mkdir build-TextFinder-JetsonTx2
    frankchen@:qt-project$ cd build-TextFinder-JetsonTx2/

    # create `Makefile` using `qmake` tool
    frankchen@:build-TextFinder-JetsonTx2$ "/home/frankchen/Documents/jetson-tx2/qt5-jetson-tx2/bin/qmake" /home/frankchen/Documents/qt-project/TextFinder/TextFinder.pro

    # build executable file
    frankchen@:build-TextFinder-JetsonTx2$ make -j4
    frankchen@:build-TextFinder-JetsonTx2$ file TextFinder 
    TextFinder: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-, for GNU/Linux 3.7.0, BuildID[sha1]=248f556bb9b9dfa0329b54b918f919ce406da67b, not stripped

    ```

**References:**
* [NVIDIA JetPack Software](https://developer.nvidia.com/embedded/develop/software)
* [CUDA Development for Jetson with NVIDIA Nsight Eclipse Edition](https://devblogs.nvidia.com/cuda-jetson-nvidia-nsight-eclipse-edition/)



### Compile Qt program for `nVidia Jetson Nano` device on Linux host(advanced example)

**Steps:**

1. Download the [Jetson Nano Image](https://developer.download.nvidia.com/assets/embedded/downloads/jetson-nano-sd-card-image/r32.1.1-2019-05-31/jetson-nano-sd-r32.1.1-2019-05-31.zip), write the image to a sd card.[Host] 

*References:*
[Write Image to the microSD Card](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)


2. Install development libraries.[Nano]

```sh
# enable sudo without password
jetson@jetson-desktop:~$ sudo visudo
# At the end of the /etc/sudoers file add this line:
jetson     ALL=(ALL) NOPASSWD:ALL

# install development libs

## uncomment the deb-src line in the /etc/apt/sources.list file
jetson@jetson-desktop:~ $ sudo vim /etc/apt/sources.list

## update and install the required development packages
jetson@jetson-desktop:~ $ sudo apt-get update
jetson@jetson-desktop:~$ sudo apt-get build-dep qtdeclarative5-dev
jetson@jetson-desktop:~ $ sudo apt-get install libudev-dev libinput-dev libts-dev libxcb-xinerama0-dev libxcb-xinerama0
jetson@jetson-desktop:~$ sudo apt-get install rsync
```

3. Prepare target folder.[Nano]

```sh
jetson@jetson-desktop:~$ export TARGET=/usr/local/qt5-jetson-nano
jetson@jetson-desktop:~$ sudo mkdir $TARGET
jetson@jetson-desktop:~$ sudo chown jetson:jetson $TARGET
```

4. Install Qt-5.12.3 source.[Host]

[Qt Downloads](https://download.qt.io/archive/qt/5.12/5.12.3/single/)

```sh
# prepare a clean source folder, avoid using the built source folder
frankchen@:Src$ cd /home/frankchen/Qt/5.12.3/Src
```

5. Create working folder, set up `sysroot`, `toolchains` and other tools.[Host]

**workding folder**
```sh
frankchen@~$: mkdir -p ~/Documents/jetson-nano/
frankchen@~$: cd ~/Documents/jetson-nano/
```

**sysroot**
```sh
frankchen@jetson-nano$: mkdir sysroot sysroot/usr
frankchen@jetson-nano$: rsync -avz jetson@jetson-desktop.local:/lib sysroot
frankchen@jetson-nano$: rsync -avz jetson@jetson-desktop.local:/usr/include sysroot/usr
frankchen@jetson-nano$: rsync -avz jetson@jetson-desktop.local:/usr/lib sysroot/usr
```


**toolchians**[](https://developer.nvidia.com/embedded/linux-tegra)

```sh
frankchen@:jetson-nano$: mkdir toolchains
frankchen@:jetson-nano$ wget https://developer.download.nvidia.com/embedded/L4T/r31_Release_v1.0/BSP/gcc-linaro-6.4.1-2017.08-x86_64_aarch64-linux-gnu.tar.xz -P ./toolchains
frankchen@:jetson-nano$ cd toolchains && tar -zvf gcc-linaro-6.4.1-2017.08-x86_64_aarch64-linux-gnu.tar.xz && cd ..
```

**symbolic link tool**

```sh
frankchen@jetson-nano: wget https://raw.githubusercontent.com/riscv/riscv-poky/master/scripts/sysroot-relativelinks.py
frankchen@jetson-nano: chmod +x ./sysroot-relativelinks.py
frankchen@jetson-nano: sudo ./sysroot-relativelinks.py sysroot
```


6. Configure Qt for cross compile.[Host]

```sh
# cd QT_SRC
frankchen@:jetson-nano$ cd ~/Qt/5.12.3/Src/

# create a `linux-jetson-nano-g++` device
frankchen@:Src$ mkdir qtbase/mkspecs/devices/linux-jetson-nano-g++

# create `qmake.conf` and `qplatformdefs.h` under the device[https://github.com/sirspudd/mkspecs/tree/master/linux-jetson-nano-g%2B%2B]


frankchen@:Src$ ll qtbase/mkspecs/devices/linux-jetson-nano-g++
total 16
drwxr-xr-x  2 frankchen frankchen 4096 Jun 26 16:22 ./
drwxrwxr-x 39 frankchen frankchen 4096 Jun 26 16:19 ../
-rw-r--r--  1 frankchen frankchen 1074 Jun 26 16:21 qmake.conf
-rw-r--r--  1 frankchen frankchen 1959 Jun 26 16:22 qplatformdefs.h

# configure `ENV` for later usage in convenience
frankchen@:Src$ export JETSON_TOOLCHAIN=/home/frankchen/Documents/jetson-nano/toolchains/gcc-linaro-6.4.1-2017.08-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-

frankchen@:Src$ export JETSON_SYSROOT=/home/frankchen/Documents/jetson-nano/sysroot

frankchen@:Src$ export TARGET=/usr/local/qt5-jetson-nano
# configure
frankchen@:Src$ ./configure -release \
    -opensource -confirm-license \
    -opengl es2 \
    -device linux-jetson-nano-g++ \
    -device-option CROSS_COMPILE=$JETSON_TOOLCHAIN \
    -sysroot $JETSON_SYSROOT \
    -make libs \
    -skip qtwayland -skip qtlocation -skip qtscript \
    -prefix $TARGET \
    -extprefix ~/Documents/jetson-nano/qt5-jetson-nano \
    -hostprefix ~/Documents/jetson-nano/qt5 \
    -no-gbm -v

```

7. Build Qt libraries and install into both host and embedded device.[Host]

```sh
# it will take couple of hours depending on your host machine
frankchen@:jetson-nano$ clean
frankchen@:jetson-nano$ make
frankchen@:jetson-nano$ make install


# deploy to `jetson nano` device
frankchen@:jetson-nano$ rsync -avz qt5-jetson-nano/ jetson@jetson-desktop.local:$TARGET

```

8. Cross compile a Qt application.[Host]

```sh
# 1. create build folder
frankchen@:qt-project$ mkdir build-TextFinder-Jetson_Nano && cd "$_"

# 2. generate `Makefile` file.
frankchen@:build-TextFinder-Jetson_Nano$ "/home/frankchen/Documents/jetson-nano/qt5/bin/qmake" /home/frankchen/Documents/qt-project/TextFinder/TextFinder.pro -spec devices/linux-jetson-nano-g++ CONFIG+=qtquickcompiler

# 3. create application.
frankchen@:build-TextFinder-Jetson_Nano$ "/usr/bin/make" -j4

# 4. deploy application in `jetson nano` device
frankchen@:build-TextFinder-Jetson_Nano$ rsync -avz TextFinder jetson@jetson-desktop.local:~/Documents/
```



9. Run application.[Nano]

```sh
jetson@jetson-desktop:~/Documents$ ./TextFinder
```

**errors:**
> QFontDatabase: Cannnot find font directory /usr/local/qt-5-jetson-nano/lib/fonts....,The reason behind the error is: Qt normally uses `fontconfig` to provide access to system fonts, seeing [more details](https://doc.qt.io/qt-5/qt-embedded-fonts.html). And we backtrack to the `step 6` on configuration for compilation, getting the following:

```sh
Qt Gui:
  Accessibility .......................... yes
  FreeType ............................... yes
    Using system FreeType ................ no
  HarfBuzz ............................... yes
    Using system HarfBuzz ................ yes
  Fontconfig ............................. no

```

We failed to configure the `Fontconfig`, 

There two solutions,
1. Install `freetype` in the `jetson nano` device in `step 2`, and repeat from `step 3`.
2. In the `jetson nano` device, link an existing `fonts` libs to the path `/usr/local/qt-5-jetson-nano/lib/fonts`, such as
   ```sh
   jetson@jetson-desktop:~$ ln -s /usr/share/fonts/truetype/dejavu /usr/local/qt-5-jetson-nano/lib/fonts
   ```




##### References
[Building Qt for Embedded Linux](https://wiki.qt.io/Building_Qt_for_Embedded_Linux)

[Qt 5.13 rc3 on the Nvidia Jetson Nano](https://www.chaos-reins.com/2019-06-19-jetson-nano/)