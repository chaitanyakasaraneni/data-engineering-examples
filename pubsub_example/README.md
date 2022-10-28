# PubSub

This example fetches stock data using [Polygon.io](http://polygon.io) API and uploads it into Cloud Pub/Sub of GCP. 
Using Cloud Functions, the data is then pulled from Pub/Sub into a Cloud Storage Subscription.

## Project Folders & Files
- **[services](https://github.com/chaitanyakasaraneni/pubSubPractice/tree/main/services) Folder:** Contains the source code
  - [publishData_toPub.py](https://github.com/chaitanyakasaraneni/pubSubPractice/blob/main/services/publishData_toPub.py): Code to publish data to Pub/Sub Topic
  - [subscribeData_toStorage.py](https://github.com/chaitanyakasaraneni/pubSubPractice/blob/main/services/subscribeData_toStorage.py): Published data from Topic to subscribed Cloud Storage Bucket
- **[utils](https://github.com/chaitanyakasaraneni/pubSubPractice/tree/main/utils) Folder:** Contains config file and GCP credentials JSON file (either service account or IAM Role)
  - [example.cfg](https://github.com/chaitanyakasaraneni/pubSubPractice/blob/main/utils/example.cfg): Contains example format of config file I used.
