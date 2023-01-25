import os
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Hello World"}
    
@app.get('/files')
def showFiles():
    entries = os.listdir('.')
    for entry in entries:
        # print(entry)
        #if entry.is_file():
        #    print("is file: " + entry.name)
        #else:
        #    print("is folder: " +  entry.name)    
        filtered = []
        for word in entries:
            if "." in word:
                filtered.append(word)

        #filtered = filter(lambda file: '.' in file, entries)
        #print(list(filtered))
    return {"files": filtered}    
