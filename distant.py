import numpy as np

from itertools import product
from itertools import islice
from tkinter import filedialog 



filename1 = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("txt files", "*.txt"),("all files","*.*")))
#filename1 = 'E:norm.txt'


xs = [[(12.96, 10.488, 0.0),(12.841, 10.963, 0.0),(12.647, 11.412, 0.0),(12.382, 11.824, 0.0)],
[(9.8, 9.8, 0.3),(9.4, 9.4, 0.3),(9.01, 9.01, 0.3),(8.829, 0.221, 0.3)],
[(9.8, 9.8, 0.6),(9.4, 9.4, 0.6),(9.01, 9.01, 0.6),(0.344, 8.829, 0.6)],
[(9.8, 9.8, 0.8999999999999999), (9.4, 9.4, 0.8999999999999999), (9.039, 1.968, 0.8999999999999999)],
[(9.8, 9.8, 1.2), (9.4, 9.4, 1.2), (9.039, 1.968, 1.2), (9.039, 9.039, 1.2), (9.04, 9.04, 1.2), (9.039, 5.102, 1.2)]]

r = []
for n7 in xs[0:]:
    
    r += n7

#print(r)
    

open(filename1, "w").close()

for n3 in xs[0:]:
    
    #print(n3)
    for n4 in n3[0:]:
        #print(n4)
        xxx1 = n4[0]
        yyy1 = n4[1]
        zzz1 = n4[2]



       
        with open(filename1,"a") as f:
        
            f.write('v {} {} {} \n'.format(xxx1, yyy1, zzz1))
            f.close()


        
    

for n, m in zip(xs[1:], xs[:-1]):

  
    for n1, m1 in zip(m[1:], m[:-1]):
        
        
        xx1 = m1[0]
        yy1 = m1[1]
        zz1 = m1[2]
        xx2 = n1[0]
        yy2 = n1[1]
        zz2 = n1[2]

        #print(tt1)
        #print(tt2)

        #print(xx1, yy1, zz1, xx2,  yy2, zz2)
        xx = (xx1 + xx2)/2
        yy = (yy1 + yy2)/2
        zz = (zz1 + zz2)/2

        

        

        #print(m1,n1)




    
       #print(m)
        n = np.array(n)
        leftbottom = np.array((xx, yy, zz))
        distances = np.linalg.norm(n-leftbottom, axis=1)
        min_index = np.argmin(distances)
        NEXT1 = np.array(n[min_index])


        #print(xx, yy, zz)
        #print(m1, n1, type(NEXT1), NEXT1.shape)

        xx3 = NEXT1[0]
        yy3 = NEXT1[1]
        zz3 = NEXT1[2]
        
        

        # Найдём координаты вектора М1М2
        V1X1 = xx2 - xx1
        V1Y1 = yy2 - yy1
        V1Z1 = zz2 - zz1

        # Найдём координаты вектора М1М3
        V2X1 = xx3 - xx1
        V2Y1 = yy3 - yy1
        V2Z1 = zz3 - zz1

        X13 = V1Y1*V2Z1-V2Y1*V1Z1
        Y13 = V1Z1*V2X1-V1X1*V2Z1
        Z13 = V1X1*V2Y1-V1Y1*V2X1


        with open(filename1,"a") as f1:
        
            f1.write('vn {} {} {} \n'.format(X13, Y13, Z13))
            f1.close()


        
        #print( "n = (", X13,";", Y13, ";", Z13,")")

for n10, m11 in zip(xs[1:], xs[:-1]):

  
    for n12, m13 in zip(m11[1:], m11[:-1]):
        
        ttt1 = r.index(m13)
        ttt2 = r.index(n12)
        xx1 = m1[0]
        yy1 = m1[1]
        zz1 = m1[2]
        xx2 = n1[0]
        yy2 = n1[1]
        zz2 = n1[2]

        #print(tt1)
        #print(tt2)

        #print(xx1, yy1, zz1, xx2,  yy2, zz2)
        xx = (xx1 + xx2)/2
        yy = (yy1 + yy2)/2
        zz = (zz1 + zz2)/2

        

        

        #print(m1,n1)




    
       #print(m)
        n = np.array(n)
        leftbottom = np.array((xx, yy, zz))
        distances = np.linalg.norm(n-leftbottom, axis=1)
        min_index = np.argmin(distances)
        NEXT1 = np.array(n[min_index])


        #print(xx, yy, zz)
        #print(m1, n1, type(NEXT1), NEXT1.shape)

        xx3 = NEXT1[0]
        yy3 = NEXT1[1]
        zz3 = NEXT1[2]
        
        tt3 = (xx3, yy3, zz3)
        ttt3 = r.index(tt3)
        


        


        with open(filename1,"a") as f2:
        
            f2.write('f {}//{} {}//{} {}//{} \n'.format(ttt1, ttt2, ttt2, ttt3, ttt3, ttt1))
            f2.close()
        
      
        

    
    



    
       

    


        
        

    




    
    
        
    
