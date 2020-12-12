from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as chop
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random
import string
import requests
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    passwor = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return passwor


def fixaccount(sess):
    names = open('mnames.txt', 'r').read().splitlines()
    disname = random.choice(names)

    print('Creating an account with %s which will be Named %s '% (email, disname))
    url = 'https://secure.hi5.com/register.html?src=index_email&page=register&loc=fr_FR'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'Referer': 'https://secure.hi5.com/register.html?err=1020'}
    coockies = {'S': '%s'% sess}
    obj = {'displayName': '%s'% disname, 'email': '%s'% email, 'password': 'NewPassword456', 'passwordStr': '1607268001%3ARCGYBM03Sg', 'city': 'Ville', 'gender': 'M', 'birthMonth': '9', 'birthDay': '21', 'birthYear': '1998', 'zipCode': '10006', 'country': 'US'}
    r = requests.post(url, data=obj, headers=headers, cookies=coockies, proxies=proxy)
    print(r.text)

    print('account updated successfully...')

# def readying():
#     url = 'https://secure.hi5.com/register.html?src=index_email&page=register&loc=fr_FR'
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}
#     coockies = {'S': '%s' % sess}
#     obj = {'displayName': '%s'%disname, 'gender': 'M', 'birthdate_month': '09', 'birthdate_day': '21', 'birthdate_year': '1998', 'zipCode': '10006', 'country': 'US', 'show_my_location': 'S', 'tagline': 'Come, lets chat', 'language_1': 'en_US', 'language_2': '-1', 'language_3': '-1', 'ethnicity_asian': 'false', 'ethnicity_east_indian': 'false', 'ethnicity_native_american': 'true', 'ethnicity_african_american': 'false', 'ethnicity_hispanic_latino': 'false', 'ethnicity_pacific_islander': 'false', 'ethnicity_caucasian': 'false', 'ethnicity_middle_eastern': 'false', 'ethnicity_other': 'false', 'show_my_ethnicity': 'S', 'religion': 'C', 'show_my_religion': 'S', 'orientation': 'S', 'show_my_orientation': 'S', 'relationship_status': 'D'}
#     r = requests.post(url, data=obj, headers=headers, cookies=coockies)
#     response = json.loads(r.text)
#     print(response)
#     print('account updated successfully...')


