Radiotech
=========
This repository contains all the demo source code required to perform labs. 5 labs are planned.
List of labs:
--------------
1. [Analog modulation (Amplitude modulation as an example)]
2. [Digital modulation (Amplitude shift keying (ASK) as an example)]
3. Coding
4. Something else

Requirements
------------
To assume the correct work you have to download Matplotlib (http://matplotlib.org/) and Numpy (http://www.numpy.org/) libraries. Instructions are following:

Windows

If you're running Windows x32 you have to install following packages:

1. python-2.7.6 http://www.python.org/download/releases/2.7.6/
2. matplotlib-1.3.1.win32-py2.7 http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
3. numpy-1.8.0-win32-superpack-python2.7    http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
4. pyparsing-2.0.1.win32-py2.7 http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyparsing
5. python-dateutil-2.2.win32-py2.7 http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-dateutil
6. scipy-0.13.3.win32-py2.7 http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
7. six-1.5.2.win32-py2.7 http://www.lfd.uci.edu/~gohlke/pythonlibs/#six

Other versions of these packages is avalible here: http://www.lfd.uci.edu/~gohlke/pythonlibs/ (this site may be down sometimes)

Linux

If you're running Ubuntu/Debian you may install packages from repository:

1. ```sudo apt-get install python```
2. ```sudo apt-get install python-numpy```
3. ```sudo apt-get install python-matplotlib```

OS X

In order to get the whole package of python libraries updates (e.g. numpy is in OS X as a base though getting newer version is a safe play for backward compatibility issues) you may consider reading this guide:

http://www.thisisthegreenroom.com/2011/installing-python-numpy-scipy-matplotlib-and-ipython-on-lion/

Even though it's quite outdated and based on OS X 10.7 Lion this guide is still reliable up to Mavericks. Ruby and XCode Command Line Tools must be obtained beforehand, look for the latter in Mac App Store; ruby is preinstalled and may be outdated too. We won't use any virtualization here so installing virtualenv isn`t necessary, also one may skip IPython.


Other
---------
There are two branches. Master branch contains excersices, Test branch is additional (and also temprary non-existant for sake of laziness). There you can find additional functions, which won't be used in this course.


Pull request information
---------
How to name the files:
first_name_last_name_type_of_modulation.py

You have to add source file into folder of your group

[Analog modulation (Amplitude modulation as an example)]: https://github.com/dep403mai/Radiotech/tree/master/Lab1
[Digital modulation (Amplitude shift keying (ASK) as an example)]: https://github.com/dep403mai/Radiotech/tree/master/Lab2
