import numpy as np
import matplotlib.pyplot as plt
from tftb.processing import WignerVilleDistribution

def s(t, t1=1, t2=2):
    omega1 = 2 * np.pi * 10 
    omega2 = 2 * np.pi * 20
    A = 1
    return np.piecewise(t, 
                        [t < t1, (t >= t1) & (t < t2), t >= t2],
                        [lambda t: A * np.cos(omega1 * t), 
                         lambda t: 0, 
                         lambda t: A * np.cos(omega2 * t)])
t = np.linspace(0, 6, 1024)
wvd = WignerVilleDistribution(s(t), timestamps=t)
wvd.run()

fs = 1 / (t[1] - t[0])
frequencies = np.linspace(0, fs / 2, wvd.tfr.shape[0])
plt.contourf(t, frequencies, np.abs(wvd.tfr), levels=1000, cmap='jet')

plt.tight_layout()
plt.show()
