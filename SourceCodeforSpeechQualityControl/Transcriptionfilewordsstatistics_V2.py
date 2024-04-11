#Usage:  python3 Transcriptionfilewordsstatistics_V2.py /home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/InnovSenseTechnologies/Indic_Languages/Bengali/be_innov_r004_V1/TRANSCRIPTION/be_innov_C_r004_s001.json

#Usage: python3 Transcriptionfilewordsstatistics_V1.py /home/svg/NLTM_SQC/SpeechCorpora/IITMSTiIL/IITM_STiIL_Phase1/Karya_Inc/Indic_Languages/Bengali/be_KARYA_r003_V1/TRANSCRIPTION/be_KARYA_C_r003_s001.json


# Transcription file words statistics 
# Trnasciption is read from a json file
import json
import sys



def Transcriptionfilewordsstatistics(transcriptionFilename):
    # Create a file object using open
    # function and pass transcriptionFilename as parameter.
    transcriptionFilePointer = open(transcriptionFilename, 'r')
    # Read file contents as string and convert to lowercase.
    transcriptionFile = transcriptionFilePointer.read().lower()
    wordsTranscriptionFile = transcriptionFile.split()
    nTranscriptionwords = len(wordsTranscriptionFile)
    print('The number of transcription words')
    print(nTranscriptionwords)
    # Creating a dictionary for finding transcription statistics.
    words_dict = {}
    for i in wordsTranscriptionFile:
        if i in words_dict:
            words_dict[i] += 1
        else:
            words_dict[i] = 1
    count = 0
    # Traverse the dictionary and increment
    # the counter for every unique word.
    for i in words_dict:
        if words_dict[i] == 1:
            count += 1
    transcriptionFilePointer.close()
    print('The words and their frequency of the transcription')
    print(words_dict)

    print('The Number of distinct Words')
    nDistinctwords = len(words_dict)
    print(nDistinctwords)

    nForeignwords = 0
    print('Foreign words are')
    for i in words_dict.keys():
        if i[0] == '<' or (i[0] >='a' and i[0] <='z') :
            print(i)
            nForeignwords += 1

    print('The number of foreign words are')
    print(nForeignwords)

    nMonolingualwords = nTranscriptionwords - nForeignwords
    print('Number of Monolingual words')
    print(nMonolingualwords)

    print('Transcription file words statistics')
    print('===================================')
    print('Input file name: ', inputTranscriptionfile)

    print('Number of transcription words: ', nTranscriptionwords)

    print('Number of Distinct Words:', nDistinctwords)

    print('Number of Monolingual words:', nMonolingualwords)

    print('Number of foreign words are: ', nForeignwords)

    Percentage_of_foreign_words = 100*nForeignwords/nTranscriptionwords

    formated_Percentage_of_foreign_words = "{:.3f}".format(Percentage_of_foreign_words)

    print('Percentage of foreign words are: ', formated_Percentage_of_foreign_words)

    print('Number of Unique words  in the file are:', count)

    return None  # Return nothing.


# Main program starts here

# Opening JSON file
inputTranscriptionfile= sys.argv[1]
f = open(inputTranscriptionfile)
#f = open('hi_IN_9845637_20230112_Left.json')
#f = open('bn_IN_9440434_20221203_Right.json')

# returns JSON object as a dictionary
data = json.load(f)

segmentType_count = 0
segmentType_speech_count = 0
segmentType_nonSpeech_count = 0
Duration_of_nonSpeech_segments = 0
Duration_of_speech_wavfile = 0
speakerSeqId1count = 0
speakerSeqId2count = 0
speakerSeqId1duration = 0
speakerSeqId2duration = 0
mindurspeechsegment = data["callDuration"]
maxdurspeechsegment = 0
mindurspeechsegmentId = 0
maxdurspeechsegmentId = 0

