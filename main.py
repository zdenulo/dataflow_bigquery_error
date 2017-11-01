# -*- coding: utf-8 -*-
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

if __name__ == '__main__':
    OUTPUT_TABLE = ''  # name of BigQuery table to which data will be written
    DATESET = ''  # name of dataset
    PROJECT = ''  # name of project
    BUCKET = ''  # name of Google Cloud Storage Bucket
    OUTPUT_TABLE = 'bq-test'
    DATESET = 'working'
    PROJECT = 'starry-braid-156516'
    BUCKET = 'acuteiq_zdenko'
    pipeline_options = {
        'project': PROJECT,
        'staging_location': 'gs://' + BUCKET + '/staging',
        'runner': 'DataflowRunner',
        # 'runner': 'DirectRunner',
        'job_name': 'bq-test',
        'temp_location': 'gs://' + BUCKET + '/temp',
        # 'requirements_file': 'requirements.txt',
        'save_main_session': True
    }

    options = PipelineOptions.from_dictionary(pipeline_options)
    p = beam.Pipeline(options=options)

    bq = p | 'Create data' >> beam.Create([{'name': 'X'}, {'name': 'Y'}, {'name': 'Z'}])

    bq = bq | 'Write data to BigQuery' >> beam.io.WriteToBigQuery(OUTPUT_TABLE, dataset=DATESET, project=PROJECT,
                                                                  create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                                                                  write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
                                                                  schema="name:STRING"
                                                                  )
    result = p.run()
    result.wait_until_finish()
