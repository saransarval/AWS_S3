import boto3
import csv
#initialize  and conect to the aws cloud


with open('credentials.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)
    for row in reader:
        print(row)
        awsaccesskeyid = row[2]
        awssecret_accesskey = row[3]




s3 = boto3.client('s3',aws_access_key_id =awsaccesskeyid ,aws_secret_access_key = awssecret_accesskey )
print("client connected")

upload_status=s3.upload_file('myphoto1.jpg','sarantestbucket','images/photo_1.jpg')
print(upload_status)
if not upload_status == True:
    print("Uploaded succesfully")

else:
    print("check the code")
