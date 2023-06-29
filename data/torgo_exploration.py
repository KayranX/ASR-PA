import argparse
import os
import time
from audioplayer import AudioPlayer

# ToDo: Write tests
# ToDo: Implement visualizers for: raw audio, FFT, MFCC
# the torgo dataset can be downloaded here: http://www.cs.toronto.edu/~complingweb/data/TORGO/torgo.html

"""
The folder structure should look like this:
-> torgo_exploration.py
-> torgo
   -> F
   -> ...
   -> MC
      -> MC01
      -> ...
      -> MC04
         -> Session1
         -> Session2
            -> ...
            -> wav_arrayMic
               -> ...
               -> 0670.wav
               -> ...
"""

# read the corresponding files to play audio
parser = argparse.ArgumentParser(
    prog='Torgo Exploration',
    description='Explore certain samples from the TORGO dataset'
)

# ToDo: For demonstration purposes, use the default values
parser.add_argument(
    '--speaker',
    type=str,
    default='F01',
    help='Speaker selection from (F01, F03, F04, FC01, FC02, FC03, M01, M02, M03, M04, M05, MC01, MC02, MC03, MC04).'
)

parser.add_argument(
    '--session',
    type=int,
    default='1',
    help='Session selection from (1, 2, 3). Note: Not all sessions exist for every speaker.'
)

parser.add_argument(
    '--rec_number',
    type=int,
    default='1',
    help='Audio-file selection from the list. Note: The number of available audio files differs.'
)

parser.add_argument(
    '--mic',
    type=str,
    default='array',
    help='Microphone selection from (array, head). Note: One of the microphones might be sometimes unavailable.'
)


# ToDo: Can be shortened once the assert_inputs_basic is adapted to check everything beforehand
# play the desired audio-sample and show the text
def play_audio(arguments: argparse.Namespace):
    speaker_group = arguments.speaker[:1] if arguments.speaker[1].isnumeric() else arguments.speaker[:2]
    # the session name does not fit for all cases yet
    session_name = 'Session' + str(arguments.session)
    microphone_name = 'wav_' + arguments.mic + 'Mic'
    recording_name = str(arguments.rec_number).zfill(4) + '.wav'
    prompt_name = str(arguments.rec_number).zfill(4) + '.txt'

    # create the corresponding prompt-path and print the prompt
    prompt_path = os.path.join(
        'torgo', speaker_group, arguments.speaker, session_name, 'prompts', prompt_name
    ).replace('\\', '/')
    assert os.path.exists(prompt_path), 'The desired path does not exist. Please use other parameters!'
    prompt_file = open(prompt_path, 'r')
    prompt = prompt_file.readline()
    prompt_file.close()
    print(f'This prompt was given and executed: {prompt}')
    time.sleep(3)

    # create the corresponding audio-file-path and play the audio
    audio_path = os.path.join(
        'torgo', speaker_group, arguments.speaker, session_name, microphone_name, recording_name
    ).replace('\\', '/')
    assert os.path.exists(audio_path), 'The desired path does not exist. Please use other parameters!'
    AudioPlayer(audio_path).play(block=True)


# ToDo: Expand this basic function to better verify the given arguments
# verify that the inputs fit the requirements
# does not guarantee that the requested file even exists
def assert_inputs_basic(arguments: argparse.Namespace):
    assert arguments.speaker in (
        'F01', 'F03', 'F04', 'FC01', 'FC02', 'FC03', 'M01', 'M02', 'M03', 'M04', 'M05', 'MC01', 'MC02', 'MC03', 'MC04'
    ), 'The requested speaker is not available. Check your inputs!'
    assert arguments.session in (0, 1, 2), 'The requested session is not available. Check your inputs!'
    # no concrete verification available for arguments.rec_number
    assert arguments.mic in ('array', 'head'), 'The requested microphone does not exist. Check your inputs'

    print('All inputs fit the requirements.')


if __name__ == '__main__':
    args = parser.parse_args()
    assert_inputs_basic(arguments=args)
    play_audio(arguments=args)

