

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
    if(p % 2 == 0 or p < 4):
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


#Kibővített euklideszi algoritmus
def kib_eukildesz(a, b):
    d = {}
    #betesszük az a-t, a b-t és a x,y-t a táblázatba
    d[0] = [a, 0, 1, 0]
    d[1] = [b, int(a/b), 0, 1]
    
    maradek = a % b   
    i = 2
    #táblázat feltöltése
    while(maradek > 0):
        maradek = d[i-2][0]%d[i-1][0]
        #a +1-edik sor 0 maradék kiküszöbölése
        if(maradek > 0):
            egesz = int(d[i-1][0]/maradek)
        else:
            egesz = 0
        x = d[i-1][2] * d[i-1][1] + d[i-2][2] 
        y = d[i-1][3] * d[i-1][1] + d[i-2][3] 
        d[i] = [maradek, egesz, x, y]
        i = i + 1
    
    n = i - 2
    r = d[n][0]
    x = (-1) ** n * d[n][2]
    y = (-1) ** (n + 1) * d[n][3]

    #ellenőrzés
    #if r == a * x + b * y:
        #print("igaz")
    #else:
        #print("hamis")

    return y


def main(): 
    #print(gyorsh(6, 73, 100))
    #print(miller_rabin(561, 2))
    #print(miller_rabin(73, 2))
    #print(miller_rabin(97, 2))
    print("A d: értéke:",kib_eukildesz(402, 123))
    print("A d: értéke:",kib_eukildesz(160, 47))

main()