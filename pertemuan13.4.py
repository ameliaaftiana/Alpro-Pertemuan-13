def palindrome_perulangan(input_string): #true/false
    input_string = input_string.lower()
    reversed_input_string  = input_string[::-1]
    if input_string == reversed_input_string:
        return True
    else:
        return False

def palindrome_rekursif(input_string,depan,belakang):
    #base case jika karakter cuma 1
    if depan == belakang:
        if input_string[depan] == input_string[belakang]:
            return True
    #base case jika bersebelahan, karakter tinggal 2
    elif belakang == depan + 1:
        if input_string[depan] == input_string[belakang]:
            return True
        else:
            return False
    else:
        if input_string[depan] == input_string[belakang]:
            return palindrome_rekursif (input_string, depan+1, belakang-1)
        else:
            return False
    
kalimat = 'KasUr RuSak'
    
print (palindrome_perulangan('kasur rusak'))
print (palindrome_perulangan('praktikum alpro'))
print (palindrome_rekursif('kasur rusak',0,len('kasur rusak')-1))
print (palindrome_rekursif('prktikum alpro',0,len('prktikum alpro')-1))
print (palindrome_rekursif(kalimat.lower(),0,len(kalimat)-1))