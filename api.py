from fastapi import FastAPI, UploadFile
import uvicorn
from controller import processFileUpload
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return 'This app is running'

@app.post("/upload-file")
async def create_upload_file(files: list[UploadFile]):
   return await processFileUpload(files)
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
