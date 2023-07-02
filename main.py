from fastapi import FastAPI
from .api.api_v1.api import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn
main: app - -reload