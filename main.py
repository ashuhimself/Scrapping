import requests
import time
import re
import json
import logging
import itertools
from tqdm import tqdm


start_time = time.time()
json_data = []
url = 'https://www.cermati.com/karir'
logging.basicConfig(filename='log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

with requests.Session() as session:
    html = session.get(url).text
    with open("index.html", "w") as f:
        f.write(html)
    pattern = re.compile(r'\bref":"(https?://[^"]+)')
    job_urls = pattern.findall(html)
    for job_url in job_urls:
        try:
            json_response = session.get(job_url)
            json_response.raise_for_status()
            data = json_response.json()
            final = {
                "department": data['department']['label'],
                "title": data['name'],
                "location": data['location']['region'] + ', ' + data['customField'][2]["valueLabel"],
                "description": re.sub('<[^<]+?>', '', data['jobAd']['sections']['jobDescription']['text']).replace('&#xa0;', ''),
                "qualification": re.sub('<[^<]+?>', '', data['jobAd']['sections']['qualifications']['text']).replace('&#xa0;', ''),
                "posted by": data['creator']['name']
                } 
            json_data.append(final)
        except Exception as e:
            logging.exception(f"Error occurred while parsing data from {job_url}")

data = sorted(json_data, key=lambda x: x["department"])

grouped_data = {}
for department, group in itertools.groupby(data, key=lambda x: x["department"]):
    job_postings = [job_posting.copy() for job_posting in group]
    for job_posting in job_postings:
        del job_posting["department"]
    grouped_data[department] = job_postings

with open('data.json', 'w') as outfile:
    json.dump(grouped_data, outfile, indent=4)

end_time = time.time()
runtime = end_time - start_time
print(f"Program runtime: {runtime:.2f} seconds")
