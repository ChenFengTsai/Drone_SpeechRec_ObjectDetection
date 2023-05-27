# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 23:42:45 2023

@author: sb5
"""

from djitellopy import Tello
import configparser
import sys
import os

config = configparser.ConfigParser()
cd = sys.path[0]
dir = os.path.join(os.path.dirname(cd), 'config.ini')
config.read(dir)
wifi_name = config.get('wifi', 'wifi_name')
wifi_password = config.get('wifi', 'wifi_password')
    
# Connect to the drone
drone = Tello()
drone.connect()

# Connect to your home WiFi
drone.connect_to_wifi(wifi_name, wifi_password)

# reboot the drone