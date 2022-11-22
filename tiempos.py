def conversion_tiempo(h,m,s):
    hs = h*60*60
    ms = m*60
    tt = hs+ms+s
    return tt


h = 4
m = 44
s = 46
tt = conversion_tiempo(h,m,s)
h1 = 8
m1 = 41
s1 = 24
tt1 = conversion_tiempo(h1,m1,s1)
print(tt-tt1)



    
