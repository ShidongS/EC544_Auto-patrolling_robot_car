import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('test.mov', 'rb')
s3.Bucket('Your_bucket').put_object(Key='test.mov', Body=data)