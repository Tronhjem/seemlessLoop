# Seemless loop maker

This is a commandline python tool to take tail after specified loop length
and apply it to the beginning.
This allows music loops to loop seemless, if there's a lot of reverb or tail after the loop is ended.

# Install:

make sure pydub is installed:
pip install pydub

# Usage:

python seemlessLoop.py path/to/folder/with/audiofiles -bpm someIntForBpm -l someIntForLength

-bpm is for specifying bpm of loops
-l is loop length in bars.

# Example of cutting loops:

Loops to make seemless loops of 16 bars, loops have a bpm of 90

python seemlessLoop.py path/to/folder/with/audiofiles -bpm 90 -l 16
