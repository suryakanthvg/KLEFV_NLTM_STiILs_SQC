# Python program to read
import time
from pydub import AudioSegment
from pydub.playback import play

# Import an audio file
# Format parameter only
# for readability
wav_file = AudioSegment.from_file(file = "bn_IN_9440434_20221203_Right.wav", format = "wav")

# Play the audio segment
#play(wav_file)

# Opening JSON file
f = open('bn_IN_9440434_20221203_Right.json')
# returns JSON object as
# a dictionary
data = json.load(f)
# Iterating through the json
# list
for i in data['segments']:
    print(i)
    time.sleep(2)

    print(i["transcription"])
    print(i["start"])
    print(i["end"])
    print("")
    start_wav=i["start"]
    end_wav=i["end"]
    start_wav_ms=int(start_wav * 1000)
    end_wav_ms=int(end_wav * 1000)
    print(start_wav_ms)
    print(end_wav_ms)
    print("")
    segment_duration=end_wav-start_wav
    formated_segment_duration="{:.3f}".format(segment_duration)
    print(formated_segment_duration)
    time.sleep(4)
    wav_segment=wav_file[start_wav_ms:end_wav_ms]
    play(wav_segment)

# Closing file
f.close()

