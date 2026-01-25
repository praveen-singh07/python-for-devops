import boto3

s3_client = boto3.client("s3")  # creating a client for S3 access
response = s3_client.list_buckets()

clean_data = []

for item in response["Buckets"]:
    print(item["Name"])
#for item in response.get("Buckets",[]):
    # extracted = {
    #     "Name": item.get("Name")
    #     # "task_title": item.get("title"),
    #     # "is_done": item.get("completed")
    #     }
    # clean_data.append(extracted)
    
    # another way
    #clean_data.append(item.get("Name"))

#print(clean_data)