from pathlib import Path
import os.path
import subprocess


# Shigt are in seconds
def splitSound(inputFileName):

    inputFile = Path(inputFileName)
    inputExtension = os.path.splitext(inputFileName)[1][1:]

    if inputExtension != 'wav':
        raise Exception('Inputfile is not .wav')

    timeShift = get_time(0)
    timeVideo = get_time(120)

    if inputFile.is_file():

        str_cmd = 'ffmpeg -i {0} -ss {1} -t {2} {3}'
        str_cmd = str_cmd.format(
            inputFileName, timeShift, timeVideo, 'subsound.wav')
        print(str_cmd)

        try:
            subprocess.check_call(str_cmd, shell=True)

        except Exception as e:
            raise e

        finally:
            pass

    else:
        print('{0} File does exist'.format(inputFileName))


def get_time(nbSeconds):

    minutes, seconds= divmod(nbSeconds, 60)
    hours, minutes= divmod(minutes, 60)

    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
