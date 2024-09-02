""" Sin usar la computadora, analice los siguientes programas e indique cuál es la salida de cada uno de ellos.
A continuación, compruebe sus respuestas ingresando los programas a la computadora. """ 

#Digo que s=9 y t=3
"""
s = 0
t = 0
for i in range(3):
    for j in range(3):
        s = s + 1
        if i < j:
            t = t + 1
    print(t)
    print(s)"""
#--------------------------------------------------------------------
#Digo que s=9 y t=2
"""
s = 0
t = 0
for i in range(3):
    for j in range(3):
        s = s + 1
    if i < j:
        t = t + 1
        print(t)
print(s)"""
#-----------------------------------------------------------------------
"""
s = 0
t = 0
for i in range(3):
    for j in range(3):
        s = s + 1
if i < j:
    t = t + 1
    print(t)
print(s)"""
#-----------------------------------------------------------------------
"""
j = 2  
c = 1
p = True
i = 0
while j > 0:
    j = j - c
    if p:
        c = c + 1
    p = not p
    print(p)
print(j < 0 and p)"""
#--------------------------------------------------------------------------
"""
a = 10
c = 1
x = 0
y = x + 1
z = y
while z <= y:       #(1=1)(2=2)(FALSE)
    z = z + c       #(z=2)(z=3)
    y = 2 * x + z   #(y=1)(y=1)
    if y < 4:       #(true)(true)
        y = y + 1   #(y=2)(y=2)
    x = x - 1       #(x=-1)(x=-2)
print(x, y, z)"""   #(-2 2 3)
#--------------------------------------------------------------------------
"""
a = 11
b = a / 3
c = a / 2
n = 0
while a == b + c:       #(False)
    n += 1              
    b += c              
    c = b - c           
    if n % 2 == 0:      
        a = 2 * a - 3   
    print(100 * b + c)  """
#--------------------------------------------------------------------------
a = True
b = '1'
c = 2
print(b[-1])
while b[-1] not in '378':   # (true)
    a = 0 == len(b) % 2     # (a = False)
    if a:                   # (no)
        c = c * 7           # (no)
    b = b + str(c)          # (b=)
print (c)                   #
