import numpy as np
from astropy.io import fits
import healpy as hp
import pickle
from scipy import special

fin_nside = 256

fullmap = fits.open('./data/COM_CMB_IQU-smica_2048_R3.00_hm1.fits')
idata = fullmap[1].data["I_STOKES"]
print("Loaded data")
ring_datai = hp.reorder(idata, inp='NESTED', out='RING')


slow=False

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

npix = hp.nside2npix(fin_nside)

for l in range(lmax):
    print("On l:", l)
    lilm = []
    maxl = min(l, 10)
    if slow:
        for m in range(0, maxl+1):
            mval = np.sum(np.conj(special.sph_harm(m, l, anglist[:,1], anglist[:,0]))*lesspretty*4*np.pi/npix)
            lilm.append(mval)
    else:
        for m in range(0, l+1):
            mval = np.sum(np.conj(special.sph_harm(m, l, anglist[:,1], anglist[:,0]))*lesspretty*4*np.pi/npix)
            lilm.append(mval)
    A_lm.append(lilm)

if slow:
    fname = "./data/calc_alms_"+str(fin_nside)+'_slow'
else:
    fname = "./data/calc_alms_"+str(fin_nside)+'_bad'
    
with open(fname, 'wb') as f:
    pickle.dump(A_lm, f)