def login(email, password, recovmail):
    print('starting login function')
    FIPATH = geckopath
    #PATH = "C:/Users/hadji/chromedriver.exe"
    options = Options()
    # prox = Proxy({
    #     'proxyType': ProxyType.MANUAL,
    #     'httpProxy': proxy,
    #     'ftpProxy': proxy,
    #     'sslProxy': proxy,
    #     'noProxy': ''  # set this value as desired
    # })
    uag = open('WUserAgents.txt').read().splitlines()
    uar = random.choice(uag)
    print(uar)
    #useragent = UserAgent()
    #uar = random.choice(useragent)
    options.headless = False
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", uar)
    # profile.set_preference("network.proxy.type", 1)
    # profile.set_preference("network.proxy.http", '110.232.86.52')
    # profile.set_preference("network.proxy.http_port", 53281)

    Browser_one = webdriver.Firefox(executable_path=FIPATH, firefox_profile=profile, options=options)
    #Browser_one = webdriver.Chrome(executable_path=PATH)
    Browser_one.implicitly_wait(30)
    Browser_one.set_window_size(1024, 690)
    #print('Redirecting to google login page')

    Browser_one.get("https://accounts.google.com/o/oauth2/auth/identifier?response_type=permission id_token code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcontacts.readonly&openid.realm&include_granted_scopes=true&redirect_uri=storagerelay%3A%2F%2Fhttps%2Fsecure.hi5.com%3Fid%3Dauth761688&client_id=1034081759906-qmctkoa6acasj44mr28353f7m5qfnj2q.apps.googleusercontent.com&ss_domain=https%3A%2F%2Fsecure.hi5.com&gsiwebsdk=shim&access_type=offline&flowName=GeneralOAuthFlow")
    #Browser_one.get('https://www.whatismyip-address.com/?check')

    em = "%s" % email
    pa = "%s" % password
    rc = '%s' % recovmail
    try:

        print("Typing email address...")
        try:
            emailinput = Browser_one.find_element_by_id("identifierId")
        except:
            emailinput = Browser_one.find_element_by_id("Email")

        for character in em:
            emailinput.send_keys(character)
            time.sleep(random.uniform(0.1, 0.3))
        time.sleep(random.uniform(1, 1.5))
        emailinput.send_keys(Keys.RETURN)
        #time.sleep(1000)
        time.sleep(random.uniform(1, 1.5))
        print("typing Password...")
        time.sleep(random.uniform(1, 1.5))
        passwordinput = Browser_one.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
        time.sleep(random.uniform(1, 1.5))
        for character in pa:
            passwordinput.send_keys(character)
            time.sleep(random.uniform(0.05, 0.1))
        time.sleep(random.uniform(1, 1.5))
        passwordinput.send_keys(Keys.RETURN)

        # try:
        #     #print("Typing Recovery email...")
        #     # #time.sleep(1000)
        #     # Browser_one.find_element_by_xpath("//div[contains(@id, 'view_container')]")
        #     # print('stxpath click')
        #     # recoveminput = Browser_one.find_element_by_xpath("//html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]")
        #     # recoveminput.click()
        #     # print('clicked')
        #     #
        #     # time.sleep(random.uniform(1, 3))
        #     # for character in rc:
        #     #     recoveminput.send_keys(character)
        #     #     time.sleep(random.uniform(0.1, 0.3))
        #     # time.sleep(random.uniform(0.5, 1))
        #     # recoveminput.send_keys(Keys.RETURN)
        # except Exception as e: print(e)

        #allowing google access to the app:
        print('Clicking Allow Button')
        try:
            Browser_one.find_element_by_xpath('//*[@id="submit_approve_access"]').click()
        except Exception as e: print(e)

        time.sleep(5)
        print('Redirecting to Hi5')
        Browser_one.get('https://secure.hi5.com/')

        Browser_one.find_element_by_xpath(
            "//html/body/div[2]/div[3]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span").click()
        print('Logging in to hi5 using %s' % email)
        time.sleep(5)
        Browser_one.get('https://secure.hi5.com/account_info.html?dataSource=Settings&ll=nav')
        time.sleep(3)
        session = Browser_one.get_cookie('S')
        bsession = Browser_one.get_cookie('B')
        bval = bsession['value']
        sval = session['value']
        print('session Retrieved: S=%s'%sval)
        Browser_one.quit()

        return sval, bval
    except Exception as e: print(e)


