import csv
import pandas as pd

bit_res = 4096          # bit resolution
Vref = 3                # reference voltage

# Bit resolution ratio
bit_res_ratio = Vref / bit_res
# Script tests whether analog values are within
# specs
analog_values_len = 48      # Number of analog input channels
message_len = 104      # Number of analog input channels

analog_values = []
#message = []
message_len_hex = []

# Hardcoded values
var_input = "0AC0"
header1 = ["A5"]
header2 = ["5A"]
header3 = ["7E"]
mode = ["80"]
crc = ["BFA2"]
analog_card_number = ["30"]

# Manipulate the analog values length
analog_values_len_hex = hex(analog_values_len)
analog_values_len_hex = list(analog_values_len_hex)
analog_values_len_hex.pop(0)
analog_values_len_hex.pop(0)
analog_values_len_hex = [analog_values_len_hex[0] + analog_values_len_hex[1]]

print(analog_values_len_hex)
print(type(analog_values_len_hex))

# Generate 48 analog values
for j in range(0,analog_values_len):
    analog_values.append(var_input)

print(analog_values)

# Generate a text file with the serial message containing
# analog input vlaues
with open("./analog_input_generated.txt", "wt") as analog_input_gen: # f.write(text1)
    # construct message
    concat_message = header1 + header2 + header3 + mode + message_len_hex \
    + analog_card_number + analog_values + crc
    for i in range(0,int(message_len/2)):
        #concat_message = [concat_message[0] + concat_message[1] + concat_message[2] ]
        concat_message.join([concat_message[i]])
    print(concat_message)

    message = header1 + header2 + header3 + mode + analog_card_number \
        + analog_values_len_hex + analog_values + crc
    analog_input_gen.write(str(message))
    #print(analog_input_gen)

'''
# Read generated file and calculate voltages
with open("./analog_input_constructed.txt", "rt") as analog_input_raw:
    analog_data = analog_input_raw.read()
    message_len = (analog_data[6:8])
    message_len = int(message_len, 16)                      #Converts to decimal from base 16
    message = analog_data[0:(message_len-1)]
    header1 = message[0:2]
    header2 = message[2:4]
    header3 = message[4:6]
    mode = message[8:10]
    analog_card_number = message[10:12]
    crc = message[(message_len-3):(message_len+1)] # 112 - 3 = 109
    
    analog_values = analog_data[10:(message_len-4)]
    if header1 == "A5":
        print(f"Header 1 is {header1}.")
    else:
        print(f"Header 1 is not A5.")

    if header2 == "5A":
        print(f"Header 2 is {header2}.")
    else:
        print(f"Header 2 is not 5A.")

    if header3 == "7E":
        print(f"Header 3 is {header3}.")
    else:
        print(f"Header 3 is not 7E.")

    # display serial string values
    print(f"The mode is {mode}.")
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
'''