with open("transcriptionfile.txt", "w") as file:
    # Iterating through the json list
    for i in data['segments']:
        segmentType_count += 1
        print(i["segmentId"])
        Duration_of_speech_wavfile = Duration_of_speech_wavfile + (i["end"] - i["start"])
        if (i['segmentType'] == 'speech'):
        #if (i["transcription"] != None):
        #if (i['segmentType'] == 'speech'):
        #if (i['segmentType'] != "overlap"):
           file.write(i["transcription"])
           file.write('\n')
           segmentType_speech_count += 1
           curspeechsegduration = i["end"] - i["start"]
           if (curspeechsegduration > maxdurspeechsegment):
               maxdurspeechsegment = curspeechsegduration
               maxdurspeechsegmentId = i["segmentId"]
           if (curspeechsegduration < mindurspeechsegment):
               mindurspeechsegment = curspeechsegduration
               mindurspeechsegmentId = i["segmentId"]
           if (i["speakerSeqId"] == 1):
               speakerSeqId1count += 1
               speakerSeqId1duration = speakerSeqId1duration + curspeechsegduration
           else: 
               if (i["speakerSeqId"] == 2):
                  speakerSeqId2count += 1
                  speakerSeqId2duration = speakerSeqId2duration + curspeechsegduration
        else:
            if (i['segmentType'] == 'nonSpeech'):
                segmentType_nonSpeech_count += 1
                curnonSpeechsegduration = i["end"] - i["start"]
                Duration_of_nonSpeech_segments = Duration_of_nonSpeech_segments + curnonSpeechsegduration

f.close()

Transcriptionfilewordsstatistics('transcriptionfile.txt')


print('===================================')
print('Speaker(s) participation  statistics')
print("inputTranscriptionfile", inputTranscriptionfile)
#print('\n')
print('Number of segments', segmentType_count)
print('Number of nonSpeech segments', segmentType_nonSpeech_count)
print('Number of speech segments', segmentType_speech_count)

num_segmentType_speech_nonSpeech_count = segmentType_speech_count + segmentType_nonSpeech_count

if (segmentType_count == num_segmentType_speech_nonSpeech_count):
   print('Number of speech and nonSpeech segments MATCHES with number of  segments')
else:
   print('Number of speech and nonSpeech segments DOES NOT MATCHES with number of  segments')
    
print('Number of segments in which speakerSeqId1 has participated', speakerSeqId1count)
print('Duration (in seconds) of speakerSeqId1 has participated', speakerSeqId1duration)

print('Number of segments in which speakerSeqId2 has participated', speakerSeqId2count)
print('Duration (in seconds) of speakerSeqId2 has participated', speakerSeqId2duration)

num_speakerSeqId1_speakerSeqId2_segments = speakerSeqId1count + speakerSeqId2count

if (segmentType_speech_count == num_speakerSeqId1_speakerSeqId2_segments):
   print('Number of speakerSeqId1 and speakerSeqId2 segments  MATCHES with speech segments')
else:   
   print('Number of speakerSeqId1 and speakerSeqId2 segments  DOES NOT MATCHES with speech segments')

Duration_of_speech_segments = speakerSeqId1duration + speakerSeqId2duration
print('Duration (in seconds) of speech segments', Duration_of_speech_segments)
print('Duration (in seconds) of nonSpeech segments', Duration_of_nonSpeech_segments)
Duration_of_speech_nonSpeechsegments = Duration_of_speech_segments + Duration_of_nonSpeech_segments
print('Duration (in seconds) of speech_nonSpeechsegments', Duration_of_speech_nonSpeechsegments)
print('Duration (in seconds) of speech wavfile by computation ', Duration_of_speech_wavfile)


if (Duration_of_speech_nonSpeechsegments == Duration_of_speech_wavfile):
   print('Duration (in seconds) of speech_nonSpeechsegments MATCHES with speech wavfile by computation') 
else:   
   print('Duration (in seconds)) of speech_nonSpeechsegments DOES NOT MATCHES with speech wavfile by computation') 

print('Duration (in seconds) of speech wavfile from transcription file header (callDuration)', data["callDuration"])

if (Duration_of_speech_wavfile == data["callDuration"]):
    print('Duration of speech wavfile by computation MATCHES with the transcription file')
else:
    print('Duration of speech wavfile by computation DOES NOT MATCHES with the transcription file')

print('Minimum Duration (in seconds) of speech segment', mindurspeechsegment)
print('Minimum Duration  speech segmentId', mindurspeechsegmentId)
print('Maximum Duration (in seconds) of speech segment', maxdurspeechsegment)
print('Maximum Duration speech segmentId', maxdurspeechsegmentId)





 



