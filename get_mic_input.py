import pyaudio
import numpy as np
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
# WAVE_OUTPUT_FILENAME =
RATE = 44100
audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
frames = []

signal = stream.read(CHUNK)
ft = np.fft.rfft(np.fromstring(signal, dtype=np.int16))
ft = np.delete(ft, len(ft) - 1)
amp = np.log10(np.abs(ft)) ** 2
freqs = np.fft.rfftfreq(len(signal), d=1. / RATE)
print amp
# for freq, val in zip(freqs, np.abs(ft)):
#     print freq, val
# print freqs
# peak = np.average(np.abs(data))
# print peak
# bars = '#' * int(50 * peak / 2**16)
# print("%05d %s" % (peak, bars))
# frames.append(data)
    # print np_array
