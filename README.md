---
name: Smartcharger.Server - Server part of a Smart Charger project
description: Smartcharger is a project designed to provide smart charging capability to any Android phone, using smart outlet, Raspberry Pi with a RF 433MHz transmitter and receiver (for sniffing the codes of specific outlets). 
Code here is to run as a service on a Raspberry Pi with properly connected RF 433 MHZ transmitter 
page_type: sample
languages:
- python
products:
- raspberry
---
# SmartCharger Server Application

This is simple TCP/IP server application featuring running on a raspberry unit in a local network.
It receives status from the Phone with a SmartCharger.Android application and switch smart outlet ON or OFF, depending of the battery level and defined parameters.

![Raspberry setup](Screenshots/raspberry.jpg)
![Outlet set](Screenshots/outlet_set.jpg)
![Outlet](Screenshots/outlet.jpg)
![Phone](Screenshots/phone.jpg)


