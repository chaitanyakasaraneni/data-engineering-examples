import requests
import os
import time
import json
import configparser
from google.cloud import pubsub_v1

class Publish:
    def __init__(self, config):
        self.project_id = str(config['PROJECT']['PROJECT_ID'])
        self.topic_id = str(config['TOPIC']['TOPIC_ID'])
        self.api_url = str(config['API']['API_URL'])+str(config['API']['API_KEY'])
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(config['AUTH']['CRED_FILE'])

    def fetch_stock(self):
        url = self.api_url

        response = requests.get(url)
        string = response.json()['results'][0]
        string['active']= str(string['active'])

        json_string = json.dumps(string)
        print("string =",json_string)

        return str(json_string)


    def publish_msg(self):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self.project_id,self.topic_id)

        # fetch_stock should be byte string
        stock_data = self.fetch_stock()
        stock_data = stock_data.encode("utf-8")

        future = publisher.publish(topic_path,stock_data)
        print(future.result())



if __name__=='__main__':
    #read configuration file
    config = configparser.ConfigParser()
    config.read('utils/config.cfg')
    
    pub = Publish(config)
    pub.publish_msg()
    pub.fetch_stock()