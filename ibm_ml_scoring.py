import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account
API_KEY = "<YokhkNK_p3NzrHSARMi7zs2HhE1avB4T-kboXoM6c3cP>"

# Get IAM token
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token',
    data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
)
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {
    "messages": [
        {
            "content": "",  # Fill with your input content
            "role": ""      # Fill with the role if required by your model
        }
    ]
}

response_scoring = requests.post(
    'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/4184c73f-2fd9-4ae8-8f63-e63fea1ab40b/ai_service_stream?version=2021-05-01',
    json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken}
)

print("Scoring response")
try:
    print(response_scoring.json())
except ValueError:
    print(response_scoring.text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
