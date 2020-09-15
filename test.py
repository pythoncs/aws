from requests import post

data = {
    "TOKEN": "aws-sap-cs-2",
    "page": 1
    }


# response = post('http://0.0.0.0:8787/aws', json=data)
response = post('http://47.107.158.24:666/aws', json=data)

print(response.text)