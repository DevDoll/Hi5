import requests
import json
import os
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import random
import string



 #extracting account id
def getacc():
    try:
        alphanumiric = string.ascii_lowercase + string.digits
        did = ''.join(random.choice(alphanumiric) for i in range(16))
        aid = "".join([random.choice(alphanumiric) for i in range(8)])+"-"+"".join([random.choice(alphanumiric) for i in range(4)])+"-"+"".join([random.choice(alphanumiric) for i in range(4)])+"-"+"".join([random.choice(alphanumiric) for i in range(4)])+"-"+"".join([random.choice(alphanumiric) for i in range(12)])

        print('Using %s as a DeviceID and as AAID: %s' % (did, aid))

        url = 'https://secure.hi5.com/api/?method=tagged.login.login&application_id=user'
        headers = {'User-Agent': '%s'%useragent}
        obj = {'email': '%s@gmail.com'%email, 'password': 'NewPassword456', 'deviceId': '%s'%did, 'aaid': '%s'%aid}
        try:
            r = requests.post(url, data=obj, headers=headers, proxies=proxy)
            response = json.loads(r.text)
            print('Retrieving Account Info')
            print(response)
            results = response['result']
            working = response['stat']
            if working == 'fail':
                return False
            else:
                accid = results['user_id']
                autotoken = results['auto_token']
                session = results['session']
                mid = str(accid)
                return mid, autotoken, session
        except Exception as e: print(e)
    except:
        print('\nCant Login to the account, moving on\n')
        return False

def extractor(age):
    try:
        print(age)
        cookies = {'S': 'ev0fhabdvaaj8m8rrirqqlibmq'}
        headers = {'User-Agent': '%s'%useragent}
        r = requests.get('https://secure.hi5.com/api/?method=tagged.search.query&returns_users=true&show=25&language=-1&min_age=%s&max_age=%s&distance=750&location=USA&num_results=400&gender=%s&country=US&application_id=user'% (age, max, gender), cookies=cookies, headers=headers, proxies=proxy)
        users = json.loads(r.text)


        for result in users['results']:
            user = result['userId']
            usr = str(user)
            status = result['online']
            if status == True:
                outF = open("bot-users/%s-active-fresh-users.txt"%email, "a+")
                print('this user is online: %s'%user)
                print(user, file=outF)
                outF.close()

            elif status == False:
                a = 'user is offline'
            else:
                print('something went wrong with %s'%user)
    except:
        extractor(age)

 # Remove reached users
def rechecker():

    with open('users/%s-reached-users.txt'%niche, 'r+') as source:
        filter_lines = source.readlines()

    with open('bot-users/%s-active-fresh-users.txt'%email, 'r') as f:
        lines = f.readlines()

    with open('bot-users/%s-active-clean-users.txt'%email, 'w') as target:
        for line in lines:
            if line not in filter_lines:
                target.write(line)
    source.close()
    f.close()
    target.close()
    os.remove('bot-users/%s-active-fresh-users.txt'%email)
    actfile = open("bot-users/%s-active-clean-users.txt"%email, "r")
    line_count = 0
    for line in actfile:
        if line != "\n":
            line_count += 1
    actfile.close()
    print('%s fresh accounts was cleaned & are ready to be Cocked!' % line_count)



def sender():
    try:
        cookies = {'S': '%s'% session}
        headers = {'User-Agent': '%s'%useragent}
        r = requests.get('https://secure.hi5.com/api/?method=tagged.im.getConversation&size=s&size2=m&uid=%s&count=100&isPhotoCommentSupported=true&application_id=user'%usrid, cookies=cookies, headers=headers, proxies=proxy)
        reply = json.loads(r.text)

        replys = reply['result']
        container = replys['items']
        count = 0
        for result in container:
            user = result['uid']
            uids = str(user)
            if uids == myid:
                count +=1

        if count == 0:
            try:
                print("trying to send the first message to: %s"%usrid)
                objec = {'uid': '%s'%usrid, 'message': '%s'% keywords, 'type': '1'}
                send = requests.post('https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user', data=objec, headers=headers, cookies=cookies, proxies=proxy)
                fmsg = json.loads(send.text)
                results = fmsg['result']

                if "code" not in results:
                    print(fmsg)
                    print('Message Sent!\n')
                    outf = open("%s/%s-reached-users.txt"%(DropboxFolder,niche), "a")
                    time.sleep(5)
                    #outi = open('bot-users/%s-reached-users.txt' % email, 'a')
                    outf.write(usrid)
                    #outi.write(usrid)
                    outf.close()
                    #outi.close()
                elif "code" in results:
                    code_num = results['code']
                    print(fmsg)
                    if code_num == 25:
                        print('\nThe account have reached the maximum messages sent... Replying to messages & Moving to the next account\n')
                        return False
                    else:
                        print('message didnt arrive, skipping to the next user...')
            except Exception as e: print(e)

        elif count > 0:
            print('Message has already been sent previously to %s'%usrid)
            outf = open("users/reached-users.txt", "a")
            outf.write(usrid)
            outf.close()
    except Exception as e: print(e)

