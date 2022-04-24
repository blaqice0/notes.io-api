# notes.io-api
Restful API for notes.io

# Requirements
* Python 3 
* Install from requirements.txt


# Examples
### Create Note
**Using Python 3**
```python
import requests
import json

url = "localhost:8000/api/v1/notes/"

payload = json.dumps({
    "title": "Note 1",
    "text": "Some text about Note 1"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

**Using Postman**
![screenshot](screenshots/create_note.png)

### Retrieve Note
**Using Python 3**
```python

import requests

url = "localhost:8000/api/v1/notes/1/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

```
**Using Postman**
![screenshot](screenshots/retrieve_note.png)

### Retrieve All Notes
**Using Python 3**
```python

import requests

url = "localhost:8000/api/v1/notes/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

```
**Using Postman**
![screenshot](screenshots/retrieve_all.png)

### Update Note
**Using Python 3**
```python

import requests
import json

url = "localhost:8000/api/v1/notes/2/"

payload = json.dumps({
    "text": "Updated text on Note 2"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)

```
**Using Postman**
![screenshot](screenshots/update_note.png)

### Delete Note
**Using Python**
```python

import requests

url = "localhost:8000/api/v1/notes/1/"

payload={}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

```