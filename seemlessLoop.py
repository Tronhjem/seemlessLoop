from pydub import AudioSegment
import os
import argparse


def combineTail():
    """
    Takes a folder with audio files, and loop through all of them.
    For each file, the tail after the specified loop length is faded, 
    and applied to the beginning of the loop, for seemless looping.
    """
    path = cliArgs.path
    bpm = cliArgs.bpm
    loopLengthInBars = cliArgs.l

    loopLengthInMs = (60000 / bpm) * 4 * loopLengthInBars

    fileList = os.listdir(path)

    for file in fileList:
        # TODO checkf or audio file extensions instead of just not .DS_Store
        if not file == ".DS_Store":
            sound = AudioSegment.from_file(os.path.join(path, file), format="wav")
            loop = sound[0:loopLengthInMs]
            tail = sound[loopLengthInMs : len(sound)]
            tailLength = len(tail)
            print(tailLength)
            if tailLength < 1:
                tailLength = 1

            tail = tail.fade_out(tailLength)

            combined = loop.overlay(tail)
            newFileName = file.split(".")[0] + "_2ndPass.wav"
            print(newFileName)
            file_handle = combined.export(os.path.join(path, newFileName), format="wav")


if __name__ == "__main__":

    # TODO 1. variable append name. 2. move loop out of method for cleaner method.

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", nargs="?", type=str, help="path to folder with files to process'"
    )
    parser.add_argument("-bpm", type=float, default=60, help="Project bpm")
    parser.add_argument("-l", type=float, default=4, help="length of loop in beats")

    cliArgs = parser.parse_args()

    combineTail()

    print("done")
