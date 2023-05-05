from google.cloud import storage


project_id = "qwiklabs-gcp-00-b0ccf959449d"
client = storage.Client(project=project_id)
bucket = client.get_bucket('qwiklabs-gcp-00-b0ccf959449d')
blob = bucket.blob('demo.txt')
contents = blob.download_as_string()
print(contents)
