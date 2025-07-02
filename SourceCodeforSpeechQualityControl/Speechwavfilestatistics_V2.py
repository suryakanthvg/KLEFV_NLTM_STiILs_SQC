# Speechwavfilestatistics_V2.py
#Usage: python3 Speechwavfilestatistics_V2.py /home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/InnovSenseTechnologies/Indic_Languages/Bengali/be_innov_r004_V1/AUDIO
#Usage: python3 Speechwavfilestatistics_V1.py /home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/Karya_Inc/Indic_Languages/Bengali/be_KARYA_r003_V1/AUDIO

import glob
import time
import os
from scipy.io.wavfile import read
import numpy as np
import sys


cls = 'clear'
wavfilepath = sys.argv[1]
Full_wavfilepath = wavfilepath + '/'

#wavfilepath = "/home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/Karya_Inc/Indic_Languages/Bengali/be_KARYA_r003_V1/AUDIO/"
#wavfilepath = "/home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/Karya_Inc/Indic_Languages/Assamese/as_KARYA_r003_V1/AUDIO/"

dir_namearray=Full_wavfilepath.split('/')
len_dir_namearray=len(dir_namearray)
#print(dir_namearray)
#print(len_dir_namearray)
release_name=dir_namearray[len_dir_namearray-3]
time.sleep(2)   

SpeechwavfileSignalLevelQualityDetails_file = release_name + '_SpeechwavfileSignalLevelQualityDetails_file.txt' 

#print(Speechwavfilestatistics_file)
#time.sleep(2)   

wavs = glob.glob(Full_wavfilepath+"*.wav")

total_duration_in_sec = 0
nClippingfiles = 0
nStereofiles = 0  



with open(SpeechwavfileSignalLevelQualityDetails_file, 'w') as f:
     for wavfile in wavs:
         os.system(cls)
         #base_dir_pair=os.path.split(wavfile)[0]
         #dirname=os.path.dirname(wavfile)
         filename=os.path.basename(wavfile)

         #filename_withoutextension=os.path.splitext(filename)[0]


         print('speech wavfile: ', filename)
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
            print('It is a stereo channel  speeh signal') 
            nStereofiles += 1  
            f.write("Stereo: ")
            f.write(filename)
            #f.write(wavfile)
            f.write('\n')
         else:
            print('The  speech signal is monochannel') 
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
               f.write("Clipped: ")
               f.write(filename)
               #f.write(wavfile)
               f.write('\n')
         time.sleep(2)   

     print('Summary of Observations')
     print('-----------------------')
     f.write( '\n' + 'Summary of Observations' + '\n')
     f.write( '--------------------------------' + '\n')
     formated_total_duration_in_sec="{:.3f}".format(total_duration_in_sec)
     print('Total duration of speech wavfiles (in seconds)', formated_total_duration_in_sec)
     f.write('Total duration of speech wavfiles (in seconds) ' + str(formated_total_duration_in_sec) + '\n')
     #f.write('\n')
     total_duration_in_min= total_duration_in_sec/60
     print('Total duration of speech wavfiles (in minutes) ', total_duration_in_min)
     f.write('Total duration of speech wavfiles (in minutes) ' + str(total_duration_in_min) + '\n')
#     f.write('\n')
     total_duration_in_hrs=total_duration_in_sec/(60*60)
     print('Total duration of speech wavfiles (in hours)', total_duration_in_hrs)
     f.write('Total duration of speech wavfiles (in hours) ' + str(total_duration_in_hrs) + '\n')
     #f.write('\n')

     nWavfiles = len(wavs)
     print('Number of wav files ', nWavfiles)
     f.write('Number of wav files ' +  str(nWavfiles) + '\n')
     #f.write('\n')

     print('Total number of Stereo wav files ', nStereofiles)
     f.write('Total number of Stereo wav files ' + str(nStereofiles) + '\n')
     #f.write('\n')
     percentStereofiles = 100*nStereofiles/nWavfiles
     print('Percentage of Stereo wav files ', percentStereofiles)
     f.write('Percentage of clipped wav files ' + str(percentStereofiles) + '\n')
     #f.write('\n')

     print('Total number of clipped wav files ', nClippingfiles)
     f.write('Total number of clipped wav files ' + str(nClippingfiles) + '\n')
     #f.write('\n')
     percentClippingfiles = 100*nClippingfiles/nWavfiles
     print('Percentage of clipped wav files ', percentClippingfiles)
     f.write('Percentage of clipped wav files ' + str(percentClippingfiles) + '\n')
     f.write('\n')

