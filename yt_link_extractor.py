
import regex as re
import requests
import googleapi.client.discovery
import googleapiclient.errors
import pandas as pd

url="https://www.youtube.com/@FutureSmartAI/videos"
response = requests.get(url)

video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
print(video_ids)