def reload(email, password):
    print('starting login function')
    FIPATH = geckopath
    #PATH = "C:/Users/hadji/chromedriver.exe"

    options = Options()
    uag = open('WUserAgents.txt').read().splitlines()
    uar = random.choice(uag)
    options.headless = False
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", uar)

    Browser_one = webdriver.Firefox(executable_path=FIPATH, firefox_profile=profile, options=options)
    #Browser_one = webdriver.Chrome(executable_path=PATH)

    Browser_one.implicitly_wait(30)
    Browser_one.set_window_size(1024, 690)

    Browser_one.get("https://accounts.google.com/o/oauth2/auth/identifier?response_type=permission id_token code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcontacts.readonly&openid.realm&include_granted_scopes=true&redirect_uri=storagerelay%3A%2F%2Fhttps%2Fsecure.hi5.com%3Fid%3Dauth761688&client_id=1034081759906-qmctkoa6acasj44mr28353f7m5qfnj2q.apps.googleusercontent.com&ss_domain=https%3A%2F%2Fsecure.hi5.com&gsiwebsdk=shim&access_type=offline&flowName=GeneralOAuthFlow")
    # Browser_one.get('https://www.whatismyip-address.com/?check')

    em = "%s" % email
    pa = "%s" % password
    rc = '%s' % recovmail
    try:

        print("Typing email address...")
        try:
            emailinput = Browser_one.find_element_by_id("identifierId")
        except:
            emailinput = Browser_one.find_element_by_id("Email")

        for character in em:
            emailinput.send_keys(character)
            time.sleep(random.uniform(0.1, 0.3))
        time.sleep(random.uniform(1, 1.5))
        emailinput.send_keys(Keys.RETURN)
        # time.sleep(1000)
        time.sleep(random.uniform(1, 1.5))
        print("typing Password...")
        time.sleep(random.uniform(1, 1.5))
        passwordinput = Browser_one.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
        time.sleep(random.uniform(1, 1.5))
        for character in pa:
            passwordinput.send_keys(character)
            time.sleep(random.uniform(0.05, 0.1))
        time.sleep(random.uniform(1, 1.5))
        passwordinput.send_keys(Keys.RETURN)

        # try:
        #     #print("Typing Recovery email...")
        #     # #time.sleep(1000)
        #     # Browser_one.find_element_by_xpath("//div[contains(@id, 'view_container')]")
        #     # print('stxpath click')
        #     # recoveminput = Browser_one.find_element_by_xpath("//html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]")
        #     # recoveminput.click()
        #     # print('clicked')
        #     #
        #     # time.sleep(random.uniform(1, 3))
        #     # for character in rc:
        #     #     recoveminput.send_keys(character)
        #     #     time.sleep(random.uniform(0.1, 0.3))
        #     # time.sleep(random.uniform(0.5, 1))
        #     # recoveminput.send_keys(Keys.RETURN)
        # except Exception as e: print(e)

        # allowing google access to the app:
        print('Clicking Allow Button')
        try:
            Browser_one.find_element_by_xpath('//*[@id="submit_approve_access"]').click()
        except Exception as e:
            print(e)

        time.sleep(5)
        print('Redirecting to Hi5')
        Browser_one.get('https://secure.hi5.com/')

        Browser_one.find_element_by_xpath(
            "//html/body/div[2]/div[3]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span").click()
        print('Logging in to hi5 using %s' % email)
        time.sleep(5)
        Browser_one.get('https://secure.hi5.com/account_info.html?dataSource=Settings&ll=nav')
        time.sleep(3)
        session = Browser_one.get_cookie('S')
        bsession = Browser_one.get_cookie('B')
        bval = bsession['value']
        sval = session['value']
        print('Session Retireved: S=%s & B=%s'%(sval, bval))

        fcookie = {'S': '%s' % sval, 'B': '%s' % bval}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
                   'X-Requested-With': 'XMLHttpRequest'}
        try:

            # Update Password
            print('Launching the API Part...')
            print('Updating Password...')
            furl = 'https://secure.hi5.com/api/?application_id=user&format=JSON'
            passcon = {'method': 'tagged.account.setPassword', 'oldPass': 'NewPassword456', 'newPass': 'NewPassword456',
                       'confPass': 'NewPassword456'}
            upass = requests.post(furl, data=passcon, cookies=fcookie, headers=headers)
            passresult = json.loads(upass.text)
            print(passresult)
        except Exception as e: print(e)

        Browser_one.quit()
        return sval, bval
    except Exception as e: print(e)


def picup(sess):
    fcookie = {'S': '%s' % sess}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'X-Requested-With': 'XMLHttpRequest'}

    try:
        # Upload Pictures
        picurls = open('piclinks.txt', 'r').read().splitlines()
        picurl = random.choice(picurls)
        print(picurl)
        purl = 'https://www.hi5.com/api/?application_id=user&format=JSON'
        print('Uploading Picture from url')
        odara = {'method': 'tagged.photo.urlUpload', 'url': '%s' % picurl, 'make_large_thumb': 'true',
                 'full_path_size': 'p', 'image_type': 'P', 'album_id': '0'}
        upic = requests.post(purl, data=odara, cookies=fcookie, headers=headers, proxies=proxy)
        resu = json.loads(upic.text)
        print(resu)
        results = resu['result']
        picid = results['id']
        print('Photo id is %s, Making it primary' % picid)
        time.sleep(2)
        pdara = {'method': 'tagged.photo.setPrimary', 'photo_id': '%s' % picid}
        sepic = requests.post(purl, data=pdara, cookies=fcookie, headers=headers, proxies=proxy)
        print(sepic)

    except Exception as e: print(e)

