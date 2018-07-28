import os, requests
from configparser import ConfigParser

#PREPARING CONFIG
#MADE BY CYB0R

cfg = ConfigParser()
if not os.path.exists('config.ini'):
    print ('CONFIG FILE NOT FOUND, SET VALUES')
    tokken = input ('tokken >> ')
    newconfig(tokken)
else:
    cfg.read('config.ini')
    upload_link = cfg['USER_DATA']['upload_link']

def main():
    os.system('cls')
    mode = input ('Single or multiple files? s/m >> ')
    if mode == 's':
        mode1()
    elif mode == 'm':
        mode2()
    else:
        print ('Wrong mode')
        os.system('pause')
        main()

def mode1():
    link = input ('LINK >> ')
    page = requests.get(upload_link + link)
    url = page.url
    print (url + ' : ' + link)

def mode2():
    file = input ('FILE PATH >> ')
    if not file:
        file = 'Links.txt'
    print ('Shorting links from ' + file + '...')
    try:
        links = [line.rstrip('\n') for line in open(file)]
        for link in links:
            print (link)
            try:
                page = requests.get(upload_link + link)
                url = page.url
                print (url + ' : ' + link)
            except:
                print ('ERROR')

    except:
        print ('INVALID FILE!')
        mode2()


def newconfig(tokken):
    cfg['USER_DATA'] = {'user_tokken' : tokken, 'upload_link' : 'http://sh.st/st/' + tokken + '/'}

    with open ('config.ini', 'w') as configfile:
        cfg.write(configfile)

main()
