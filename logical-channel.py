# -*- coding: utf-8 -*-
"""
Created on Mon Feb 2 20:39:25 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Ad Hoc Net ")
print(Fore.GREEN+font)


import os
import subprocess

def get_user_input():
    """Prompts the user for network configuration details."""
    ssid = input("Enter the SSID (Network Name):")
    ip_address = input("Enter the IP address:")
    netmask = input("Enter the network netmask (e.g., 255.255.255.0):")
    gateway = input("Enter the gateway IP address (optional, press Enter to skip):")
    channel = input("Enter the channel number (1-11 for 2.4GHz, 36-165 for 5GHz):")
    
    # Make sure that the channel is valid for the selected frequency
    return ssid, ip_address, netmask, gateway, channel

def configure_ad_hoc_network(ssid, ip_address, netmask, gateway, channel):
    """Sets up an ad-hoc network using user input."""
    
    # Commands to configure the ad-hoc network
    interface = 'wlan0'  # You may need to change this based on the OS and hardware
    
    # Disable Wi-Fi before configuring
    os.system(f"sudo ifconfig {interface} down")
    
    # Set up ad-hoc mode
    os.system(f"sudo iw dev {interface} set type ibss")
    
    # Configure SSID
    os.system(f"sudo iw dev {interface} ibss join {ssid} {channel}")
    
    # Assign IP address
    os.system(f"sudo ifconfig {interface} {ip_address} netmask {netmask}")
    
    if gateway:
        # Set up the gateway if provided
        os.system(f"sudo route add default gw {gateway} {interface}")
    
    # Enable the network interface
    os.system(f"sudo ifconfig {interface} up")
    
    print(f"Ad-hoc network '{ssid}' configured on channel {channel} with IP {ip_address}.")

def main():
    print("Welcome to the Ad-hoc Network Configuration Tool!")
    
    # Get user input for network details
    ssid, ip_address, netmask, gateway, channel = get_user_input()
    
    # Configure the ad-hoc network
    configure_ad_hoc_network(ssid, ip_address, netmask, gateway, channel)
    
    print("Ad-hoc network setup complete.")

if __name__ == "__main__":
    main()
