import numpy as np
 
from json import load
from convert_words_to_idx import words_to_index
from calc_phrase_index import calc_phrase_index
 
data = load(open('data/indexed_B.json'))
vocabulary = load(open('data/vocabulary.json'))
index_length = load(open('data/index_length.json'))
memory_a = np.zeros((len(data),index_length))
memory_b = []
 
for i, k in enumerate(data.keys()):
    memory_a[i] = np.array([ float(x) for x in k.split(',') ])
    memory_b += [data[k]]
 
A, B = np.polyfit((np.min(memory_a),np.max(memory_a)),(0,1),1)
 
memory_a = memory_a * A + B
 
def get_answer(phrase):
    idx = words_to_index(calc_phrase_index(phrase),vocabulary,index_length) * A + B
    diffs = np.sum((memory_a - idx) ** 2, axis=1)

    phrase_idx = np.argmin(diffs)
 
    return memory_b[phrase_idx]
 
 
if __name__ == '__main__':
    _in = [
        'Привет',
        'Пока',
        'Как дела',
        'Привет, как дела',
        'Сегодня хорошая погода',
        'Привет, как дела',
        'Как вы видите, конец выглядит не лучшим образом, но бывало и хуже.',
    ]
    for p in _in:
        print(f"{p} -> {get_answer(p)}")






        M = np.array(m)

for i2 in range(len(m)):
    leftbottom2 = np.array((m[i2]))
    distances2 = np.linalg.norm(M-leftbottom2, axis=1)
    min_index2 = np.argmin(distances2)
    HERE1 = (f"{M[min_index2]}")
    print(HERE1)

for n, m in zip(xs[1:], xs[:-1]):

   
    n = np.array(n)
    for i1 in range(len(m)):
        leftbottom = np.array((m[i1]))
        distances = np.linalg.norm(n-leftbottom, axis=1)
        min_index = np.argmin(distances)
        NEXT1 = (f"{n[min_index]}")


        n = np.array(n)
        M = np.array(m)
        for i1 in range(len(m)):
            leftbottom = np.array((m[i1]))
            distances = np.linalg.norm(n-leftbottom, axis=1)
            min_index = np.argmin(distances)
            NEXT1 = (f"{n[min_index]}")

                #distances2 = np.linalg.norm(M-leftbottom, axis=1)
                #min_index2 = np.argmin(distances2)
        
     
                #HERE1 = (f"{M[min_index2]}")
          
            print(NEXT1)



new_list = []
for i2 in range(len(n)):
    if m[i2] != NEXT1:
        new_list.append(n[i2])
        new_list = np.array(new_list)
        distances2 = np.linalg.norm(new_list-NEXT1, axis=1)
        min_index2 = np.argmin(distances2)
        
     
        HERE1 = (f"{new_list[min_index2]}")
          
        print(leftbottom, HERE1, NEXT1)
       