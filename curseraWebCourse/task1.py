#This is my solution for the first-week task https://www.coursera.org/learn/python-for-web/programming/POfZx/praktika-po-requests
#(access_token removed, but y can get via instractions in link i gave before)
import requests as rq
import json
import datetime
def getIdByUID(uid):
    payload = {'v': '5.71', 'access_token': 'REMOVED',
     'user_ids': uid}
    return rq.get('https://api.vk.com/method/users.get', params=payload).json()['response'][0]['id']

def sorting(pare):
    pass    

def calc_age(uid):
    payload = {'v': '5.71', 'access_token': 'REMOVED',
     'user_id': getIdByUID(uid), 'fields': 'bdate'}
    usersList = rq.get('https://api.vk.com/method/friends.get', params=payload).json()['response']['items']
    resultDict = {}
    for item in usersList:
        bdate = item.get('bdate')
        if  bdate != None:
            if len(bdate.split('.')) == 3:
                newValue =  datetime.datetime.now().year - int(bdate.split('.')[2])
                dictValue = resultDict.get(newValue)
                if dictValue != None:
                    resultDict.update({newValue: dictValue+1})
                else:
                    resultDict.update({newValue: 1})
    newList = list(resultDict.items())  
    newList.sort(key= lambda x: (-x[1], x[0])) 
    return newList

print(calc_age('reigning'))