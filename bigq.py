from google.cloud import bigquery
from google.cloud.bigquery import job

# Create a client object
client = bigquery.Client("qwiklabs-gcp-04-95658d53321d")

# Define the source and destination
dataset_ref = client.dataset('demoDataset')
table_ref = dataset_ref.table('demoTable')
job_config = job.LoadJobConfig()
job_config.source_format = job.SourceFormat.CSV
job_config.skip_leading_rows = 1
job_config.autodetect = True
uri = 'gs://my_bucket/demo.csv'

# Submit the job to load the data
load_job = client.load_table_from_uri(
    uri,
    table_ref,
    job_config=job_config,
)

# Wait for the job to complete
load_job.result()
