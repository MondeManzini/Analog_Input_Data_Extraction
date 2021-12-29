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

bit_res = 4096          # bit resolution
Vref = 3                # reference voltage

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
    crc = message[(message_len-3):(message_len+1)] # 112 - 3 = 109
    
    analog_values = analog_data[12:(message_len-4)]
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

    #def voltage_calc(channel_voltage):
    #    voltage_out = channel * bit_res_ratio
    #    return voltage_out

    #for i in analog_values:
    #    channel = int(message_len, 16)                      #Converts to decimal from base 16
    #    voltage_calc(i+3)
    #    print(voltage_out)

    message_list = message.split()
    print(f"New message as a list is {message_list}.")

    message_list.append(crc)
    print(f"New message with CRC is {message_list}.")

    print(f"The length of analog values is {len(analog_values)}.")

   # print(f"The output voltage of Channel {channel_no} is {voltage_out}.")

