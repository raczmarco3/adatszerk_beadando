
#gyorhatványozás
def gyorsh(a, b, m):
    d = {}
    i = 0
    ismnegyz = []

    #osztjuk a kitevőt 2-vel és eltároljuk az eredményt és a maradékot egy dictionarybe
    while(b != 0):
        egesz = b // 2
        maradek = b % 2
        b = egesz

        d[i] = [b, maradek]

        #ismételt négyzetre emelés
        ismnegyz.append((a ** (2 ** i)) % m)
        i = i + 1
    
    eredmeny = 1

    #az ismét négyzetre emelésből veszem azokat az értékeket, ahol a dictionarybe 1 a maradék (ugyanaz az indexük) 
    for k, v in d.items():
        if v[1] == 1:
            eredmeny = eredmeny * ismnegyz[k]

    return eredmeny % m

#Miller-Rabin prímteszt 
def miller_rabin(p, a):

    #Leellenőrizzük a p-t
    if(p % 2 == 0):
        return "A p-nek 3-nál nagyobb páratlan egésznek kell lennie!"
    else:
        d = p - 1
        s = 0
        #s és d meghatározása
        while(d % 2 == 0):
            d = int(d / 2)
            s = s + 1
   
        #a a d-ediken teszt
        if (a ** d) % p == 1:
            return str(p) +  " valószínűleg prím!"
        else:
            #a 2 az i-edking szer d tesztek

            sikeres = False
            i = 0
            while(i < s):
                if (a ** ((2 ** i) * d)) % p == p - 1:
                    sikeres = True
                i = i + 1
            
            if sikeres:
                return str(p) + " valószínűleg prím!"
            else:
                return str(p) + " összetett!"


def main(): 
    print(gyorsh(6, 73, 100))
    print(miller_rabin(561, 2))
    print(miller_rabin(73, 2))
    print(miller_rabin(97, 2))
    

main()