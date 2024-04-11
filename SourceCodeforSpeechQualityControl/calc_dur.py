from pydub import AudioSegment
import glob
import os
import json

ABS1 = ""
# ABS1 = "/Users/adiyadaval/Downloads/dual_ready_complete/"
wavs = glob.glob(ABS1+"*.wav")

total_duration = 0
for wav in wavs:
    audio = AudioSegment.from_file(wav)
    total_duration += audio.duration_seconds

print(total_duration)

