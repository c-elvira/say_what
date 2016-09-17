from pathlib import Path
import os.path
import subprocess
#from datetime import date, time, datetime, timedelta


# Shigt are in seconds
def extractVideoFromText(inputFileName, outputFileName, outputFolder='', shiftInSecond=0):

    if outputFolder != '':
        if not outputFolder.endswith('/'):
            outputFolder += '/'

    inputFile = Path(inputFileName)
    outputFile = Path(outputFolder + outputFileName)

    outputExtension = os.path.splitext(outputFileName)[1][1:]

    timeShift = get_shift_str(shiftInSecond)

    if inputFile.is_file():

        str_cmd = 'ffmpeg -i {0} -vn -ar 44100 -ac 2 -ab 192k -ss {3} -f {1} {2}'
        str_cmd = str_cmd.format(
            inputFileName, outputExtension, outputFolder + outputFileName, timeShift)

        try:
            if not outputFile.is_file():
                subprocess.check_call(str_cmd, shell=True)

            else:
                print('{0} already exist'.format(outputFileName))
        except Exception as e:
            raise e

        finally:
            pass

    else:
        print('{0} File does exist'.format(inputFileName))


def get_shift_str(shiftInSecond):

    minutes, seconds= divmod(shiftInSecond, 60)
    hours, minutes= divmod(minutes, 60)

    #t = timedelta(seconds=shiftInSecond)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
