import re
import numpy as np
from itertools import islice
from itertools import groupby
from itertools import product
from tkinter import filedialog 
from pathlib import Path


#Выбор конечного файла для сохранения результата
filename1 = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("txt files", "*.txt"),("all files","*.*")))

def get_coords():
   
    #Выбираем файл .gcode и прочитываем его послойно
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

r = []
for n7 in res[0:]:
    
    r += n7



open(filename1, "w").close()
with open(filename1,"a") as f3:
    f3.write('# Blender v2.79 (sub 0) OBJ File: ''\n# www.blender.org\nmtllib cube.mtl\no Cube_Cube.001\n')
    f3.close()  


#Достаём координаты и находим нормальный вектор плоскости
for n, m in zip(res[1:], res[:-1]):

    
    for n1, m1 in zip(m[1:], m[:-1]):

        xx1 = m1[0]
        yy1 = m1[1]
        zz1 = m1[2]
        xx2 = n1[0]
        yy2 = n1[1]
        zz2 = n1[2]

        
        xx = (xx1 + xx2)/2
        yy = (yy1 + yy2)/2
        zz = (zz1 + zz2)/2

        n = np.array(n)
        leftbottom = np.array((xx, yy, zz))
        distances = np.linalg.norm(n-leftbottom, axis=1)
        min_index = np.argmin(distances)
        NEXT1 = np.array(n[min_index])

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

        #print( "n = (", X13,";", Y13, ";", Z13,")")
        with open(filename1,"a") as f1:
        
            f1.write('vn {} {} {} \n'.format(X13, Y13, Z13))
            f1.close()

