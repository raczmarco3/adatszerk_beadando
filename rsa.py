import random
import time
import Crypto.Util.number


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
            d = d // 2
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


x = 0
y = 0


def kib_eukildesz(a, b):
    global x, y
    l1 = [a, 0, 1, 0]
    l2 = [b, a // b, 0, 1]

    maradek = a % b   
    i = 2
    #táblázat feltöltése
    while(maradek > 0):
        l3 = []
        #a kettővel és az eggyel előző számokból kiszámoljuk a maradékot
        maradek = l1[0]%l2[0]
        #a +1-edik sor 0 maradék kiküszöbölése
        if(maradek > 0):
            egesz = l2[0] // maradek
        else:
            egesz = 0

        #a sor x és y értékeinek kiszámolása
        x = l2[2] * l2[1] + l1[2] 
        y = l2[3] * l2[1] + l1[3] 
        l3 = [maradek, egesz, x, y]
        #csak azt a 2 sort tartjuk meg mindig, amivel a következő sort számolni fogjuk
        l1 = l2
        l2 = l3
        i = i + 1

    #lépésszám meghatározása
    n = i - 2
    #x és y meghatározása
    x = (-1) ** n * l1[2]
    y = (-1) ** (n + 1) * l1[3]

    return y


q = 0
p = 0
d = 0
n = 0


def rsa_titkositas(m):
    global q
    global p
    global d
    global n
    #p és q legenerálása
    p = Crypto.Util.number.getPrime(1000)
    q = Crypto.Util.number.getPrime(1000)
    #p = 463
    #q = 547

    #print(p)
    #print()
    #print(q)

    #p és q ellenőrzése,ha megegyeznek akkor addig generálok q-t amíg nem különböznek
    if p == q:
        while(p == q):
            q = Crypto.Util.number.getPrime(1024)

    n = p * q
    #print("n: ",n)
    fn = (p - 1) * (q - 1)
    #e = 47
    e = 65537

    d = kib_eukildesz(fn, e)
    if d < 0:
        d = d % fn

    #print("d: ",d)

    titok = (m ** e) % n

    return titok


#gyorhatványozás
def gyorsh(a, b, m):
    eredmeny = 1
    a = a % m
    #osztjuk a kitevőt 2-vel
    while(b > 0):
        #ha a maradék 1 akkor ismételt négyzetre emelem és összeszorzom őket
        if b % 2 == 1:
            eredmeny = (eredmeny * a) % m

        b = b // 2   
        a = (a * a) % m     

    return eredmeny


def rsa_visszafejtes(c):
    #kiszámoljuk a dp-t és a dq-t d mod (p-1) és d mod (q-1)
    dp = d % (p - 1)
    dq = d % (q - 1)
    #a dp és qp értékek felhasználásával kiszámoljuk mp-t és a mq-t (a titkosított üzenetet dp és dq hatványra emeljük majd mod q és p)
    mp = gyorsh(c, dp, p)
    mq = gyorsh(c, dq, q)
    #eukilidészi algoritmussal kiszámoljuk az x-et és az y-t
    kib_eukildesz(p, q)
    #visszafejtjük a titkosított üzenetet
    m = (mp * y * q + mq * x * p) % n

    return m    


def main(): 
    #print(gyorsh(6, 73, 100))
    #print(miller_rabin(561, 2))
    #print(miller_rabin(73, 2))
    #print(miller_rabin(97, 2))
    #print("A d: értéke:",kib_eukildesz(402, 123))
    #print("A d: értéke:",kib_eukildesz(160, 47))
    m = rsa_titkositas(2)
    print("A titkosított üzenet: ", m)
    print(rsa_visszafejtes(m))
    

main()