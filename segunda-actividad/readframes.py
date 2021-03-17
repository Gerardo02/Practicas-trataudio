import wave
import numpy as np
import matplotlib.pyplot as plt


### onda de good morning ###
print('\nFrames de good morning')

good_morning = wave.open('good-morningMan.wav', 'r')
frames = good_morning.readframes(-1)
print(frames[:10])

ondaConvertida = np.frombuffer(frames, dtype="int16")
#print(ondaConvertida [:10])
framerate_gm = good_morning.getframerate()
print(framerate_gm)

time_gm = np.linspace(start=0, stop=len(ondaConvertida) / framerate_gm, num=len(ondaConvertida))
print(time_gm[:10])






### onda de good afternoon ###
print('\nFrames de good afternoon')

good_afternoon = wave.open('good-afternoon.wav', 'r')
frames2 = good_afternoon.readframes(-1)
print(frames2[:10])

ondaConvertida2 = np.frombuffer(frames2, dtype="int16")
#print(ondaConvertida2 [:10])
framerate_gm2 = good_afternoon.getframerate()
print(framerate_gm2)

time_gm2 = np.linspace(start=0, stop=len(ondaConvertida2) / framerate_gm2, num=len(ondaConvertida2))
print(time_gm2[:10])


### onda de plane ###
print('\nFrames de plane')

plane = wave.open('plane.wav', 'r')
frames3 = plane.readframes(-1)
print(frames3[:10])

ondaConvertida3 = np.frombuffer(frames3, dtype="int16")
#print(ondaConvertida3 [:10])
framerate_gm3 = plane.getframerate()
print(framerate_gm3)

time_gm3 = np.linspace(start=0, stop=len(ondaConvertida3) / framerate_gm3, num=len(ondaConvertida3))
print(time_gm3[:10])




### onda de anymore ###
print('\nFrames de anymore')

anymore = wave.open('anymore.wav', 'r')
frames4 = anymore.readframes(-1)
print(frames4[:10])

ondaConvertida4 = np.frombuffer(frames4, dtype="int16")
#print(ondaConvertida4 [:10])
framerate_gm4 = anymore.getframerate()
print(framerate_gm4)

time_gm4 = np.linspace(start=0, stop=len(ondaConvertida4) / framerate_gm4, num=len(ondaConvertida4))
print(time_gm4[:10])




#generacion de la grafica

plt.title('Good morning vs good afrternoon')

#etiqueta de los ejes
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')

#agregar informacion de las ondas para graficar
plt.plot(time_gm, ondaConvertida, label='Good morning')
plt.plot(time_gm2, ondaConvertida2, label='Good afternoon', alpha=0.5)
plt.plot(time_gm3, ondaConvertida3, label='Plane', alpha=0.5)
plt.plot(time_gm4, ondaConvertida4, label='Anymore', alpha=0.5)

plt.legend()
plt.show()
