import requests
import json
import random
import time
import string


# extracting account id

def getacc():
    try:
        alphanumiric = string.ascii_lowercase + string.digits
        did = ''.join(random.choice(alphanumiric) for i in range(16))
        aid = "".join([random.choice(alphanumiric) for i in range(8)]) + "-" + "".join(
            [random.choice(alphanumiric) for i in range(4)]) + "-" + "".join(
            [random.choice(alphanumiric) for i in range(4)]) + "-" + "".join(
            [random.choice(alphanumiric) for i in range(4)]) + "-" + "".join(
            [random.choice(alphanumiric) for i in range(12)])

        print('Using %s as a DeviceID and as AAID: %s' % (did, aid))

        url = 'https://secure.hi5.com/api/?method=tagged.login.login&application_id=user'
        headers = {
            'User-Agent': 'hi5/9.30.1 (SPA Condor Electronics TFX-708G; Android 4.4.2; Android/TFX-708G/TFX-708G:4.4.2/KOT49H/1445414608:user/release-keys)'}
        obj = {'email': '%s@gmail.com' % email, 'password': 'NewPassword456', 'deviceId': '%s' % did,
               'aaid': '%s' % aid}
        try:
            r = requests.post(url, data=obj, headers=headers, proxies=proxy)
            response = json.loads(r.text)
            print('Retrieving Account Info for %s' % email)
            print(response)
            stats = response['stat']
            if stats == 'fail':
                return False
            else:
                results = response['result']
                accid = results['user_id']
                autotoken = results['auto_token']
                session = results['session']
                mid = str(accid)
                return mid, autotoken, session
        except Exception as e:
            print(e)
    except:
        print('\nCant Login to the account, moving on\n')
        return False


# Replying to users function
def replier():
    cookies = {'S': '%s' % session}
    headers = {'User-Agent': '%s' % useragent}
    inburl = 'https://secure.hi5.com/api/?method=tagged.im.getInbox&size=s&size2=m&count=20&filter=new&isPhotoCommentSupported=true&application_id=user'
    inb = requests.get(inburl, headers=headers, cookies=cookies, proxies=proxy)
    inbox = json.loads(inb.text)
    print(inbox)
    results = inbox['result']
    usrs = results['items']
    linklimit = 0

    for item in usrs:
        uid = item['uid']
        lastsender = item['lastUidInConv']

        if lastsender == uid:
            print('user has sent a message, checking the conversation...')
            convurl = 'https://secure.hi5.com/api/?method=tagged.im.getConversation&size=s&size2=m&uid=%s&count=25&isPhotoCommentSupported=true&application_id=user' % uid
            rq = requests.get(convurl, cookies=cookies, headers=headers, proxies=proxy)
            rep = json.loads(rq.text)
            print(rep)
            res = rep['result']
            it = res['items']

            count = 0
            counth = 0
            for resu in it:
                uuid = str(resu['uid'])
                umsg = resu['html']
                print('\nuser last message was: %s'%umsg)
                if uuid == myid:
                    count += 1
                else:
                    counth += 1
            print('user %s have RECEIVED: %s messages & SENT: %s messages' % (uid, count, counth))
            surl = 'https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user'

            if count == 1 and counth >= 1:
                # Chossing messages
                randdomain = random.choice(domainnames)
                randext = random.choice(ext)
                blk = '%s %s' % (randdomain, randext)
                second = random.choice(secondreply)

                if linklimit < linkperround:
                    # marking the message as read
                    rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                    rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                    markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy)
                    json.loads(markread.text)
                    print('user message has be unread')

                    # # getting responses
                    print('\nuser replied to the first message, Sending the Landing Page...\n')

                    one = {'uid': '%s' % uid, 'message': '%s' % second, 'type': '1'}
                    send1 = requests.post(surl, data=one, headers=headers, cookies=cookies, proxies=proxy)
                    se1 = json.loads(send1.text)
                    print(se1)
                    linklimit = + 1
                    print('worm message has been sent')

                    blcav = {'uid': '%s' % uid, 'message': '%s' % blk, 'type': '1'}
                    send11 = requests.post(surl, data=blcav, headers=headers, cookies=cookies, proxies=proxy)
                    se11 = json.loads(send11.text)
                    print(se11)
                    print('blocking avoid message has been sent')

                    # three = {'uid': '%s' % uid, 'message': '%s' % conf, 'type': '1'}
                    # send3 = requests.post(surl, data=three, headers=headers, cookies=cookies)
                    # se3 = json.loads(send3.text)
                    # print(se3)
                    #
                    #
                    # time.sleep(random.uniform(1, 3))
                    # lppb = {'uid': '%s' % uid, 'message': '%s' % gif, 'type': '9'}
                    # sendlp = requests.post(surl, data=lppb, headers=headers, cookies=cookies)
                    # selp = json.loads(sendlp.text)
                    # print(selp)
                    # print('Gif has been sent')

                    # imgurl = 'https://secure.hi5.com/api/?method=tagged.im.sendPhotoFromUpload&uid=%s&application_id=user' % uid
                    # sendimg = requests.post(imgurl, files=files, headers=headers, cookies=cookies)
                    # print(sendimg)
                    # seni = json.loads(sendimg.text)
                    # print(seni)
                    # time.sleep(random.uniform(2, 2))

                    print('USER %s Have Been Coocked =D' % uid)

                    outF = open("users/engaged-users.txt", "a")
                    usid = str('\n%s' % uid)
                    outF.write(usid)
                    print('user %s has been added to the engaged list' % uid)
                    outF.close()
                else:
                    print('Skiping User in order to keep it %s link per hour'%linkcount)


            elif count == 2 and counth >= 2:
                # getting response
                third = random.choice(thirdreplys)

                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy)
                json.loads(markread.text)
                print('user message has be unread')

                tow = {'uid': '%s' % uid, 'message': '%s' % third, 'type': '1'}
                send2 = requests.post(surl, data=tow, headers=headers, cookies=cookies, proxies=proxy)
                se2 = json.loads(send2.text)
                print(se2)
                print('Flirting with user...')


            elif count == 3 and counth >= 2:
                # getting response
                forth = random.choice(forthreplys)

                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy)
                json.loads(markread.text)
                print('user message has be unread')

                print('Asking the user again to confirm Higher the impressions...')
                url = 'https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user'
                one = {'uid': '%s' % uid, 'message': '%s' % forth, 'type': '1'}
                send1 = requests.post(url, data=one, headers=headers, cookies=cookies)
                json.loads(send1.text)
            elif count == 4 and counth >= 3:
                # getting response
                fifth = random.choice(fifthreplys)

                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy)
                json.loads(markread.text)
                print('user message has be unread')

                print('Asking the user to follow the instructions...')
                url = 'https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user'
                one = {'uid': '%s' % uid, 'message': '%s' % fifth, 'type': '1'}
                send1 = requests.post(url, data=one, headers=headers, cookies=cookies)
                json.loads(send1.text)
            elif count == 5 and counth >=4:
                # getting response
                sisxth = random.choice(sixthreplys)

                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy)
                json.loads(markread.text)
                print('user message has be unread')

                print('Retreating from the user...')
                url = 'https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user'
                one = {'uid': '%s' % uid, 'message': '%s'%sisxth, 'type': '1'}
                send1 = requests.post(url, data=one, headers=headers, cookies=cookies)
                json.loads(send1.text)


            elif count == 1 and counth == 0:
                # #marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy)
                json.loads(markread.text)
                print('user message has be unread')
                print('user received the first message but he didnt reply')


            elif count == 0 and counth >= 1:
                print('a user sent the first message, unreading him...')
                # #marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy)
                json.loads(markread.text)
                print('user message has be unread')


        elif lastsender == myid:
            print('user didnt reply yet')


