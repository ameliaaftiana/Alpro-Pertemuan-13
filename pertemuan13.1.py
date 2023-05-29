def hellon(n):
    for i in range(n):
        print ('Hello World')
    
def hello(n):
    if n == 0: #base n = 0 
        # print ('end')
        return '' #exit dari fungsi
    else : 
        print ('Hello World') #print sekali
        return hello (n-1) #atau bisa langsung tanpa menggunakan return (hello(n-1))

hellon(5)
hello (5)

