import re

def get_coords():
    in_file = 'C:\\Users\\user\\Desktop\\Нахождение нормали\\cc.gcode'

    f = [x for x in open(in_file, 'r').readlines() if x.startswith('G') or x.startswith(';LAY')]
    y = re.findall(r'YER:(\d+)(.*?);((LA)|(En))', ''.join(f), re.DOTALL | re.MULTILINE)


    layer_count = len(y)
    layers = (x[1] for x in y)

    Z = 0.3
    for z, layer in ( (n*Z, v) for n, v in enumerate(layers) ):
        n_rr = re.findall(r'^G.*?X(\d+\.\d+).*?Y(\d+\.\d+)(.*?E(\d+\.\d+))?', layer, re.MULTILINE)
    # print(n_rr)
        
        for x, y in ((l[:2]) for l in n_rr):
            yield x, y, z

print(list(get_coords()))