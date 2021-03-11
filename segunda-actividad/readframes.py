import wave
import numpy as np

wenosDiablos = wave.open('good-morningMan.wav', 'r')

frames = wenosDiablos.readframes(-1)

print(frames[:10])

ondaConvertida = np.frombuffer(frames, dtype="int16")

print(ondaConvertida [:10])