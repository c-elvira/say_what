from pathlib import Path
import os.path
import subprocess


def extractVideoFromText(inputFileName, outputFileName, outputFolder=''):

    if outputFolder != '':
        if not outputFolder.endswith('/'):
            outputFolder += '/'

    inputFile = Path(inputFileName)
    outputFile = Path(outputFolder + outputFileName)

    outputExtension = os.path.splitext(outputFileName)[1][1:]

    if inputFile.is_file():

        str_cmd = 'ffmpeg -i {0} -vn -ar 44100 -ac 2 -ab 192k -f {1} {2}'
        str_cmd = str_cmd.format(
            inputFileName, outputExtension, outputFolder + outputFileName)

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
