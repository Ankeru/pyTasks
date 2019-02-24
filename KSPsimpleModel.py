
# Settings
StartMass = 2.44 #Начальная масса в тоннах 
MAXRashod = 15.821 #Максимальный расход топлива
MAXThrustATM = 162.909*1e3 # Максимальная тяга двигателя (1 атм) [Н]
MAXThrustVACCUUM = 192.909*1e3# Максимальная тяга двигателя (1 вакуум)[Н]
MAXFuel = 140       # Максимальное количетсво топлива[1]
FUELWeightPERED = 7.5 # Вес единицы топлива[кг]
KerbalRad = 600*1e3  #Радиус Кербина
KerbinMass = 5.292e22 #Масса кербина
KerbinSecondSpaceSpeed = 3431 #m/c
G = KerbalRad*KerbinSecondSpaceSpeed**2/(2.0*KerbinMass)  #Кербиновская гравитационная постоянная
Cf = 0.04 #Постоянная сопротивления воздуха конусовидного тела
S = 1.3 #Площадьпоперечного сечения ракеты



def getg(h):
    return G*KerbinMass/((KerbalRad+h)**2)

#На вход подаются метры
def approxRO(m):
    a = -1
    b = -1
    if m < 100 and m >= 0:
        a = 1.225
        b = 1.213
        dif = 100
        start = 0
    elif m < 200:
        a = 1.213
        b = 1.201
        dif = 100
        start = 100
    elif m < 300:
        a = 1.201
        b = 1.190
        dif = 100
        start = 200
    elif m < 400:
        a = 1.190
        b = 1.178
        dif = 100
        start = 300
    elif m < 500:
        a = 1.178
        b = 1.167
        dif = 100
        start = 400
    elif m < 1000:
        a = 1.167
        b = 1.111
        dif = 500
        start = 500
    elif m < 2000:
        a = 1.111
        b = 1.006
        dif = 1000
        start = 1000
    elif m < 3000:
        a = 1.006
        b = 0.909
        dif = 1000
        start = 2000
    elif m < 4000:
        a = 0.909
        b = 0.819
        dif = 1000
        start = 3000
    elif m < 5000:
        a = 0.819
        b = 0.736
        dif = 1000
        start = 4000
    elif m < 6000:
        a = 0.736
        b = 0.659
        dif = 1000
        start = 5000
    elif m < 7000:
        a = 0.659
        b = 0.589
        dif = 1000
        start = 6000
    elif m < 8000:
        a = 0.589
        b = 0.525
        dif = 1000
        start = 7000
    elif m < 9000:
        a = 0.525
        b = 0.466
        dif = 1000
        start = 8000
    elif m < 10000:
        a = 0.466
        b = 0.412
        dif = 1000
        start = 9000
    elif m < 11000:
        a = 0.412
        b = 0.363
        dif = 1000
        start = 10000
    elif m < 12000:
        a = 0.363
        b = 0.310
        dif = 1000
        start = 11000
    elif m < 13000:
        a = 0.310
        b = 0.260
        dif = 1000
        start = 12000
    elif m < 14000:
        a = 0.260
        b = 0.210
        dif = 1000
        start = 13000
    elif m < 15000:
        a = 0.210
        b = 0.160
        dif = 1000
        start = 14000
    elif m < 16000:
        a = 0.160
        b = 0.110
        dif = 1000
        start = 15000
    elif m < 17000:
        a = 0.110
        b = 0.60
        dif = 1000
        start = 16000
    elif m < 18000:
        a = 0.60
        b = 0.10
        dif = 1000
        start = 17000
    else:
        a = 0.05
        b = 0
        dif = 1
        start = 1
        m = 2
    if a == -1:
        print("ERRRRROR")    
    return a - (a - b)/dif*(m-start)  

#На вход подаются метры
def getFt(m, ogr, fuel):
    if fuel > 0: 
        return ogr*MAXThrustATM + ogr*(MAXThrustVACCUUM - MAXThrustATM)/(70000)*(m)
    else:
        return 0 
    
def getMassAndFuel(Mass, dt, rashod, fuel):
    if fuel > 0:
        if fuel - dt*rashod > 0:
            CurrentRashod = dt*rashod
        else:
            CurrentRashod = fuel
        return [Mass - CurrentRashod*FUELWeightPERED, fuel - CurrentRashod]
    else: 
        return [Mass, 0]

FUEL = 140 #Начальное количество топлива
OGRthrust = 1
V = 0
a = 0
dt = 0.001
Mass = StartMass*1e3
t = 0
h = 74

while t < 15 :
    # print("now",getFt(h, OGRthrust, FUEL), approxRO(h))
    a = ( getFt(h, OGRthrust, FUEL) - Mass*getg(h) - (Cf*approxRO(h)*(V**2)*S)/2.0 )/Mass
    V = V + a*dt 
    h = h + V*dt
    t = t + dt
    [Mass, FUEL] = getMassAndFuel(Mass, dt, MAXRashod, FUEL)
print(t, a,V, h,Mass,FUEL)
    

