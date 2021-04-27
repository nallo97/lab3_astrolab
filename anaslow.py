import numpy as np
from astropy.io import fits
import healpy as hp
import pickle
from scipy import special

fin_nside = 512


fullmap = fits.open('./data/COM_CMB_IQU-smica_2048_R3.00_hm1.fits')
idata = fullmap[1].data["I_STOKES"]
print("Loaded data")
ring_datai = hp.reorder(idata, inp='NESTED', out='RING')

lesspretty = hp.ud_grade(ring_datai, fin_nside)

print("Reduced quality")

anglist = []
for i in range(hp.nside2npix(fin_nside)):
    anglist.append(np.array(hp.pix2ang(fin_nside, i)))
    
print("Created anglist")

anglist = np.array(anglist)               
A_lm = []

lmax = 3*fin_nside - 1
print("lmax = ", lmax)

for l in range(lmax):
    print("On l:", l)
    lilm = []
    maxl = min(l, 10)
    for m in range(-maxl, maxl+1):
        mval = np.sum(np.conj(special.sph_harm(m, l, anglist[:,0], anglist[:,1]))*lesspretty)
        lilm.append(mval)
    A_lm.append(lilm)

with open("./data/calc_alms_"+str(fin_nside), 'wb') as f:
    pickle.dump(A_lm, f)