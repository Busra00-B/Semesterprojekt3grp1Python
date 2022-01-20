#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:55:12 2022

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

#baseline støjet fjernes

L=303
Fc=0.667

#designet filter
FiltHP = signal.firwin(numtaps=L, cutoff=0.667, fs=1/Ts, pass_zero=False)

FiltUB=signal.filtfilt(FiltHP,1,ecg0)
plt.title("EKG uden baselinestøj")
plt.xlabel("tids")
plt.ylabel("milivolts")
plt.plot(t,FiltUB)
plt.show()

#powerline støjen fjernes fra det ekg signal vi har fjernet baseline støjen
f1=50
Q1=50/120
Fs=500

#filter  som fjerner powerline interference støj 
b1,a1=signal.iirnotch(f1,Q1,Fs)
freq, h = signal.freqz(b1, a1, fs=Fs)

FiltUBPS=signal.filtfilt(b1,a1,FiltUB)
plt.title("EKG uden baseline + powerline støj")
plt.plot(FiltUBPS)
plt.show()

#EMG støjen fjernes fra det ekg signal vi har fjernet baseline+poerline støjen

M=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]

FiltUBPES=signal.filtfilt(M,1,FiltUBPS)
plt.plot(FiltUBPES)
plt.ylim([-0.1, 0.4])
plt.title("EKG uden de tre støjtyper")
plt.xlabel("tid(s)")
plt.ylabel("amplitude")
plt.show()

#frekvensdomænet
#spektrum uden baseline støj
plt.magnitude_spectrum(FiltUB,Fs,color="blue")
plt.title("EKG uden baseline støj")
plt.show()

#spektrum uden baseline og powerline støj
plt.magnitude_spectrum(FiltUBPS,Fs, color="red")
plt.title("EKG uden baseline og powerline støj")
plt.show()

#spektrum uden de tre typer støj
plt.magnitude_spectrum(FiltUBPES,Fs, color="purple")
plt.title("EKG uden de 3 typer støj")
plt.show()




