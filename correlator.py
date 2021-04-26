import numpy as np
import healpy as hp
from tqdm import tqdm_notebook

def generate_1d_data(npoints, distrib='gauss'):
    ''' Generate some random data points '''
    if distrib=='gauss':
        data = np.random.normal(0, 1, npoints)
    else:
        data = np.random.uniform(0, 1, npoints)
    return data

def distance(i,j, point_dict):
    ''' Given index i and j, calculate the distance between the points '''
    # We're going to use a stupid distance fn for now.
    # We can replace it with a smarter one that uses healpy
    # and properly gets the spherical distance
    if i==j:
        return 0
    else:
        ip = point_dict[i]
        jp = point_dict[j]
        dprod = np.dot(ip, jp)
        if dprod > 1:
            dist = 0
        elif dprod < -1:
            dist = np.pi
        else:
            dist = np.arccos(dprod)
    return dist

def outercheck(dat):
    ''' Calculate the correlation matrix using np.multiply.outer.
    Only feasible for smaller arrays so best for checking '''

    corr_mat = np.multiply.outer(dat, dat)
    return corr_mat

def distcheck(dat, bins, pdic):
    ''' Calculate the entire distance matrix.
    Only feasible for smaller arrays so best for checking '''

    n = len(dat)
    dist_mat = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            dist_mat[i,j] = bin_distance(i,j, bins, pdic)

    return dist_mat

def bin_distance(i,j,bins, point_dict):
    raw_dist = distance(i,j, point_dict)
    return np.digitize(raw_dist, bins)

def manual_outer(dat, ndx):
    ''' Calculate the row ndx of correlation matrix by hand '''
    # add some code here
    n = len(dat)

    correlation_row = dat*dat[ndx]
    return correlation_row

def dist_matrix(dat, ndx, bins, point_dict):
    ''' Calculate the row ndx of the matrix of distances between '''
    n = len(dat)

    dist = np.array([bin_distance(ndx, i, bins, point_dict) for i in range(n)])
    return dist

def create_pointdict(Nside):
    nmax = hp.nside2npix(Nside)
    
    points = {}
    for i in range(nmax):
        points[i] = np.array(hp.pix2vec(Nside, i), dtype=np.float)
    
    print("Created point dictionary")
    return points


def correlate(dat, bins, disp=False):
    ''' Output averaged values for each distance, in increasing order '''
    # Meat and potatoes of our code. It is also extremely annoying!
    
    dlen = len(dat)
    nside = hp.npix2nside(dlen)
    
    point_dict = create_pointdict(nside)
    maxbins = len(bins) + 1
    
    corr_dict = np.zeros(maxbins)
    count_dict = np.zeros(maxbins)
    for i, v in enumerate(dat):
        if disp:
            if i%100==0:
                print(i)
        data_row = manual_outer(dat, i)
        dist_row = dist_matrix(dat, i, bins, point_dict)
        
        corr_dict += np.bincount(dist_row, data_row, minlength=maxbins)
        count_dict += np.bincount(dist_row, minlength=maxbins)

    print("Calculating averages")
    final_average = corr_dict/count_dict
    
    return final_average, count_dict