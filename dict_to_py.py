
import os 
import time

path = os.path.join(os.path.split(__file__)[0], 'dict.txt')
dic = {}
file = open(path)
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []
t = []
u = []
v = []
w = []
x = []
y = []
z = []
for fi in file:
        while fi[-1] not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            fi = fi[0:-1]
        if 'a' in fi:
            a.append(fi)
        if 'b' in fi:
            b.append(fi)
        if 'c' in fi:
            c.append(fi)
        if 'd' in fi:
            d.append(fi)
        if 'e' in fi:
            e.append(fi)
        if 'f' in fi:
            f.append(fi)
        if 'g' in fi:
            g.append(fi)
        if 'h' in fi:
            h.append(fi)
        if 'i' in fi:
            i.append(fi)
        if 'j' in fi:
            j.append(fi)
        if 'k' in fi:
            k.append(fi)
        if 'l' in fi:
            l.append(fi)
        if 'm' in fi:
            m.append(fi)
        if 'n' in fi:
            n.append(fi)
        if 'o' in fi:
            o.append(fi)
        if 'p' in fi:
            p.append(fi)
        if 'q' in fi:
            q.append(fi)
        if 'r' in fi:
            r.append(fi)
        if 's' in fi:
            s.append(fi)
        if 't' in fi:
            t.append(fi)
        if 'u' in fi:
            u.append(fi)
        if 'v' in fi:
            v.append(fi)
        if 'w' in fi:
            w.append(fi)
        if 'x' in fi:
            x.append(fi)
        if 'y' in fi:
            y.append(fi)
        if 'z' in fi:
            z.append(fi)
file.close()
dic['a'] = a
dic['b'] = b
dic['c'] = c
dic['d'] = d
dic['e'] = e
dic['f'] = f
dic['g'] = g
dic['h'] = h
dic['i'] = i
dic['j'] = j
dic['k'] = k
dic['l'] = l
dic['m'] = m
dic['n'] = n
dic['o'] = o
dic['p'] = p
dic['q'] = q
dic['r'] = r
dic['s'] = s
dic['t'] = t
dic['u'] = u
dic['v'] = v
dic['w'] = w
dic['x'] = x
dic['y'] = y
dic['z'] = z

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in alphabet:
    file = open(letter + ".py", 'w')
    file.write(letter + " = " + str(dic[letter]))
    file.close    
