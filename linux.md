# Linux

## Basic

- [Linux From Scratch](http://www.linuxfromscratch.org)
**Problems**
[Error while installing perl with thread support](https://www.perlmonks.org/?node_id=820920)

[asan_rtl.cc](https://github.com/gcc-mirror/gcc/blob/gcc-8-branch/libsanitizer/asan/asan_rtl.cc)

[What are the "prefix" and "lib" arguments to makefile.pl used for?](https://www.perlmonks.org/?node_id=564720)


- [Pocket Linux Guide](http://tldp.org/LDP/Pocket-Linux-Guide/html/index.html)

- [The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/)



### Hard Drive and OS Boot

[Some basics of MBR v/s GPT and BIOS v/s UEFI](https://wiki.manjaro.org/index.php?title=Some_basics_of_MBR_v/s_GPT_and_BIOS_v/s_UEFI)

[Difference between Legacy BIOS and UEFI](https://askubuntu.com/questions/993269/difference-between-legacy-bios-and-uefi)

[What is the difference in “Boot with BIOS” and “Boot with UEFI”](https://superuser.com/questions/496026/what-is-the-difference-in-boot-with-bios-and-boot-with-uefi)

[Dual boot with BIOS and EFI?](https://superuser.com/questions/1081545/dual-boot-with-bios-and-efi)



- **Partition**
  - MBR
  - GPT

[Partitioning](https://wiki.archlinux.org/index.php/Partitioning)

[How to Create Disk Partitions in Linux](https://tecadmin.net/how-to-create-and-format-disk-partitions-in-linux/)

[How can I change/convert a Ubuntu MBR drive to a GPT, and make Ubuntu boot from EFI?](https://askubuntu.com/questions/84501/how-can-i-change-convert-a-ubuntu-mbr-drive-to-a-gpt-and-make-ubuntu-boot-from)


- **Grub**

[GRUB bootloader - Full tutorial](https://www.dedoimedo.com/computers/grub.html)

[Set up GRUB to boot a Linux SD card (on a Linux computer)](http://linux.lsdev.sil.org/wiki/index.php/Set_up_GRUB_to_boot_a_Linux_SD_card_(on_a_Linux_computer))

[The difference between booting MBR and GPT with GRUB](https://www.anchor.com.au/blog/2012/10/the-difference-between-booting-mbr-and-gpt-with-grub/)

[How grub2 works on a MBR partitioned disk and GPT partitioned disk?](https://superuser.com/questions/1165557/how-grub2-works-on-a-mbr-partitioned-disk-and-gpt-partitioned-disk)

[Where is Grub installed on a GPT disk?](https://askubuntu.com/questions/657179/where-is-grub-installed-on-a-gpt-disk)

[Is it possible to boot Linux from a GPT disk on a BIOS system?](https://superuser.com/questions/1337344/is-it-possible-to-boot-linux-from-a-gpt-disk-on-a-bios-system)



### Windowing System

[Wiki Windowing System](https://en.wikipedia.org/wiki/Windowing_system)

[Display Server](https://en.wikipedia.org/wiki/Display_server)

[X Window System](https://en.wikipedia.org/wiki/X_Window_System)

[Wayland and Ubuntu](https://wiki.ubuntu.com/Wayland)

[Wayland vs Xorg](https://www.secjuice.com/wayland-vs-xorg/)

[X Clients under Wayland (XWayland)](https://wayland.freedesktop.org/xserver.html)


**interesting takeaway:**

```sh
# list the devices on your system:
$ xinput list

# get the recorded key logs on the initial terminal
$ xinput test id

# obtain session ID
$ loginctl
$ loginctl show-session <SESSION_ID> -p Type
# when login into `desktop`
Type=wayland
# when login into `ssh`
Type=tty

```


## Device in Linux

[Embedded Linux Device Drivers](http://linuxembeded.blogspot.com/2014/04/embedded-linux-drivers.html)

[Firmware](https://wiki.ubuntu.com/Kernel/Firmware)

[Firmware](https://wiki.debian.org/Firmware)

[Welcome to the official Linux Wireless wiki](https://wireless.wiki.kernel.org/en/users/Drivers/iwlwifi)



**interests:**

```sh
# list linux kernel modules
$ find /lib/modules/$(uname -r) -type f -name '*.ko'

```


## OS(Operating System)








### Persistent and Full Installation

[Benefits of persistent install over direct install to flashdrives (SD/USB)](https://ubuntuforums.org/showthread.php?t=1655412)

[The Differences Between Persistent Live USB and Full Linux Install on USB](https://www.maketecheasier.com/persistent-live-usb-vs-full-install-usb/)

- **Persistent Install**

[3 Ways To Create A Lightweight And Persistent Xubuntu Linux USB Drive](https://www.lifewire.com/create-lightweight-xubuntu-linux-usb-2202083)

- **Full Install**

[How do I install Ubuntu to a USB key? (without using Startup Disk Creator)](https://askubuntu.com/questions/16988/how-do-i-install-ubuntu-to-a-usb-key-without-using-startup-disk-creator)

[Linux Full Install to USB stick](https://www.linux.org/threads/linux-full-install-to-usb-stick.20921/)(recommend)

[Making a portable full installation of Ubuntu on a USB HDD](https://www.dionysopoulos.me/portable-ubuntu-on-usb-hdd/)

[Installing Broadcom Wireless Drivers](https://askubuntu.com/questions/55868/installing-broadcom-wireless-drivers)














### Virtual Machine

[QEMU vs. VirtualBox](https://www.linuxjournal.com/content/qemu-vs-virtualbox)

[Virtualisation Face-off: Qemu, VirtualBox, VMware Player and Parallels Workstation](https://opensourceforu.com/2012/05/virtualisation-faceoff-qemu-virtualbox-vmware-player-parallels-workstation/)

[How to run Ubuntu desktop on QEMU?](https://askubuntu.com/questions/884534/how-to-run-ubuntu-desktop-on-qemu)

[How To Install And Configure QEMU In Ubuntu](https://www.unixmen.com/how-to-install-and-configure-qemu-in-ubuntu/)

[Difference between KVM and QEMU](https://serverfault.com/questions/208693/difference-between-kvm-and-qemu#)

[How To Use QEMU To Test Operating Systems & Distributions](https://fosspost.org/tutorials/use-qemu-test-operating-systems-distributions)



### Ubuntu

[Upgrade Ubuntu Using an ISO Image File](https://sumtips.com/how-to/upgrade-ubuntu-using-iso-image-file/)







