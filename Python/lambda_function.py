import logging
import base64
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

response  = {
    'statusCode': 200,
    'headers': {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    },
    'body': ''
}
def getHashTag(queries):
    import requests
    url = "https://api.twitter.com/1.1/search/tweets.json"
    l = []
    print()
    for query in queries:
        print(query)
        payload ='q=' + query['Name'] + 'nyc' + '&result_type=recent'
        headers = {
          'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAO%2FfWQEAAAAANJCqO8tZ8iw3OUXSl7aYFHNG2BE%3DpASZ8a8RM1hVmQw0b3V45bYHmPk9LnDpN9H1NM3iueh9KcCPw6',
          'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': 'guest_id=v1%3A163847594419880767; guest_id_ads=v1%3A163847594419880767; guest_id_marketing=v1%3A163847594419880767; personalization_id="v1_QxAzF74n4hMhfVsJecGNGQ=="'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

    #     print(response.text)
        data = response.json()
        for i in data['statuses']:
            for j in i['entities']['hashtags']:
    #             print(j['text'])
                l.append(j['text'])
    l = [[i, l.count(i)] for i in set(l)]
    l.sort(key = lambda x: x[1], reverse=True)
    return l

def lambda_handler(event, context):

    file_name = event['headers']['file-name']
    file_content = base64.b64decode(event['body'])

    BUCKET_NAME = "hashtag-pic-uploads"

    try:
        s3_response = s3_client.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)
        logger.info('S3 Response: {}'.format(s3_response))
        response['body'] = 'Your file has been uploaded'
        client2 = boto3.client('rekognition',region_name = 'us-west-2')


        response2 = client2.detect_labels(Image = {"S3Object":{"Bucket": "hashtag-pic-uploads", "Name":file_name}}, MaxLabels = 10,MinConfidence= 50)
        labels = response2['Labels']
        numOfLables = len(labels)
        if numOfLables>5:
            labels = labels[:5]
        hashTags = getHashTag(labels)

        # for i in range(numOfLables):
        #         print(labels[i])



        response  = {
    'statusCode': 200,
    'headers': {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    },
    'body': hashTags
}

        return response


    except Exception as e:
        raise IOError(e)
