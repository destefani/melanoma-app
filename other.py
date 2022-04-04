
from fastapi import FastAPI, UploadFile, File, Form

app = FastAPI()




@app.post("/")
async def login_with_form_data(hola:str = Form(...),
                               chao:str = Form(...)):
    return{"username":hola, "password":chao}



# @app.post("/")
# async def create_mytest_file(file: bytes=File(...)):
#      
#   return {"size_of_file":len(file)}

@app.post("/")
async def create_mytest_file_name(file: UploadFile=File(...)):
     
  return {"name_of_file":file.filename}
 