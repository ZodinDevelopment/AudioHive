import os
import pyaudio 
import wave 
import sys
import time



CHUNK = 1024

DIR = os.getcwd() 

AUDIO_DIR = os.path.join(DIR, "audio/") 

AUDIO_FILES = os.listdir(AUDIO_DIR)


def main():
    
    if len(AUDIO_FILES) <=0:
        print('No audio files found.')
        sys.exit()


    #Use wave to open the file in binary formar 
    AUDIO_F = os.path.join(AUDIO_DIR, AUDIO_FILES[0])

    print('Opening wave file in readonly mode as binary data.')
    time.sleep(0.8)


    #Instantiate pyaaudio (1)
    p = pyaudio.PyAudio()
    
    #Open Stream(2)
    print("Opening the audio stream in output mode.")
    time.sleep(0.6)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    print('Now reading data in chunks of side {} and writing each to the output stream.'.format(str(CHUNK)))
    time.sleep(0.5)

    data = wf.readframes(CHUNK)

    #play data
    print('Playback is beginning')
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)


    # stop stream (4)
    os.system("clear")
    print('Playback finished, stopping and closing the stream and terminating our PyAudio instance.')
    time.sleep(1)

    stream.stop_stream()
    stream.close()


    p.terminate() 

if __name__ == "__main__":
    main()





    
    
    

