# utube_auto_up_backend
pip install testresources
pip install --upgrade google-api-python-client

uvicorn main:app --reload

python upload_video.py --file="./test_video_file.mp4" --title="Teste de Envio de video Pelo script Python"    --description="Este video foi enviado pelo script automatizado" --keywords="Programador Malandro" --category="22"   --privacyStatus="private"