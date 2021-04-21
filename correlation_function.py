import numpy as np

def distance(i,j):
    ''' Given index i and j, calculate the distance between the points '''
    # We're going to use a stupid distance fn for now.
    # We can replace it with a smarter one that uses healpy
    # and properly gets the spherical distance
    dist = np.abs(i - j)
    return dist
  
  def correlate(data):
    corr_dict = {}
    count_dict = {}
    means = {}
    n = len(data)
    for i in range(n):
        #data row
        data_row = data[i] * data
        dist_row = np.zeros(n)
        #distance row
        for j in range(n):
            dist_row[j] = distance(i,j)
        #assigning data into dictionaries
        for k in range(n):
            if dist_row[k] in corr_dict:
                corr_dict[dist_row[k]]  += data_row[k]
                count_dict[dist_row[k]] += 1
            else:
                corr_dict[dist_row[k]]   = data_row[k]
                count_dict[dist_row[k]]  = 1
    #means
    for key in corr_dict:
        means[key] = corr_dict[key]/count_dict[key] 

    return means
