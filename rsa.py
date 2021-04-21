import random
import time
import Crypto.Util.number


#gyorhatványozás
def gyorsh(a, b, m):
    i = 0
    eredmeny = 1

    #osztjuk a kitevőt 2-vel
    while(b != 0):
        maradek = b % 2
        b = b // 2
        
        #ha a maradék 1 akkor ismételt négyzetre emelem és összeszorzom őket
        if maradek == 1:
            eredmeny = (a ** (2 ** i) % m) * eredmeny
        i = i + 1

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
            return True
        else:
            #a 2 az i-ediken szer d tesztek
            sikeres = False
            i = 0

            while(i < s and not sikeres):
                if (a ** ((2 ** i) * d)) % p == p - 1:
                    sikeres = True
                i = i + 1
            
            if sikeres:
                return True
            else:
                return False


#Kibővített euklideszi algoritmus
def kib_eukildesz(a, b):
    d = {}
    #betesszük az a-t, a b-t és a x,y-t a táblázatba
    d[0] = [a, 0, 1, 0]
    d[1] = [b, a // b, 0, 1]
    
    maradek = a % b   
    i = 2
    #táblázat feltöltése
    while(maradek > 0):
        #a kettővel és az eggyel előző számokból kiszámoljuk a maradékot
        maradek = d[i-2][0]%d[i-1][0]
        #a +1-edik sor 0 maradék kiküszöbölése
        if(maradek > 0):
            egesz = d[i-1][0] // maradek
        else:
            egesz = 0
        x = d[i-1][2] * d[i-1][1] + d[i-2][2] 
        y = d[i-1][3] * d[i-1][1] + d[i-2][3] 
        d[i] = [maradek, egesz, x, y]
        i = i + 1
    
    #lépésszám meghatározása
    n = i - 2
    #utolsó nem 0 maradék
    r = d[n][0]

    #x és y meghatározása
    x = (-1) ** n * d[n][2]
    y = (-1) ** (n + 1) * d[n][3]

    #ellenőrzés
    #if r == a * x + b * y:
        #print("igaz")
    #else:
        #print("hamis")

    return y


def rsa_titkositas(m):
    
    #p és q legenerálása
    p = Crypto.Util.number.getPrime(1024)
    q = Crypto.Util.number.getPrime(1024)

    print(p)
    print(q)

    #p és q ellenőrzése,ha megegyeznek akkor addig generálok q-t amíg nem különböznek
    if p == q:
        while(p == q):
            q = Crypto.Util.number.getPrime(1024)

    n = p * q
    fn = (p - 1) * (q - 1)
    #e = 47
    e = 65537

    d = kib_eukildesz(fn, e)
    if d < 0:
        d = d % fn

    titok = (m ** e) % n

    return titok

def main(): 
    print(gyorsh(6, 73, 100))
    #print(miller_rabin(561, 2))
    #print(miller_rabin(73, 2))
    #print(miller_rabin(97, 2))
    #print("A d: értéke:",kib_eukildesz(402, 123))
    #print("A d: értéke:",kib_eukildesz(160, 47))
    #print(rsa_titkositas(2))

main()