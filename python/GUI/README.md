# GUI(Graphic User Interface)

## GUI toolkits for Python
Depending on the platform's GUI toolkits, such as `Gtk+`, `Qt`, `FLTK`, `wxWidgets` or `Tcl/Tk`.

## Tkinter

Standard builds of Python include an object-oriented interface to the `Tcl/Tk` widget set, since it comes included with most binary distributions of Python.
However, if you use slim python which is common in python docker image, you need to install the `binary distributions` of Tkinter safely as like in debian linux, 

```sh
apt-get install python3-tk
```


## wxPython(wxWidgets\Gtk+)

- Windows and macOS
based on `wxWidgets`

```sh
pip install -U wxPython
```

- Linux Wheels.
Differences between Linux distributions bring about different binary wheels based on `gtk3 or gtk2`.

```sh
pip install -U \
    -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 \
    wxPython
```

**Gooey**

[Gooey](https://github.com/chriskiehl/Gooey) based on `wxPython`
Turn (almost) any Python 2 or 3 Console Program into a GUI application with one line

*projects*:
[UGI_CBIR](/10.6.64.30/dhtsys-home/MSA Project Information/UGI_CBIR)



## Qt

**PyQt**
PyQt exists for a long time and is supported well ahead of PySide2 once.

**PySide2(Qt for Python)**
The Qt Company is investing into PySide2 officially with brighter future.


[PyQt vs Qt for Python(PySide2)](https://machinekoder.com/pyqt-vs-qt-for-python-pyside2-pyside/)


*projects*:
[richen-demo](ssh://git@10.6.64.19:10022/shavonling/richen-demo.git)-PySide2


## PySimpleGUI

`PySimpleGUI` wraps tkinter, Qt, WxPython and Remi so that you can get and interact with them in a more simple, friendly and common ways across the ports: `PySimpleGUI`.

`PySimpleGUI` is released on PyPI as 5 distinct packages.
1. PySimpleGUI - tkinter version
2. PySimpleGUI27 - tkinter version that runs on 2.7
3. PySimpleGUIWx - WxPython version
4. PySimpleGUIQt - PySided2 version
5. PySimpleGUIWeb - The web (Remi) version

