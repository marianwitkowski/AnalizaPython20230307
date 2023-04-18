
import requests
import numpy as np

response = requests.get("http://127.0.0.1:1234/np")
s = response.text
arr = np.fromstring(s)
print(arr)