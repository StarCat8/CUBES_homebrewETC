import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


m = input("inserisci la magnitudine AB dell'oggetto da osservare: ")
m = float(m)
m = 13
t_max = 5000
m_BKR = 23.5
S_p = 1539.6 * 10**(-0.4*m) #fotoni segnale per cm**2 per secondo centrato in banda u (ugriz)
BKG = 1539.6 * 10**(-0.4*m_BKR) #fotoni background per cm**2 per secondo centrato in banda u (ugriz)
delta = 6*0.7 #
phi = 1. #in arcsec
D = 820 #in cm
A = np.pi*0.25*D**2 #area dello specchio
eta = 0.1124 #efficienza
DK = 0.000139 #e- per second per pixel
pix = 0.122 #arcsec
pix_size = 15 #microsec
snrx1 = []
snrx2 = []
ROnnie = 2.5
sigma_grating1 = 3580 #grooves per mm
sigma_grating2 = 3108 #grooves per mm
beta_grating = 35.841/360*2*np.pi
f_cam = 464
deltaLambda1 = 10**4*np.cos(beta_grating)/sigma_grating1/f_cam *pix_size
deltaLambda2 = 10**4*np.cos(beta_grating)/sigma_grating2/f_cam *pix_size


t_exp = []
for x in range(1000):
    t_exp.append(1.*x/1000.*t_max)
    snrx1.append((S_p * A * eta *deltaLambda1*t_exp[x])/(np.sqrt(((S_p +2*BKG*delta*phi)*deltaLambda1*A*eta+2*delta/pix*DK)*t_exp[x]+35*ROnnie**2)))
    snrx2.append((S_p * A * eta *deltaLambda2*t_exp[x])/(np.sqrt(((S_p +2*BKG*delta*phi)*deltaLambda2*A*eta+2*delta/pix*DK)*t_exp[x]+35*ROnnie**2)))


xarr = np.array([[t_exp],[t_exp]])
yarr = np.array([[snrx1],[snrx2]])

for i in range(2):
    plt.plot(xarr[i,0], yarr[i,0])

plt.xlabel("Exposure Time (seconds)")
plt.ylabel("SNR")
red_patch1 = mpatches.Patch(color='orange', label='3580 grating')
red_patch2 = mpatches.Patch(color='blue', label='3108 grating')
plt.show()

2400/5000
