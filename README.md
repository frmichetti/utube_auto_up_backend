# utube_auto_up_backend

### Requirements
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