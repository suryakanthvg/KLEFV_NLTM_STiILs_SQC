# Identifying the clipped wav files and declipping them
#https://engineering.papercup.com/posts/declipping/
# sox 140_NA_M_22_monologue_10384.wav -n stat

from scipy.io.wavfile import read
import numpy as np

wavfile = '1043_AH01OENC.wav'
#wavfile = '298_Mannarkkad_F_22_310_Mannarkkad_M_21_1.wav'
#wavfile = 'ma_CRESCT_C_r001_s001.wav'
#wavfile = 'MarathiSample3Recording.wav'
#wavfile = 'bn_IN_9440434_20221203_Right.wav'
#wavfile = '140_NA_M_22_monologue_10384.wav'

sample_rate, data = read(wavfile)

print('Sampling Frequency = ', sample_rate)
Number_of_samples = data.shape[0]
print('number of samples = ', Number_of_samples)
Speech_signal_duration = Number_of_samples/sample_rate
print('Speech signal duration (in seconds) = ', Speech_signal_duration)

Number_of_channels = len(data.shape)
print('Number of channels', Number_of_channels)

if (Number_of_channels > 1):
   print('It is expected to have monochannel speeh signal') 
   exit()
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
   exit()
else:   
   print('Speech signal has clipped')
   exit()


np_array = np.array(data, dtype=float)

nmax = max(np_array)
nmin = min(np_array)

clipped_segments = []
inside_clip = False
clip_start = 0
clip_end = 0

for i, sample in enumerate(np_array):
    if (sample <= nmin + 1) or (sample >= nmax - 1):  # sample equal to or extremely close to max or min
        if not inside_clip:
            inside_clip = True  # declare we are inside clipped segment
            clip_start = i  # this is the first clipped sample
        elif inside_clip:
             inside_clip = False  # not longer inside clipped segment
             clip_end = i-1  # previous sample is end of segment
             clipped_segment = (clip_start, clip_end)  # save segment as tuple
             clipped_segments.append(clipped_segment)  # store tuple in list of clipped segments

import matplotlib.pyplot as plt
new_array = np_array.copy()  # make copy of original np_array
from scipy import interpolate

for segment in clipped_segments:
    start = segment[0]
    end = segment[1]

    x_true = list(range(start - 5, start)) + list(range(end + 1, end + 6))
    y_true = [np_array[i] for i in x_true]

    interpolation_function = interpolate.interp1d(x_true, y_true, kind='cubic')  # function to predict missing values
    x_axis = list(range(start - 5, end + 6))  # indices to pass through function
    y_axis_new = [ float(int(i)) for i in interpolation_function(x_axis)]  # new sample values

    y_axis_old = [np_array[i] for i in x_axis]  # original values
    plt.plot(x_axis, y_axis_old,'bo-')
    plt.plot(x_axis, y_axis_new,'r--')
    plt.show()

for i, x in enumerate(x_axis):
        if start <= x <= end:
            new_array[x] = y_axis_new[i]

from scipy.io.wavfile import read, write

write("bad_file.wav", sample_rate, new_array)

new_max = max(abs(new_array))  # find new maximum
new_array = np.divide(new_array, new_max)  # divide by maximum
new_array = np.multiply(new_array, 32768.0)  # multiply by old maximum
new_array = new_array.astype('int16')  # 16-bit

write("new_wav.wav", sample_rate, new_array)


