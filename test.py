from requests import post

data = {
    "TOKEN": "aws-sap-cs",
    "page": 1
    }


# response = post('http://0.0.0.0:5000/aws', json=data)
response = post('http://47.107.158.24:666/aws', json=data)

print(response.text)