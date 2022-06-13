# SmartCharger Server 

This is simple TCP/IP server application featuring running on a raspberry unit installed in a local network.
It receives status from the Phone with a SmartCharger.Android application and switch smart outlet ON or OFF, depending of the battery level and defined parameters.
Language is Python, version 3.

![Raspberry setup](Screenshots/raspberry.jpg)
In this project I was using the FS1000A transmitter and corresponding receiver, but it should also work with other 433MHz transmitter/receiver modules that work in a similar fashion. These RF modules are very popular among the Arduino tinkerers and are used on a wide variety of applications that require wireless control.

Introduction
------------

Python software hosting TCP/IP server to allow Android phone to send its battery state information and sending 433Mhz LPD/SRD signals with generic low-cost GPIO RF modules on a Raspberry Pi to switch power outlet On and Off, and thus charging the phone only when desired.
It also has Ping Timeout function, when Phone doesn't send statuses it will keep the charger On, to prevent it draining battery completely.
Also it has a Waiting for network function, which is used in automatic boot to wait for the ping to local router to be successful before starting TCP/IP server.

Supported hardware
------------------

Most generic 433/315MHz capable modules (cost: ~2€) connected via GPIO to a Raspberry Pi.

![Raspberry setup](http://i.imgur.com/vG89UP9.jpg)

Installation
------------

On your Raspberry Pi, install the *rpi_rf* module via pip.

Python 3::

    # apt-get install python3-pip
    # pip3 install rpi-rf

Wiring diagram (example)
------------------------

Raspberry Pi 1/2(B+)::

                       RPI GPIO HEADER
                 
                          _______
                         |       |
                       01|  . .  |02
                  _______|__._x  |
                 |   ____|__._x  |
                 |  |    |  . .  |
       TX        |  |  __|__._x  | 
     _______     |  | |  |  . .  | 
    |       |    |  | |  |  . .  |
    |    GND|____|__| |  |  . .  | 
    |       |    |    |  |  . .  | 
    |    VCC|____|    |  |  . .  | 
    |       |         |  |  . .  | 
    |   DATA|_________|  |  . .  | 
    |_______|            |  . .  |
                         |  . .  |
                         |  . .  |
                         |  . .  |
                         |  . .  |
                         |  . .  |
                         |  . .  |
                       39|  . .  |40
                         |_______|

    TX:
       GND > PIN 09 (GND)
       VCC > PIN 04 (5V)
      DATA > PIN 10 (GPIO15)
   
Usage
-----

Run script server.py and put it in autostart after boot.

Open Source
-----------

* The code is licensed under the `BSD Licence`
* The project source code is hosted on `GitHub`
* Please use `GitHub issues`to submit bugs and report issues
