# находим нормальный вектор плоскости
import numpy as np
from tkinter import filedialog 
from tkinter.filedialog import askopenfilename




filename1 = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("txt files", "*.txt"),("all files","*.*")))

#fname = 'C:\Users\user\Desktop\Нахождение нормали\a.txt'
File_data1 = np.loadtxt(filename1, usecols=0, dtype=int)
File_data2 = np.loadtxt(filename1, usecols=1, dtype=int)
File_data3 = np.loadtxt(filename1, usecols=2, dtype=int)


#print(File_data1)
#print(File_data2)
#print(File_data3)

#dt_3 = np.dtype([('symbol1','i2'),('symbol2','i2'), ('symbol3','i2'),])

#a, b, c = np.loadtxt(filedialog, dtype=dt_3, skiprows=0, usecols=(0,1,2), unpack = True)
 
#a



#print( "n = (", X,";", Y, ";", Z,")")

face = np.array([[File_data1[0],File_data2[0],File_data3[0]],[File_data1[1],File_data2[1],File_data3[1]],[File_data1[2],File_data2[2],File_data3[2]]])
def calc_face_normale(face):
    # Координаты М1
    #x1 = File_data1[0]
    #y1 = File_data2[0]
    #z1 = File_data3[0]
    x1, y1, z1 = face[0]

    # Координаты М2
    #x2 = File_data1[1]
    #y2 = File_data2[1]
    #z2 = File_data3[1]
    x2, y2, z2 = face[1]


    # Координаты М3
    #x3 = File_data1[2]
    #y3 = File_data2[2]
    #z3 = File_data3[2]
    x3, y3, z3 = face[2]


    #print(x2)
    #print(y2)
    #print(x1)
    #print(z3)
    #print(z1)

    # Найдём координаты вектора М1М2
    V1X1 = x2 - x1
    V1Y1 = y2 - y1
    V1Z1 = z2 - z1

    # Найдём координаты вектора М1М3
    V2X1 = x3 - x1
    V2Y1 = y3 - y1
    V2Z1 = z3 - z1


    #i     j     k
    #V1X1  V1Y1  V1Z1
    #V2X1  V2Y1  V2Z1

    #i*V1Y1*V2Z1+j*V1Z1*V2X1+k*V1X1*V2Y1-i*V2Y1*V1Z1-j*V1X1*V2Z1-k*V1Y1*V2X1

    X = V1Y1*V2Z1-V2Y1*V1Z1
    Y = V1Z1*V2X1-V1X1*V2Z1
    Z = V1X1*V2Y1-V1Y1*V2X1
    print( "n = (", X,";", Y, ";", Z,")")

    return np.array([X,Y,Z])
    
def main():
    calc_face_normale(face)

if __name__ == '__main__':
    main()




