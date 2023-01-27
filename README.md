# utube_auto_up_backend

## Prerequisites

*   Python 2.6 or greater

*   The pip package management tool

*   The Google APIs Client Library for Python:
    ```
    pip install --upgrade google-api-python-client
    ```
*   The google-auth, google-auth-oauthlib, and google-auth-httplib2 for user authorization.
    ```
    pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
    ```
    
## Requirements
```
pip install testresources
pip install --upgrade google-api-python-client
pip install "fastapi[all]"
```

### Start the server
```
uvicorn main:app --reload --port 8000
```

### Send video to Utube via script
```
python upload_video.py --file="./test_video_file.mp4" --title="Teste de Envio de video Pelo script Python"    --description="Este video foi enviado pelo script automatizado" --keywords="Programador Malandro" --category="22" --privacyStatus="private" 
--noauth_local_webserver
```

### Sample Payload to Send to Utube via API
```
{
  "file": "./test_video_file.mp4",
  "title": "Teste de Envio de video Pela API FAST do Python",
  "description": "Este video foi enviado pelo script automatizado API FAST",
  "keywords": "Programador Malandro",
  "category": "22",
  "privacyStatus": "private"
}
```
### Utube Quotas
https://developers.google.com/youtube/v3/getting-started?hl=pt-br#quota