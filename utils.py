import tf_freq_id
import tracetools as tt
import matplotlib.pyplot as plt 
import numpy as np
import control as ctrl

def pt2(omega,zeta):
    return ctrl.tf(omega**2,[1,2*zeta*omega,omega**2])

def notch(omega_n,zeta_n,omega_d,zeta_d):
    return pt2(omega_d,zeta_d)/pt2(omega_n,zeta_n)

def tf_from_txt(fname):
    with open(fname) as f:
        lines = f.readlines()
    
    lines_s = ''.join(lines)

    num_s = lines_s.split(']')[0].strip()
    den_s = lines_s.split(']')[1].strip()

    num_s = num_s.replace('[','').replace(']','').replace('\n','')
    den_s = den_s.replace('[','').replace(']','').replace('\n','')

    num = [float(x) for x in num_s.split()]
    den = [float(x) for x in den_s.split()]
    return ctrl.tf(num,den)

def print_tf(tf,f):
    num = tf.num[0][0]
    den = tf.den[0][0]

    #num = np.flip(num)
    #den = np.flip(den)

    f.write(str(num))
    f.write('\n')
    f.write(str(den))

def plot_mag(G):
    resp = ctrl.frequency_response(G)
    w = resp.omega 
    Y = resp.response[0][0]

    plt.semilogx(w,ctrl.mag2db(np.abs(Y)),label=G.name)


def bodemag(G,omega=None,**kwargs):
    resp = ctrl.frequency_response(G, omega)
    mag = np.abs(resp.response[0][0])
    omega = resp.omega

    plt.semilogx(omega, 20*np.log10(mag),**kwargs)