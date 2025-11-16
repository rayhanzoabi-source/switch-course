def foo(a, b, c):
    return a + b + c


def boo(a, c):
    d = c + 2
    x = foo(a, c, d)
    return x - d


def goo(x):
    y = boo(x, 3)
    return y + foo(y, y, y)


def moo(n, k):
    return goo(n) + too(k)


def too(j):
    return j * 2


def zoo(z):
    return too(z)


def noo(a,b):
    if boo(a,b) * 3.7 > 5887:
        return moo(4, koo(b))
    
    return boo(a,b) + 4.66


def koo(d):
    f = zoo(d) * 5.3
    return f * 1.2

def roo(x):
    if koo(x) > 2:
        x += 1
    if x/24 < 20:
        x += 1
    if goo(x) < 30:
        x += 1
    if boo(x, 44) > 30:
        x += 1
    if noo(x, 3.9) < 30:
        x += 1
    return x


r = goo(5)
w = r + too(3) + zoo(r) + boo(r, too(712)) 
q = foo(r, w, 4) + koo(34) + noo(w,r)
c = roo(r + q / 4)

'''
Answer the following questions using the debbuger.
Rule: you are not allowed to change the code!!
'''

