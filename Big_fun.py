from google.cloud import bigquery


def helper():
    client = bigquery.Client("qwiklabs-gcp-02-604e79097f7f")
    dataset_id="qwiklabs-gcp-02-604e79097f7f.my_dataset"
    table_id="qwiklabs-gcp-02-604e79097f7f.my_dataset.my_table"

    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    dataset = client.create_dataset(dataset, timeout=30)  
    print("Created dataset {}.{}".format(client.project, dataset.dataset_id))

    uri = "gs://qwiklabs-gcp-02-604e79097f7f/demo.csv"
    schema=[
            bigquery.SchemaField("Name", "STRING"),
            bigquery.SchemaField("Age", "INTEGER"),
        ]

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("Name", "STRING"),
            bigquery.SchemaField("Age", "INTEGER"),
        ],
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
    )

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows.".format(destination_table.num_rows))