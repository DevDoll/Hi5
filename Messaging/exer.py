import requests
import json
import random
import time
import webbrowser

# s = "603080264561069263587383447026613005569961397288466060996758613777716261278055446125583019738219314161281045296129135319612509630061297995456130187731612992052861304402826129814613741645464461357682016135953030610221100661357682017410546423613240198161281228536128443885741070584761282680086131763439"# test string
# import re
# print(re.sub("(.{10})", "\\1\n", s, 0, re.DOTALL))

# def picup():
#    fcookie = {'S': 'gsjfpcn10vruja2ktlqr5sjrch', 'B': 'b=60C2127F69582CED&remember_me=1', 'L': '2qN7X7N9qv3L.1vMmFK.5JO-X_'}
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'X-Requested-With': 'XMLHttpRequest'}
#
#    try:
#       # Upload Pictures
#       picurls = open('piclinks.txt', 'r').read().splitlines()
#       picurl = random.choice(picurls)
#       print(picurl)
#       purl = 'https://www.hi5.com/api/?application_id=user&format=JSON'
#       print('Uploading Picture from url')
#       odara = {'method': 'tagged.photo.urlUpload', 'url': '%s' % picurl, 'make_large_thumb': 'true',
#                'full_path_size': 'p', 'image_type': 'P', 'album_id': '0'}
#       upic = requests.post(purl, data=odara, cookies=fcookie, headers=headers)
#       resu = json.loads(upic.text)
#       print(resu)
#       results = resu['result']
#       picid = results['id']
#       print('Photo id is %s' % picid)
#       time.sleep(2)
#       print('setting the picture primary')
#       pdara = {'method': 'tagged.photo.setPrimary', 'photo_id': '%s' % picid}
#       sepic = requests.post(purl, data=pdara, cookies=fcookie, headers=headers)
#       print(sepic)
#    except Exception as e: print(e)
#
# print('started...')
# picup()

def extractor(age):
    try:
        print(age)
        cookies = {'S': 'ev0fhabdvaaj8m8rrirqqlibmq'}
        headers = {'User-Agent': '%s'%useragent}
        r = requests.get('https://secure.hi5.com/api/?method=tagged.search.query&returns_users=true&show=25&language=-1&min_age=%s&max_age=%s&distance=750&location=USA&num_results=400&gender=%s&country=US&application_id=user'% (age, max, gender), cookies=cookies, headers=headers)
        users = json.loads(r.text)


        for result in users['results']:

            user = result['userId']
            usr = str(user)
            status = result['online']
            if status == True:
                print('this user is online: %s'%user)
                onage.add(user)

            elif status == False:
                a = 'user is offline'
            else:
                print('something went wrong with %s'%user)

    except:
        extractor(age)

gender = 'F'
uaf = open('config/user-agents.txt', 'r').read().splitlines()
useragent = random.choice(uaf)
rep = int(input('How many times do you wanna repeat every age:  '))

#code:
agelist = list()
with open("config/age.txt", "r") as file:
    for line in file:
        age = line
        agelist.append((age))

started_on = time.time()
onage = set()
strep = 0
while strep < rep:
    for age in agelist:
        max = age
        extractor(age)
        strep +=1

onusers = len(onage)
endedon = time.time() - started_on
end_in_minutes = endedon / 60
print('%s online Users were scrapped in %s'%(onusers, end_in_minutes))
