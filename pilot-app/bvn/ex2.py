from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(mongo_uri)

ex2 = client.c4e

customer = ex2['customers']


events = customer.find({'ref':'events'})
ads = customer.find({'ref':'ads'})
wom = customer.find({'ref':'wom'})

event = 0
wom = 0 
ads = 0

customers = customer.find()

for i in customers :
    if i['ref'] == 'events':
        event+= 1
    elif i['ref'] == 'wom':
        wom+=1
    elif i['ref'] == 'ads': 
        ads+=1

print('event : ',event)
print('wom : ',wom)
print('ads : ',ads)

ref_type = [event,wom,ads]
ref_name = ['events','wom','ads']


pyplot.pie(ref_type , labels = ref_name,autopct='%.1f%%',)
pyplot.axis('equal')
pyplot.show()

