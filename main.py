import os
import time
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


for dirname, dirnames, filenames in os.walk('.'):
# print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        print(os.path.join(dirname, filename))
        abspath = (os.path.abspath(filename))
        print(abspath)


        file_stats = os.stat(filename)

        file_name, file_extension = os.path.splitext(abspath)

        print(file_name)
        print(file_extension)        

        print(file_stats)
        print(f'File Size in Bytes is {file_stats.st_size}')
        print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

        ti_c = os.path.getctime(abspath)
        ti_m = os.path.getmtime(abspath)
        
        # Converting the time in seconds to a timestamp
        c_ti = time.ctime(ti_c)
        m_ti = time.ctime(ti_m)
        
        print(f"The file located at the path {abspath} \
        was created at {c_ti} and was "
            f"last modified at {m_ti}")

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
    # don't go into any .git directories.
        dirnames.remove('.git')
    if '.venv' in dirnames:
    # don't go into any .venv directories.
        dirnames.remove('.venv')    
    if '__pycache__' in dirnames:
    # don't go into any __pycache__ directories.
        dirnames.remove('__pycache__')       
    