num   = [1,2,3,4,5,6,7,8,9,10]
l_num = 1000
def points(num, l_num):
    data = []
    n = int(l_num / len(num))
    for i in range(len(num)):
        a = np.random.normal(0,num[i],n)
        data.append(a)
    return data
    


    
