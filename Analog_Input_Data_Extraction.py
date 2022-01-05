""" 
Author: Monde Manzini
Affiliation: Test Engineer
Description: Purpose of the script is to tests whether analog values are 
    within specs.
Date: 08-12-2021
"""
import csv
import pandas as pd
import Generate_Test_Script
from Generate_Test_Script import analog_values
# constants
bit_res = 4096          # bit resolution
Vref = 3                # reference voltage
channel_no = 0          # channel number   
# Bit resolution ratio
bit_res_ratio = Vref / bit_res

# Read generated file and calculate voltages
with open("./analog_input_generated.txt", "rt") as analog_input_raw:
    analog_data = analog_input_raw.read()
    message_len = (analog_data[6:8])
    message_len = int(message_len, 16)                      #Converts to decimal from base 16
    message = analog_data[0:(message_len+1)]
    header1 = message[0:2]
    header2 = message[2:4]
    header3 = message[4:6]
    mode = message[8:10]
    analog_card_number = message[10:12]
    crc = message[(message_len-4):(message_len+1)] # 112 - 3 = 109
    #analog_values = analog_data[12:(message_len-4)]
    print(analog_values)

    #check headers
    #   check hearder 1
    if header1 == "A5":
        print(f"Header 1 is {header1}.\n")
    else:
        print(f"Header 1 is not A5.")

    if header2 == "5A":
        print(f"Header 2 is {header2}.\n")
    else:
        print(f"Header 2 is not 5A.")

    if header3 == "7E":
        print(f"Header 3 is {header3}.\n")
    else:
        print(f"Header 3 is not 7E.")

    # display serial string values
    print(f"The mode is {mode}.\n")
    print(f"The message length in decimal is {message_len}.")
    print(f"The Analog Card number is {analog_card_number}.")
    print(f"The analog values are {analog_values}.")
    print(f"The CRC is {crc}.")
    print(f"The message is {message}.")

    voltage_out = []
    channel_val = []
    
    # Convert voltage from hex to decimal format
    # and calculate output voltage 
    def voltage_calc(channel_no, channel_voltage):
        voltage_out_dec = int(channel_voltage, 16)
        voltage_out = voltage_out_dec * bit_res_ratio
        return print(f"The voltage output for Channel {channel_no} is {voltage_out}.")    

    # Extract each hex channel value to prepare for calculation

    for analog_value in analog_values:
        channel_no = channel_no+1
        voltage_calc(channel_no,analog_value)

    #for i in analog_values:
    #    channel_val = analog_values[(5*i):(i*5+4)]
    #    print(f"The output voltage for channel {voltage_calc(channel_val)}.")

    #for i in analog_values[0:4]:
    #    channel_no = i
    #    channel_val = analog_values[0:4]
    #    print(f"Channel value is {channel_val}")
    #    channel_val = channel_val.lstrip("['")
    #    channel_val = channel_val.rstrip("']")
    #    channel_val = channel_val.replace("'", "")
    #    channel_val = channel_val.replace(",", "")
    #    channel_val = channel_val.translate({ord(' '): None})
    #    voltage_calc(channel_val)
    #    print(f"The output voltage for channel {channel_no} is {voltage_out}.")

    #message_list = message.split()
    #print(f"New message as a list is {message_list}.")

    #print(f"The length of analog values is {len(analog_values)}.")

   # print(f"The output voltage of Channel {channel_no} is {voltage_out}.")

