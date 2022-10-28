import base64
from json import loads
from pandas import DataFrame
from google.cloud.storage import Client

class Load_to_DB:
    def __init__(self,event,context):
        self.event = event
        self.context = context
        self.bucket_name = 'stock-storage-bin1'

    def get_message(self):

        if 'data' in self.event:
            pubsub_message = base64.b64decode(self.event['data']).decode('utf-8')
            return pubsub_message
        return

    def transform_payload_to_dataframe(self,message):
        message = loads(message)
        file_id= message['last_updated_utc']
        df = DataFrame([message])
        return df,file_id

    def upload_to_bucket(self,df,file_id):

        storage_client = Client()
        bucket = storage_client.bucket(self.bucket_name)
        blob = bucket.blob(f'stocks{file_id}.csv')
        blob.upload_from_string(df.to_csv(),content_type="text/csv")
        return


def hello_pubsub(event, context):

    """Triggered from a message on a Cloud Pub/Sub topic.
      Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    process = Load_to_DB(event,context)
    message = process.get_message()
    upload_df,file_id = process.transform_payload_to_dataframe(message)
    process.upload_to_bucket(upload_df,file_id)