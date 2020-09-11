from pykafka import KafkaClient
import json
from datetime import datetime
import uuid


file=open('/root/Notebooks/Geo.json')
array= json.load(file)
cordinates= array['features'][0]['geometry']['coordinates']
#print(cordinates)


#### Generate UUID

def generate_uuid():
    return uuid.uuid4()

client= KafkaClient(hosts="localhost:9092")
#print(client.topics['sample'])  # to create sample data topic 
topic =client.topics['sampleData']
producer= topic.get_sync_producer()

data={}
data['ID']='009'

def generate_data(cordinates):
    i =0
    while i < len(cordinates):
        data['key']=data['ID']+_+str(generate_uuid())
        data['timestamp]=str(datetime.utcnow())
        data['long']= cordinates[i][0]
        data['lati']=cordinates[i][1]
        message= json.dumps(data)
        producer.produce(message.encode('ascii'))
        if i == len(cordinates)-1:
            i=0
        else:
            i +=1
generate_data(cordinates)




'''
client= KafkaClient(hosts="localhost:9092")
#print(client.topics['sample'])  # to create sample data topic 
topic =client.topics['sampleData']
producer= topic.get_sync_producer()
count=1
while True:
    message=("hey wassup it started" + str(count)).encode('ascii')
    producer.produce(message)
    print(message)
    cout +=1
'''

Read JSON Data
     
