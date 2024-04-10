# Speechwavfilestatistics_V1.py
import glob
import time
import os
from scipy.io.wavfile import read
import numpy as np

#cls = 'clear'
wavfilepath = "C:/Users/Darksoul/Desktop/WavFiles/"

wavs = glob.glob(os.path.join(wavfilepath)+"*.wav")

total_duration_in_sec = 0
nClippingfiles = 0

with open('Speechwavfilestatistics.txt', 'w') as f:
     for wavfile in wavs:
#         os.system(cls)
         print('speech wavfile: ', wavfile)
         sample_rate, data = read(wavfile)
         print('Sampling Frequency = ', sample_rate)
         Number_of_samples = data.shape[0]
         print('number of samples = ', Number_of_samples)
         Speech_signal_duration = Number_of_samples/sample_rate
         formatted_Speech_signal_duration="{:.3f}".format(Speech_signal_duration)
         print('Speech signal duration (in seconds) = ', formatted_Speech_signal_duration)
         print('Speech signal duration (in minutes) = ', Speech_signal_duration/60)
         total_duration_in_sec += Speech_signal_duration
         Number_of_channels = len(data.shape)
         print('Number of channels', Number_of_channels)
         if (Number_of_channels > 1):
            print('It is expected to have monochannel speeh signal') 
         else:
            print('The  speeh signal is monochannel') 

         nmax = max(data)
         nmin = min(data)
         print ('Maximum amplitude value = ',  nmax)
         print ('Minimum amplitude value = ',  nmin)
         maximumlimit = 2**15-1
         minmumlimit = -(2**15)
         if (nmax < maximumlimit) and (nmin > minmumlimit):
            print('Speech signal has not clipped anywhere')
         else:   
            print('Speech signal has clipped')
            nClippingfiles += 1  
            f.write(wavfile)
            f.write('\n')
         #time.sleep(2)   

formated_total_duration_in_sec="{:.3f}".format(total_duration_in_sec)
print('Total duration of speech wavfiles (in seconds)', formated_total_duration_in_sec)
#f.write('Total duration of speech wavfiles (in seconds)' + total_duration_in_sec)
#f.write('\n')
print('Total duration of speech wavfiles (in minutes)', total_duration_in_sec/60)
#f.write('Total duration of speech wavfiles (in minutes)' + total_duration_in_sec/60)
#f.write('\n')
print('Total duration of speech wavfiles (in hours)', total_duration_in_sec/(60*60))
#f.write('Total duration of speech wavfiles (in hours)' + total_duration_in_sec/(60*60))
#f.write('\n')
nWavfiles = len(wavs)
print('Number of wav files ', nWavfiles)
#f.write('Number of wav files ' + nWavfiles)
#f.write('\n')
print('Total number of clipped wav files ', nClippingfiles)
#f.write('Total number of clipped wav files ' + nClippingfiles)
#f.write('\n')
percentClippingfiles = 100*nClippingfiles/nWavfiles
print('Percentage of clipped wav files ', percentClippingfiles)
#f.write('Percentage of clipped wav files ' + percentClippingfiles + '\n')
#f.write('\n')





