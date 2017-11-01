# Sample Dataflow job which throws error when writing data to BigQuery

in main.py set variables to run  



when I run this locally on my computer it works ok.

But when I run on Dataflow, it throws following error:  

```
apache_beam.runners.dataflow.dataflow_runner.DataflowRuntimeException: Dataflow pipeline failed. State: FAILED, Error:
(ade3180ffa878a6b): Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/dataflow_worker/batchworker.py", line 706, in run
    self._load_main_session(self.local_staging_directory)
  File "/usr/local/lib/python2.7/dist-packages/dataflow_worker/batchworker.py", line 446, in _load_main_session
    pickler.load_session(session_file)
  File "/usr/local/lib/python2.7/dist-packages/apache_beam/internal/pickler.py", line 247, in load_session
    return dill.load_session(file_path)
  File "/usr/local/lib/python2.7/dist-packages/dill/dill.py", line 363, in load_session
    module = unpickler.load()
  File "/usr/lib/python2.7/pickle.py", line 858, in load
    dispatch[key](self)
  File "/usr/lib/python2.7/pickle.py", line 1182, in load_append
    list.append(value)
  File "/usr/local/lib/python2.7/dist-packages/apitools/base/protorpclite/messages.py", line 1142, in append
    self.__field.validate_element(value)
AttributeError: 'FieldList' object has no attribute '_FieldList__field'
```

Apache Beam version is 2.1.1