# Generating a proxy
def get_proxies(ua):
    proxies = []
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')

    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

  # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
                        'ip':   row.find_all('td')[0].string,
                        'port': row.find_all('td')[1].string})
    return proxies

def random_proxy(proxies):
  return random.choice(proxies)



# collecting inputs:

#type = input('(S)olo or (D)uo')    #for

osystem = input('(W)indows Or (L)inux Or (M)ac: ')
devicename = input('%s PC name: ')

gender = input('do you want them (F)emale or (M)ale:  ')
uaf = open('config/user-agents.txt', 'r').read().splitlines()
messn = int(input('how many messages do you wanna send with each account:  '))
col = int(input('how many minutes between every %s messages:  '%messn)) * 60
niche = input('What niche will you use: ')
times = int(input('how many times do you wanna repeat the messages:  '))
entimes = times - 1
cooldwn = int(input('How many minutes between each account:  ')) * 60

# adding backround touches
if osystem == 'W':
    DropboxFolder = 'C:/Users/%s/Dropbox'%devicename
elif osystem == 'L':
    DropboxFolder = '/home/%s/Dropbox'%devicename
if osystem == 'M':
    DropboxFolder = '/Users/%s/Dropbox'%devicename


#t_end = time.time() + 60 * period
s_time = time.time()





# Working to get the email:
emaillist = list()
with open('accounts/hi5acc.txt', 'r') as efile:
    for emailuser in efile:
        email = emailuser.rstrip()
        emaillist.append(email)

start_time = time.time() / 60

for email in emaillist:
    Repeat = 0
    while Repeat < times:

        #Getting Proxy
        # ua = UserAgent()
        # proxies = get_proxies(ua)
        proxy = []

        # prostr = str(nproxy)
        # ip = prostr.split(',')[0]
        # port = prostr.split(',')[1]
        # ipa = ip.split(':')[1]
        # porta = port.split(':')[1]
        # fport = porta.replace('}', '')
        #
        # ips = ipa.replace("'", "")
        # ports = fport.replace("'", "")
        # pip = ips.replace(" ", "")
        # pport = ports.replace(" ", "")

        # proxy = {
        #     "http": "http://%s:%s" % (pip, pport),
        #     "https": "http://%s:%s" % (pip, pport),
        # }

        # proxy = {
        #     "http": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
        #     "https": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
        # }


        print('\nLogged in as: %s@gmail.com'%email)
        # Declaring Variables
        useragent = random.choice(uaf)
        stats = getacc()
        if stats is not False:
            try:
                myid, token, session = getacc()

                #scrapper
                print('Scrapping Active Users...\n')
                agelist = list()
                with open("config/age.txt", "r") as file:
                    for line in file:
                        age = line
                        agelist.append((age))

                for age in agelist:
                    max = age
                    extractor(age)

                #Plugin for Keep on tracking niche reach & to keep on growing it:
                time.sleep(5)
                rechecker()

                #sending the first messages:
                print('\nThrowing Clean accounts to the grill...\n')
                usrlist = list()
                with open("bot-users/%s-active-clean-users.txt"%email, "r") as usrfile:
                    for line in usrfile:
                        usrid = line
                        usrlist.append((usrid))

                    st = 0
                    for usrid in usrlist:
                        usrid = usrid

                        msglines = open('messages/%s-opening.txt'%niche).read().splitlines()
                        keywords = random.choice(msglines)

                        if st < messn:
                            time.sleep(2)
                            limit = sender()
                            if limit is not False:
                                print('message %s has been sent' % st)
                                st +=1
                            else:
                                break

                        else:
                            break
                Repeat += 1
                print('Reapeating for the %s time'%Repeat)

                entime = time.time() - start_time * 60
                frontlinedone = entime / 60
                print('an account completed in %s Minutes' % frontlinedone)
                sleeping = col / 60
                print('Sleeping for %s Minutes' % sleeping)
                if Repeat == times:
                    break
                else:
                    time.sleep(col)

            except:
                print('\nCould Not login to the account...Moving On\n')
                break

        else:
            blcktime = s_time - time.time()
            btime = blcktime / 60
            print('Account has been blocked after %s Minutes from Launch' % btime)
            break
    accchk = getacc()
    if accchk is not False:
        cooldwnm = cooldwn / 60
        print('account done sleeping for %s minutes'%cooldwnm)
        time.sleep(cooldwn)
    else:
        Repeat =+ 100
        print('Previous account is blocked: %s'%email)





sec = time.time() - s_time
minu = sec / 60
print("\n\nThe bot finished within %s minutes" % minu)
