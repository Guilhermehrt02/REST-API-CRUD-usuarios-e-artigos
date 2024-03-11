from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso API - Seguranca')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, 
                log_level='info', reload=True)
    
# Token
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzA3OTIwMDM2LCJpYXQiOjE3MDczMTUyMzYsInN1YiI6IjEifQ.fMztEtyxPRcAB93pC5p7g8tm9--5HMrlpSvw-grPyus
# tipo Baerer 