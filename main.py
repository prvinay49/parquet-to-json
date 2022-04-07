
import json
import pandas as pd


user_json = '{"id" : "id1", "firstname": "John", "lastname":"Doe"}'
user_dict = json.loads(user_json)

# Pass an index instead
df = pd.DataFrame(user_dict, index=[0])
df.to_parquet('file.parquet')


dataset = pd.read_parquet('D:\sample/file.parquet', engine='pyarrow')
dataset.to_json('json_data.json')
