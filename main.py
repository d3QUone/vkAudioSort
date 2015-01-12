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

    offset = 0
    number = 100
    steps = count / number + 1
    
    output = []
    append = output.append
    for i in range(0, steps):
        if count > number:
            count -= number
        else:
            number = count

        response = urllib.urlopen('https://api.vk.com/method/audio.get?uid=51758590' + \
                                  '&count={0}&offset={1}&access_token={2}'.format(number, offset, token))
        response = json.load(response)
        audios = response['response']

        for j in audios:
            append([j['artist'].lower().replace('the', ''), j['title'].lower().replace('the', ''), j['aid']])
            
        offset += number
    
    before = output[0][3] # 'aid'
    output.sort(reverse=True)

    errorRequest = 0
    for i in output:
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

    print 'successful {0}\nerrors {1}'.format(glob, errorRequest)

    t = datetime.now() - t
    stat = open('_stat.txt', 'w')
    stat.write('worked= {0}\n\nsuccess audios {1}\nerrors {2}'.format(t, glob, errorRequest))
    stat.close()

main()
