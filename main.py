# -*- coding: cp1251 -*-
import urllib
import json
import time
from datetime import datetime


def main():
    # paste your token below:
    token = '26ecc39cc4ef6fae47639c6bf6aa2414245e726835bee4869d18a14e3396677360b6747c382b82491a30e'
    t = datetime.now()
    glob = 0

    response = urllib.urlopen('https://api.vk.com/method/audio.getCount?oid=51758590&access_token=' + token)
    response = json.load(response)
    count = response['response']

    output = []
    offset = 0
    number = 100
    steps = count / number + 1
    for i in range(0, steps):
        if count > number:
            count -= number
        else:
            number = count

        response = urllib.urlopen('https://api.vk.com/method/audio.get?uid=51758590' + \
                                  '&count=' + str(number) + \
                                  '&offset=' + str(offset) + \
                                  '&access_token=' + token)
        response = json.load(response)
        audios = response['response']

        for j in audios:
            output.append({'aid': j['aid'],
                           'artist': j['artist'].lower().replace('the', ''),
                           'title': j['title'].lower().replace('the', '')})
        offset += number

    aSorted = [[o['artist'], o['title'], o['aid']] for o in output]
    aSorted.sort(reverse=True)

    errorRequest = 0

    before = output[0]['aid']
    for i in aSorted:
        response = urllib.urlopen('https://api.vk.com/method/audio.reorder?aid=' + str(i[2]) + \
                                  '&before=' + str(before) + \
                                  '&access_token=' + token)
                                  #after=0&before=' + str(before)
        response = json.load(response)
        try:
             get = response['response']
             if get == 1:
                 glob += 1
        except:
            errorRequest += 1
        before = i[2]

        time.sleep(0.3)

    print 'successful ' + str(glob) + '\nerrors ' + str(errorRequest)


    t = datetime.now() - t
    stat = open('_stat.txt', 'w')
    stat.write('worked= ' + str(t) + '\n\nsuccess audios ' + str(glob) + '\nerrors ' + str(errorRequest))
    stat.close


main()
