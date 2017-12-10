import numpy as np
arr  = np.asarray([0,10,50,80,100])
for a in arr:
    x = float(a-np.min(arr))/(np.max(arr) - np.min(arr))
    print x