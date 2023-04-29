#!/usr/bin/env python
# coding: utf-8


#from ipywidgets import interactive
import numpy as np
from matplotlib import pyplot as plt


Z = np.arange(1000,12000,1000)
SA = np.arange(-15,15,1)

Fnomin = 5000

#def f(Pky1, Pky2, Pdy1, Pdy2, Pcy1, Pey1, Pey2):
Pky1 = -40
Pky2 = 1.2
Pdy1 = 1.2
Pdy2 = -0.1
Pcy1 = 1.4
Pey1 = -1
Pey2 = 0

f = plt.figure(figsize=(8,6))
ax = f.add_subplot(221)
ax2 = f.add_subplot(222)
ax3 = f.add_subplot(223)
Ky = Pky1*Fnomin*np.sin(2*np.arctan(Z/(Pky2*Fnomin)))
ax.plot(Z, Ky, '-')
ax.grid()
ax.set_title("D(Z)")
ax.set_xlabel("Z [N]")
#ax.set_ylabel("Cornering stiffness [N/rad]")

Muy = Pdy1 + Pdy2*(Z-Fnomin)/Fnomin
ax3.plot(Z, Muy, '-')
ax3.grid()
ax3.set_title("Mu(Z)")
ax3.set_xlabel("Z [N]")

for Fz in [2000, 5000, 8000, 11000]:
    D = (Pdy1 + Pdy2*(Fz-Fnomin)/Fnomin)*Fz
    B = Pky1*Fnomin*np.sin(2*np.arctan(Fz/(Pky2*Fnomin)))/D/Pcy1
    E = Pey1 + Pey2*(Fz-Fnomin)/Fnomin
    Fy = D*np.sin(Pcy1*np.arctan(B*SA*(np.pi/180) - E*(B*SA*(np.pi/180) - np.arctan(B*SA*(np.pi/180)))))
    
    ax2.plot(SA, Fy, '-', label="Fz ="+str(Fz)+" N")
ax2.legend()
ax2.grid()
ax2.set_title("Fy(SA)")
ax2.set_xlabel("SA [°]")
#ax2.set_ylabel("Fy [N]")
    

#interactive_plot = interactive(f, Pky1=(-100, 0, 1), Pky2=(0, 3, 0.1), Pdy1=(0, 3, 0.01), Pdy2=(-0.5, 0, 0.01), Pcy1=(1, 2, 0.01), Pey1=(-5, 1, 0.1), Pey2=(-5, 5, 0.1))

#interactive_plot

