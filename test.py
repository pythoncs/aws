from requests import post

data = {
    "TOKEN": "aws-sap-cs",
    # "page": 1
    }


response = post('http://0.0.0.0:5000/aws', json=data)

print(response.text)