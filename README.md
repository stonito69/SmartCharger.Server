# SmartCharger Server Application

This is simple TCP/IP server application featuring running on a raspberry unit installed in a local network.
It receives status from the Phone with a SmartCharger.Android application and switch smart outlet ON or OFF, depending of the battery level and defined parameters.
Language is Python, version 3.

![Raspberry setup](Screenshots/raspberry.jpg)
In this project I was using the FS1000A transmitter and corresponding receiver, but it should also work with other 433MHz transmitter/receiver modules that work in a similar fashion. These RF modules are very popular among the Arduino tinkerers and are used on a wide variety of applications that require wireless control.
![Outlet set](Screenshots/outlet_set.jpg)
Smart outlet set I bought for 24 EUR.
I used its remote controller to sniff the communication and to get the codes for switching on and off one outlet.
For sniffing I used Arduino Nano with a RF 433MHz receiver, and a code from this project https://github.com/Martin-Laclaustra/rc-switch/, getting the code busted took a second, for each button ON and OFF this smart outlet set uses two different codes interchangeably, but one for each will do.
![Outlet](Screenshots/outlet.jpg)
This particular outlet is configured by long pressing its button, it starts blinking, then pressing the button on the remote, configures it to the letter (A,B,C,D) you pressed. In the code I used sniffed codes for button A ON i OFF.
![Phone](Screenshots/phone.jpg)
This is how it looks in the end.
rpi-rf
======

Introduction
------------

Python module for sending and receiving 433/315MHz LPD/SRD signals with generic low-cost GPIO RF modules on a Raspberry Pi.

Protocol and base logic ported ported from `rc-switch`_.

Supported hardware
------------------

Most generic 433/315MHz capable modules (cost: ~2€) connected via GPIO to a Raspberry Pi.

.. figure:: http://i.imgur.com/vG89UP9.jpg
   :alt: 433modules

Compatibility
-------------

Generic RF outlets and most 433/315MHz switches (cost: ~15€/3pcs).

.. figure:: http://i.imgur.com/WVRxvWe.jpg
   :alt: rfoutlet


Chipsets:

* SC5262 / SC5272
* HX2262 / HX2272
* PT2262 / PT2272
* EV1527 / RT1527 / FP1527 / HS1527

For a full list of compatible devices and chipsets see the `rc-switch Wiki`_

Dependencies
------------

::

    RPi.GPIO

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
                  ____________
                 |        ____|__
                 |       |    |  |
                 |     01|  . x  |02
                 |       |  . x__|________       RX
                 |       |  . x__|______  |   ________
                 |       |  . .  |      | |  |        |
       TX        |   ____|__x .  |      | |__|VCC     |
     _______     |  |  __|__x .  |      |    |        |
    |       |    |  | |  |  x____|______|____|DATA    |
    |    GND|____|__| |  |  . .  |      |    |        |
    |       |    |    |  |  . .  |      |    |DATA    |
    |    VCC|____|    |  |  . .  |      |    |        |
    |       |         |  |  . .  |      |____|GND     |
    |   DATA|_________|  |  . .  |           |________|
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
       VCC > PIN 02 (5V)
      DATA > PIN 11 (GPIO17)

    RX:
       VCC > PIN 04 (5V)
      DATA > PIN 13 (GPIO27)
       GND > PIN 06 (GND)

Usage
-----

See `scripts`_ (`rpi-rf_send`_, `rpi-rf_receive`_) which are also shipped as cmdline tools.

Open Source
-----------

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues

.. _rc-switch: https://github.com/sui77/rc-switch
.. _rc-switch Wiki: https://github.com/sui77/rc-switch/wiki
.. _BSD Licence: http://www.linfo.org/bsdlicense.html
.. _GitHub: https://github.com/milaq/rpi-rf
.. _GitHub issues: https://github.com/milaq/rpi-rf/issues
.. _scripts: https://github.com/milaq/rpi-rf/blob/master/scripts
.. _rpi-rf_send: https://github.com/milaq/rpi-rf/blob/master/scripts/rpi-rf_send
.. _rpi-rf_receive: https://github.com/milaq/rpi-rf/blob/master/scripts/rpi-rf_receive