def passup(sess, bsess):
    fcookie = {'S': '%s' % sess, 'B': '%s' % bsess}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'X-Requested-With': 'XMLHttpRequest'}

    try:

        # Update Password
        print('Launching the API Part to update the password')
        print('Updating Password...')
        furl = 'https://secure.hi5.com/api/?application_id=user&format=JSON'
        passcon = {'method': 'tagged.account.setPassword', 'oldPass': 'Letsroll123', 'newPass': 'Letsroll123',
                   'confPass': 'Letsroll123'}
        upass = requests.post(furl, data=passcon, cookies=fcookie, headers=headers)
        passresult = json.loads(upass.text)
        print(passresult)
        print('\nPassword Updated\n')
    except:
        print('something went wrong with Updating the password')


# # Generating a proxy
# def get_proxies(ua):
#     proxies = []
#     proxies_req = Request('https://www.sslproxies.org/')
#     proxies_req.add_header('User-Agent', ua.random)
#     proxies_doc = urlopen(proxies_req).read().decode('utf8')
#
#     soup = BeautifulSoup(proxies_doc, 'html.parser')
#     proxies_table = soup.find(id='proxylisttable')
#
#   # Save proxies in the array
#     for row in proxies_table.tbody.find_all('tr'):
#         proxies.append({
#                         'ip':   row.find_all('td')[0].string,
#                         'port': row.find_all('td')[1].string})
#     return proxies
#
# def random_proxy(proxies):
#   return random.choice(proxies)


#Deckaring Variables:
print('\n Make sure geckodriver is in home directory after user folder name\n')
devicename = input('What your PC name: ')
osystem = input('Are you on (W)indows Or (L)inux Or (M)ac: ')
headstatus = input('Headless should be (T)rue or (F)alse: ')
slptime = int(input('Minutes Between Each Account:  ')) * 60
if headstatus == 'T':
    hidden = 'True'
elif headstatus == 'F':
    hiddem = 'False'
#
if osystem == 'W':
    geckopath = 'C:/Users/%s/geckodrive'%devicename
elif osystem == 'L':
    geckopath = '/home/%s/geckodriver'%devicename
if osystem == 'M':
    geckopath = '/Users/%s/geckodriver'%devicename


#Code

s_time = time.time()

email_password_list = list()
with open("gglacc.txt") as file:
    for line in file:
        email, password, recovmail = line.split(':')
        email_password_list.append((email, password, recovmail))

for email, password, recovmail in email_password_list:

    # ua = UserAgent()
    # proxies = get_proxies(ua)
    proxy = []    #random_proxy(proxies)
    #
    # proxy = {
    #     "http": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
    #     "https": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
    # }


    print('Getting session to create an account with %s from the end point...'%email)
    sess, bsess = login(email, password, recovmail)           # Login for the first time to get the session
    fixaccount(sess)                            # Update user info


    print('Updating Profile Picture')
    print('Adding Profile Picture...')
    ssess, sbsess = reload(email, password)
    picup(ssess)                                 # Update user profile picture

    print('account created succussfully with %s' % email)
    # outpua = open('hiaccounts.txt', 'a+')
    # outpua.write(email)
    # outpua.close()

    print('a google account is completed, moving on to another one')
    print('sleeping for %s'%slptime)
    time.sleep(slptime)

e_time = time.time() - s_time
minu = e_time / 60

print('\nScript done in %s\n'%minu)