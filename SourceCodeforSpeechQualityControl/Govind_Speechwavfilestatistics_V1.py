# Speechwavfilestatistics_V1.py
import glob
import time
import os
from scipy.io.wavfile import read
import numpy as np

cls = 'clear'
wavfilepath = "/home/svg/NLTM_SQC/PythonPractice/GovindD/"
#wavfilepath = "/home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/Mediscribe_Shaip/Indic_Languages/Tamil/ta_IN/16khz/ta_SHA1P_17022023_roo1/Audio/"
#wavfilepath = "/home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/Mediscribe_Shaip/Indic_Languages/Punjabi/pa_IN/16khz/pa_SHA1P_17022023_roo1/Audio/"
#wavfilepath = "/home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/Mediscribe_Shaip/Indic_Languages/Bengali/be_IN/16Khz/be_SHA1P_17082023_roo1/Audio/"
#wavfilepath = "/home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/CrescendoTranscriptions/Indic_Languages/Approval_Batch_16022023/wav/"
wavs = glob.glob(wavfilepath+"*.wav")

#total_duration_in_sec = 0
nClippingfiles = 0
maximumlimit = 2**15-1
minmumlimit = -(2**15)

with open('Speechwavfilestatistics.txt', 'w') as f:
     for wavfile in wavs:
         os.system(cls)
#         print('speech wavfile: ', wavfile)
         sample_rate, data = read(wavfile)
#         print('Sampling Frequency = ', sample_rate)
#         Number_of_samples = data.shape[0]
#         print('number of samples = ', Number_of_samples)
#         Speech_signal_duration = Number_of_samples/sample_rate
#         print('Speech signal duration (in seconds) = ', Speech_signal_duration)
#         print('Speech signal duration (in minutes) = ', Speech_signal_duration/60)
#         total_duration_in_sec += Speech_signal_duration
#         Number_of_channels = len(data.shape)
#         print('Number of channels', Number_of_channels)
#         if (Number_of_channels > 1):
#            print('It is expected to have monochannel speeh signal') 
#         else:
#            print('The  speeh signal is monochannel') 

         nmax = max(data)
         nmin = min(data)
#         print ('Maximum amplitude value = ',  nmax)
#         print ('Minimum amplitude value = ',  nmin)
         if (nmax < maximumlimit) and (nmin > minmumlimit):
            print('Speech signal has not clipped anywhere')
            print('speech wavfile: ', wavfile)
            f.write(wavfile)
            f.write('\n')
         else:   
#            print('Speech signal has clipped')
            nClippingfiles += 1  
#         time.sleep(1)   

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

