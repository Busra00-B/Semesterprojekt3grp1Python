#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:03:21 2022

@author: BILGIN
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

import wfdb

# Read the two ECG signals (raw, filtered) and read 
# the related information.
signals, info = wfdb.rdsamp('rec_2', channels=[0, 1], 
                              sampfrom=0, sampto=2000)

Fs=500
Ts=1/Fs


t=np.arange(0,2000*Ts,Ts)

ecg0 = signals[:,0]
ecg1 = signals[:,1]



#baseline wander

#f0 og f1 står for fnotch, henholdvis for baseline wander og powerline interference 
f0=0.67
f1=50

#Q kan også skrives som f0/5
Q=0.67/5
Fs=500


#filter som fjerne baseline wander støj
b0,a0=signal.iirnotch(f0,Q,Fs)
freq, h = signal.freqz(b0, a0, fs=Fs)

FiltUBS=signal.filtfilt(b0,a0,ecg0)
plt.title("EKG uden baseline wander støj")
plt.plot(FiltUBS)
plt.show()



#powerline
f1=50
Q1=50/120
Fs=500

#FiltUBS=signal.filtfilt(b,a,ecg0) giv outputtet fra baseline filteret et nyt navn som skal skrives ind i ecg0 plads for at fjerne powerline støjen fra det ekg som vi har fjernet baseline støjen fra. 

#filter  som fjerner powerline interference støj 
b1,a1=signal.iirnotch(f1,Q1,Fs)
freq, h = signal.freqz(b1, a1, fs=Fs)

FiltUBPS=signal.filtfilt(b1,a1,FiltUBS)
plt.title("EKG uden baseline + powerline støj")
plt.plot(FiltUBPS)
plt.show()


#frekvensdomænet
#Spectrum for EKG uden baseline wander støj
plt.magnitude_spectrum(FiltUBS,Fs, color="blue")
plt.title("EKG uden baseline støj")
plt.xlabel("frekvensdomænet")


#spectrum for EKG uden baseline + powerline støj

plt.magnitude_spectrum(FiltUBPS,Fs, color="red")
plt.title("EKG uden baseline +powerline støj")
plt.xlabel("frekvensdomænet")
plt.show()

plt.magnitude_spectrum(FiltUBPS,Fs)
#kommentar på at peak på 50 er væk











