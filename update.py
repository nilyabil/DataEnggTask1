from google.cloud import storage


project_id = "qwiklabs-gcp-00-8945b8196cce"
client = storage.Client(project_id)
bucket = client.get_bucket('qwiklabs-gcp-00-8945b8196cce')
blob = bucket.blob('demo1.txt')

with blob.open("w") as f:
        f.write("Hello world")

with blob.open("r") as f:
        print(f.read())