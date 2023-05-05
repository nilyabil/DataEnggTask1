#Make sure to make file name as copy1 not copy


from google.cloud import storage


project_id = "qwiklabs-gcp-00-8945b8196cce"
storage_client = storage.Client(project=project_id)


src_bucket_name = "qwiklabs-gcp-00-8945b8196cce"
src_blob_name = "demo1.txt"
dest_bucket_name = "qwiklabs-gcp-03-4bc4194f8ea8"
dest_blob_name = "demo1.txt"

src_bucket = storage_client.get_bucket(src_bucket_name)
src_blob = src_bucket.blob(src_blob_name)
dest_bucket = storage_client.get_bucket(dest_bucket_name)
dest_blob = src_bucket.copy_blob(
    blob=src_blob, destination_bucket=dest_bucket, new_name=dest_blob_name
)

print(f"File {src_blob_name} copied to {dest_blob_name} in {dest_bucket_name} bucket.")
