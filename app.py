from requests import get
import math
adresses = [
    'Екатеринбург,+Вайнера+улица,+дом+16',
    'Екатеринбург,+Малышева+улица,+дом+53',
    'Екатеринбург,+Малышева+улица,+дом+5',
    'Екатеринбург,+Татищева+улица,+дом+69',
    'Екатеринбург,+Карла Либкнехта+улица,+дом+22',
    'Екатеринбург,+Техническая+улица,+дом+37'
]
stages = [3, 8, 9, 1, 7, 2]
coord = []
for i in adresses:
    resp = get('https://geocode-maps.yandex.ru/1.x/?format=json&apikey=2eee079d-b1b7-44e7-a077-a516da1fe36d&geocode='+i)
    st = resp.json()
    s = st['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    s= s.split(' ')
    s= (float(s[0]), float(s[1]))
    coord.append(s)
    
coord = sorted(coord, key=lambda x: x[0])
distances = []
r = 6372795
for i in range(0, len(coord)):
    for j in range(i+1, len(coord)):
        delta2 = abs(coord[i][1] - coord[j][1])
        delta2 = delta2 * math.pi / 180
        a1 = math.sin(delta2 / 2)**2
        c1 = 2 * math.atan2(math.sqrt(a1), math.sqrt(1-a1))
        latdist1 = c1 * r
        distances.append(abs(latdist1))
    
for i in range(0, len(coord) -1):
    delta1 = abs(coord[i][0] - coord[-1][0])
    delta1 = delta1 * math.pi / 180
    a = math.sin(delta1 / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    latdist = c * r
    distances.append(latdist)
result = sum(distances)
for i in stages:
    result += i *3 * 2
print(result / 1000)
        
