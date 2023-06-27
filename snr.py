import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#m11 = 100000
m17 = 12.5
m12 = 13.5
m13 = 14
m14 = 15.4
m15 = 16.5
m16 = 17.5
m_vec = [m14, m12, m13, 'SNR = 200', m15, m16, m17]
M0 = 1750.6
#S_p11 = M0 * 10**(-0.4*m11)
S_p12 = M0 * 10**(-0.4*m12)
S_p13 = M0 * 10**(-0.4*m13)
S_p14 = M0 * 10**(-0.4*m14)
S_p15 = M0 * 10**(-0.4*m15)
S_p16 = M0 * 10**(-0.4*m16)
S_p17 = M0 * 10**(-0.4*m17)
t_max = 8000
m_BKR = 23.5
BKG = M0 * 10**(-0.4*m_BKR) #fotoni background per cm**2 per secondo centrato in banda u (ugriz)
delta = 3*0.7 #
phi = 1. #in arcsec
D = 820 #in cm
A = np.pi*0.25*D**2 #area dello specchio
eta = 0.1124 #efficienza
DK = 0.000139 #e- per second per pixel
pix = 0.122 #arcsec
pix_size = 15 #microsec
#snrx11 = []
snrx12 = []
snrx13 = []
snrx14 = []
snrx15 = []
snrx16 = []
snrx17 = []
snrx2 = []
snrxR = []
ROnnie = 2.5
sigma_grating1 = 3580 #grooves per mm
beta_grating = 35.841/360*2*np.pi
f_cam = 464
deltaLambda1 = 10**4*np.cos(beta_grating)/sigma_grating1/f_cam *pix_size


t_exp = []
for x in range(1000):
    t_exp.append(1.*x/1000.*t_max)
    #snrx11.append((S_p11 * A * eta *deltaLambda1*t_exp[x])/(np.sqrt(((S_p11 +2*BKG*delta*phi)*deltaLambda1*A*eta+delta/pix*DK)*t_exp[x]+delta/pix*ROnnie**2)))
    snrx12.append((S_p12 * A * eta *deltaLambda1*t_exp[x])/(np.sqrt(((S_p12 +2*BKG*delta*phi)*deltaLambda1*A*eta+delta/pix*DK)*t_exp[x]+delta/pix*ROnnie**2)))
    snrx13.append((S_p13 * A * eta *deltaLambda1*t_exp[x])/(np.sqrt(((S_p13 +2*BKG*delta*phi)*deltaLambda1*A*eta+delta/pix*DK)*t_exp[x]+delta/pix*ROnnie**2)))
    snrx14.append((S_p14 * A * eta *deltaLambda1*t_exp[x])/(np.sqrt(((S_p14 +2*BKG*delta*phi)*deltaLambda1*A*eta+delta/pix*DK)*t_exp[x]+delta/pix*ROnnie**2)))
    snrx15.append((S_p15 * A * eta *deltaLambda1*t_exp[x])/(np.sqrt(((S_p15 +2*BKG*delta*phi)*deltaLambda1*A*eta+delta/pix*DK)*t_exp[x]+delta/pix*ROnnie**2)))
    snrx16.append((S_p16* A * eta *deltaLambda1*t_exp[x])/(np.sqrt(((S_p16 +2*BKG*delta*phi)*deltaLambda1*A*eta+delta/pix*DK)*t_exp[x]+delta/pix*ROnnie**2)))
    snrx17.append((S_p17 * A * eta *deltaLambda1*t_exp[x])/(np.sqrt(((S_p17 +2*BKG*delta*phi)*deltaLambda1*A*eta+delta/pix*DK)*t_exp[x]+delta/pix*ROnnie**2)))
    snrxR.append(200)


#xarr = np.array([[t_exp],[t_exp],[t_exp],[t_exp],[t_exp]])
#yarr = np.array([[snrx17],[snrx12],[snrx13],[snrxR],[snrx15]])
xarr = np.array([[t_exp],[t_exp],[t_exp],[t_exp],[t_exp],[t_exp],[t_exp]])
yarr = np.array([[snrx14],[snrx12],[snrx13],[snrxR],[snrx15],[snrx16],[snrx17]])

for i in range(len(m_vec)):
    plt.plot(xarr[i,0]/60, yarr[i,0], label=str(m_vec[i]))

plt.xlabel("Tempo di Esposizione (minuti)")
plt.ylabel("SNR")
plt.legend()
plt.show()

print("\n\n\n\n\n")

print("Calcolo SNR(T_exp) per magnitudine specifica")
chk_keep = 'y' 
while(chk_keep == 'y'):
    m = input("inserisci la magnitudine AB dell'oggetto da osservare: ")
    m = float(m)
    S_p = M0 * 10**(-0.4*m) #fotoni segnale per cm**2 per secondo centrato in banda u (ugriz)
    T_exp = []
    CHK = True
    T_200SNR = 0
    snrx1 = []
    for x in range(1000):
        T_exp.append(1.*x/1000.*t_max)
        snrx1.append((S_p * A * eta *deltaLambda1*T_exp[x])/(np.sqrt(((S_p +2*BKG*delta*phi)*deltaLambda1*A*eta+delta/pix*DK)*T_exp[x]+delta/pix*ROnnie**2)))
        if(snrx1[x]>= 200 and CHK):
            T_200SNR = T_exp[x]/60
            CHK = False
    print("SNR dopo 60 minuti")
    print(snrx1[450])
    print("SNR dopo 120 minuti")
    print(snrx1[900])
    print("tempo di esposizione per ottenere SNR = 200")
    if(T_200SNR>0):
        print(str(T_200SNR) + r' min')
    else:
        print("Tempo richiesto superiore alle 2 ore")
    chk_keep = input("vuoi ripetere il calcolo per un altro valore di magnitudine? (y/n)  ")

