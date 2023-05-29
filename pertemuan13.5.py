def fibo(n):
    f1,f2=1,1
    print (f1,", ",f2,", ",end='')
    for i in range (2,n):
        fib = f1+f2
        f1 = f2
        f2 = fib
    return fib

def fibo_rekursif(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_rekursif(n-1) + fibo_rekursif(n-2)
    

def fibo_rekursif_mem(n, lis_fibo):
    if n == 1 or n == 2:
        return 1
    else:
        if list_fibo[n-1] != 0:
            return list_fibo[n]
        else:
            list_fibo[n-1] = fibo_rekursif_mem(n-1, list_fibo) + \
                fibo_rekursif_mem(n-2, list_fibo)
            return fibo_rekursif_mem(n-1, list_fibo) + fibo_rekursif_mem(n-2, list_fibo)
    

hasil = fibo(10)
print (hasil)


hasill = fibo_rekursif(10)
print (hasill)


n  = 41
list_fibo = [0] * n 
hasil = fibo_rekursif_mem(n,list_fibo)
print (f'Fibo rekursif memorization: {hasil}')

hasil = fibo_rekursif(41)
print (f'Fibo rekursif biasa: {hasil}')

