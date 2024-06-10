#%%
import requests
import pandas as pd

#%% define the endpoint
endpoint = "https://opendata.cbs.nl/ODataApi/odata/85791NED/UntypedDataSet"

# %% execute the request
response = requests.get(endpoint)
# %%
data = response.json()
# %%
data
# %%
records = data['value']

# %%
records
# %%
len(records)
# %%
records[40]
# %%
df = pd.DataFrame(records)
# %%
df.info()
# %%
