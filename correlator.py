import numpy as np



def generate_1d_data(npoints, distrib='gauss'):
    ''' Generate some random data points '''
    if distrib=='gauss':
        data = np.random.normal(0, 1, npoints)
    else:
        data = np.random.uniform(0, 1, npoints)
    return data

def distance(i,j):
    ''' Given index i and j, calculate the distance between the points '''
    # We're going to use a stupid distance fn for now.
    # We can replace it with a smarter one that uses healpy
    # and properly gets the spherical distance
    dist = np.abs(i - j)
    return dist

def outercheck(dat):
    ''' Calculate the correlation matrix using np.multiply.outer.
    Only feasible for smaller arrays so best for checking '''

    corr_mat = np.multiply.outer(dat, dat)
    return corr_mat

def distcheck(dat):
    ''' Calculate the entire distance matrix.
    Only feasible for smaller arrays so best for checking '''

    n = len(dat)
    dist_mat = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            dist_mat[i,j] = distance(i,j)

    return dist_mat

def manual_outer(dat, ndx):
    ''' Calculate the row ndx of correlation matrix by hand '''
    # add some code here
    n = len(dat)

    correlation_row = blahblahblahblah
    return correlation_row

def dist_matrix(dat, ndx):
    ''' Calculate the row ndx of the matrix of distances between '''
    n = len(dat)

    dist = huashuashuas
    return dist

def correlate(dat):
    ''' Output averaged values for each distance, in increasing order '''
    # Meat and potatoes of our code. It is also extremely annoying!
    
    corr_dict = {}
    count_dict = {}
    for i,v in enumerate(dat):
        data_row = manual_outer(dat, i)
        dist_row = dist_matrix(dat, i)
        for j,d in enumerate(dist_row):
            if d in corr_dict:
                corr_dict[d] += data_row[j]
                # Do the same thing for the counts
            else:
                corr_dict[d] = data_row[j]
                # Do the same thing for the counts


    # Now calculate the average given the sums and counts!
    # This is not a very efficient way to do things since dictionaries are not the best
    # There is most likely a better way to do this that isn't painful so if you have some time
    # let this simmer and try to think of a better algorithm!

    final_average = someannoyingexpressiontogetthis
    return final_average



nmax = 10
