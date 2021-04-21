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


def kib_eukildesz(a, b):
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

def rsa_titkositas(m):
    
    #p és q legenerálása
    p = Crypto.Util.number.getPrime(1024)
    q = Crypto.Util.number.getPrime(1024)

    print(p)
    print()
    print(q)

    #p és q ellenőrzése,ha megegyeznek akkor addig generálok q-t amíg nem különböznek
    if p == q:
        while(p == q):
            q = Crypto.Util.number.getPrime(1024)

    n = p * q
    print("n: ",n)
    fn = (p - 1) * (q - 1)
    #e = 47
    e = 65537

    d = kib_eukildesz(fn, e)
    if d < 0:
        d = d % fn

    print("d: ",d)

    titok = (m ** e) % n

    return titok

def main(): 
    #print(gyorsh(6, 73, 100))
    #print(miller_rabin(561, 2))
    #print(miller_rabin(73, 2))
    #print(miller_rabin(97, 2))
    #print("A d: értéke:",kib_eukildesz(402, 123))
    #print("A d: értéke:",kib_eukildesz(160, 47))
    #print(rsa_titkositas(2))
    print(gyorsh(16019801854629646850213025387985384644260818027240531715610995674368591678616758092361803771146187572857734593354048397753774580734589717287195098000940524006219045492803392555335976663145317569212409948650701220444381937278805270943424357782965156231895050762622648788409353511122033484903016462397603348333667728448256733672593626784455238416426404462072330271265692071508945036719880315762035985429653470318870706149570263287590408425043233583351323590430724456569743098921307132438226881954511869140207158613858642741893912865481235678571287180588832027823042091033736765515473252213175553011396955212698295295863,4154515950513877727681699834821303784405531261117285118614451278029351679875776749941798505519690322246337497357442537474140509577641027696942679264312178886074417383388907460359618744223676611755356305893820030062015364476890616307822386859325766545869421206362693867579302775400269794378198259197858928190851889660961640967442781190873040306040875042161598956233208277766394838751470788071797728185342283681494471671944032580161931363664451151977800613859186414564560894117801123306086334611123462427798434748381987691643910362067414143384128859619260979273633426414456117284531847449081457192796524434732715315825,16154889750138127722740925719395027062927809556179157162610376967379234665006454305264960760427432339448096627762828502340260269146188443821913633021551398342035071321654137191740140835421092565836643302442345040356847095153790217216432643147005622529764106894588339147949730983232910971529843319867691976791757426284118206819769771068255790870566898798409371200124904639464157810427921677329144050423711171663821981048519200854892654807263468211290999376316248728945378548671522598815348130617164518972560928144693513692748455990255315394745071369939032198745272490307946436839757665685261367239468224512505515863467))

main()