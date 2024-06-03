import matplotlib.pyplot as plt
import numpy as np
import copy
import math import ceil

class Audio_Item():
    def __init__(self, file_name:str) -> None:
        file_obj = open(file_name, ,mode ='rb')
        file_data = file_obj.read()
        file_obj.close()

        #file size
        file_size_inbytes = file_data[4:8] 
        file_size = int.from_bytes(file_size_inbytes, byteorder = "little")

        chan_num_inbyte = data[22:24]
        chan_num = int.from_bytes(chan_num_inbyte, byteorder = "little")

        aud_data_size_inbytes = data[40:44]
        aud_data_size = int.from_bytes(aud_data_size_inbytes, byteorder = "little")   


aud_data_size_inbytes = data[40:44]
aud_data_size = int.from_bytes(aud_data_size_inbytes, byteorder = "little")

sample_rate_inbytes = data [24:28]
sample_rate = int.from_bytes(sample_rate_inbytes, byteorder = "little")

aud_amps = []

for i in range (0, aud_data_size,2):
    amp_inbytes = data[44+i:i+2+44]
    amp = int.from_bytes(amp_inbytes, byteorder = "little", signed = True)
    aud_amps.append(amp)

time = np.linspace(0,len(aud_amps)/sample_rate,len(aud_amps))
freq = np.linspace()

spectre = np.fft.fft(aud_amps)
abd_spectre = abs(spectre)

plt.plot(time,aud_amps)
plt.show()

