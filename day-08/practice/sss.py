import boto3

def get_connection(service):
    return  boto3.client(service)

def show_buckets(s3_client):
    response = s3_client.list_buckets()
    for bucket in response["Buckets"]:
        print(bucket["Name"])

# def show_regions(ec2_client):
#     response = ec2_client.describe_regions()
#     print(response)

def create_bucket(s3_client, bucket_name):
    try:
        response = s3_client.create_bucket(Bucket = bucket_name)
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print(f"Bucket {bucket_name} created success fully : ", bucket_name)
        else:
            print("Error occured while creating the bucket ")
    except Exception as e:
        print("Error occured : ",e)


def upload_to_bucket(s3_client,file_path,bucket_name,key_name):
        s3_client.upload_file(file_path,bucket_name,key_name)
        print("File uploaded successfully")
        

s3 = get_connection("s3")
#ec2 = get_connection("ec2")
show_buckets(s3)
#create_bucket(s3,"my-first-bucket")
upload_to_bucket(s3, "output1.json", "rehman-ki-balti", "Output.json")