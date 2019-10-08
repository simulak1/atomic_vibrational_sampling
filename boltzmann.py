import numpy as np

def _get_amplitude_sqr(w,T):
    
    kb = 1.38064852*10**-23
    hbar = 6.62607004*10**-34

    if T<0.00000001:
        occupation=0
    else:
        occupation=(np.exp(hbar*w/(kb*T))-1)**-1
    
    return (hbar/w)*(occupation + 0.5)
    
def mean_square_displacement(W,T,m):
    Nw=W.shape[0]
    usqr=0
    for i in range(Nw):
        usqr+=_get_amplitude_sqr(W[i],T)
    usqr/=m
    return usqr
