import re
import numpy as np
from itertools import islice
from itertools import groupby
from itertools import product




def get_coords():
   
    in_file = 'E:cc.gcode'
    
    f = [x for x in open(in_file, 'r').readlines() if x.startswith('G') or x.startswith(';LAY')]
    
    y = re.findall(r'YER:(\d+)(.*?);((LA)|(En))', ''.join(f), re.DOTALL | re.MULTILINE)


    
    layers = (x[1] for x in y)
   
    Z = 0.3
    
    for z, layer in ( (n*Z, v) for n, v in enumerate(layers) ):
        n_rr = re.findall(r'^G.*?X(\d+\.\d+).*?Y(\d+\.\d+)(.*?E(\d+\.\d+))?', layer, re.MULTILINE)
     
        
        
    
        
        for x, y in ((l[:2]) for l in n_rr):


        
            yield float(x),float(y),z



A = list(get_coords())

res = []
for x2,z2 in groupby(A, lambda x2: x2[2]):
    xs = list(z2)
    if len(xs) > 1:

        res += [xs]
        



for n, m in zip(res[1:], res[:-1]):

    print(m,n)
    
   
    
            


        


   

   
         


#print(list(get_coords()))