# collecting inputs:
uaf = open('config/user-agents.txt', 'r').read().splitlines()
# period = int(input('For how many minutes do you want to the Bot to run:  '))
cool = int(input('How many minutes between each Inbox Check for each account: ')) * 60
times = int(input('how many times do you wanna repeat: '))
wrkngtime = cool * times
linkcount = int(input('how many links do you wanna send in each %s hours: '%wrkngtime))
cooldwn = int(input('How many minutes between every account:  ')) * 60
niche = input('What Niche You wanna launch? Make sure the 6 replys are ready: ')

linkperround = linkcount / times

domainnames = open('messages/%sdomains.txt'%niche).read().splitlines()
ext = open('messages/%s-domain-extention.txt'%niche, 'r').read().splitlines()
secondreply = open('messages/%s-2nd-reply.txt'%niche, 'r').read().splitlines()
thirdreplys = open('messages/%s-3rd-reply.txt'%niche, 'r').read().splitlines()
forthreplys = open('messages/%s-4th-reply.txt'%niche, 'r').read().splitlines()
fifthreplys = open('messages/%s-5th-reply.txt'%niche, 'r').read().splitlines()
sixthreplys = open('messages/%s-6th-reply.txt'%niche, 'r').read().splitlines()

# t_end = time.time() + 60 * period
s_time = time.time()

# while time.time() < t_end:


# Working to get the email:
emaillist = list()
with open('accounts/hi5acc.txt', 'r') as efile:
    for emailuser in efile:
        email = emailuser.rstrip()
        emaillist.append(email)

start_time = time.time()

for email in emaillist:

    Repeat = 0
    proxy = []

    while Repeat < times:

        acctchk = getacc()
        if acctchk is not False:
            sleeping = cool / 60
            print('Sleeping for %s Minutes' % sleeping)
            time.sleep(cool)
        else:
            break
        print('\nTrying To Login as: %s@gmail.com\n' % email)
        # Declaring Variables
        # proxy = {
        #     "http": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
        #     "https": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
        # }

        useragent = random.choice(uaf)
        stats = getacc()
        if stats is not False:
            try:
                myid, token, session = getacc()

                print('Replying to all users...')
                rwave = time.time()
                try:
                    time.sleep(2)
                    replier()
                except:
                    replier()
                rdone = time.time() - rwave
                rtime = rdone / 60
                print("\nOne reply wave took %s minutes\n" % rtime)
                Repeat += 1
                print('repeating for the %s time...' % Repeat)
            except:
                print('\naccount Blocked Moving on...\n')
                break

        else:
            blcktime = time.time() - s_time
            btime = blcktime / 60
            print('Account has been blocked after %s Minutes from Launch' % btime)
            break

    accchk = getacc()
    if accchk is not False:
        print('account done sleeping for %s minutes' % cooldwn)
        time.sleep(cooldwn)
        print('Account Done, Pulling up another one...')
    else:
        Repeat += 100
end_time = time.time() - s_time
minu = end_time / 60
print("The Script have finished withCant Login to the account, moving onin %s minutes" % minu)
