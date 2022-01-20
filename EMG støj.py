#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:37:37 2022

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



M=np.array([1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8])
#array på 8, 1/8 forekommer 8 gange


FiltUMAS=signal.filtfilt(M,1,ecg0)
plt.plot(FiltUMAS)
plt.title("EKG uden EMG støj")
plt.xlabel("tid(s)")
plt.ylabel("amplitude")
plt.show()


#frekvensdomænet
plt.magnitude_spectrum(FiltUMAS,Fs)
plt.title("EKG uden EMG støj")
plt.show()



