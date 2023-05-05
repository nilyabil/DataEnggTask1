from google.cloud import storage
# Set the credentials and the name of the bucket you want to upload the file to.
# storage_client = storage.Client.from_service_account_json('D:\python\Google\keys.json')
bucket_name = 'qwiklabs-gcp-00-8945b8196cce'
project_id='qwiklabs-gcp-00-8945b8196cce'
storage_client = storage.Client(project_id)
local_file_path = 'D:\demo.txt' # Set the path to the local file you want to upload.
destination_blob_name = 'demo1.txt' # Set the name of the file you want to upload to GCS.


bucket = storage_client.bucket(bucket_name)# Get the bucket object you want to upload to.

blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(local_file_path)# Upload the file to GCS.

print(f'File {local_file_path} uploaded to gs://{bucket_name}/{destination_blob_name}.')
