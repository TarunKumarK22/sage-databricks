# import requests

# # Replace this with your actual Databricks API token
# databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"

# url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/list"
# payload = ""
# headers = {
#   'Authorization': f'Bearer {databricks_api_token}'
# }

# response = requests.request("GET", url, headers=headers, data=payload)
# print(response.text)

import os
import requests

# Replace this with your actual Databricks API token
databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"

url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id=496296034538647"
payload = ""
headers = {
    'Authorization': f'Bearer {databricks_api_token}'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    job_ids = [str(job["job_id"]) for job in data["jobs"]]
    print(job_ids)
    
    # Set the job IDs as environment variables
    for index, job_id in enumerate(job_ids, start=1):
        os.environ[f'JOB_ID_{index}'] = job_id
else:
    print(f"Failed to retrieve job data. Status code: {response.status_code}")

print(response.text)
