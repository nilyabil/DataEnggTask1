from google.cloud import storage

project_id = "qwiklabs-gcp-00-8945b8196cce"
bucket_name = "qwiklabs-gcp-00-8945b8196cce"
storage_client = storage.Client(project_id)
bucket = storage_client.create_bucket(bucket_name)

print(f"Bucket {bucket.name} created.")