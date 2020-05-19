import boto3
session = boto3.Session(profile_name='pac')
s3 =session.resource('s3')

new_bucket = s3.create_bucket(Bucket='pi3141-v4', CreateBucketConfiguration={'LocationConstraint': session.region_name})
new_bucket.upload_file('index.html','index.html', ExtraArgs={'ContentType' : 'text/html'})

policy = policy.strip()
pol = new_bucket.Policy()
pol.put(policy=policy)



ws = new_bucket.Website()
ws.put(WebsiteConfiguration={
  'ErrorDocument': {
            'Key': 'error.html'
        },
        'IndexDocument': {
            'Suffix': 'index.html'
        }})

url = "http://"
policy = """
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::%s/*"
        }
    ]
}
""" % new_bucket.name

from botocore.exceptions import ClientError
