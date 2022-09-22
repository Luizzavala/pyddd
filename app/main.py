from fastapi import FastAPI
app = FastAPI(title="python_ddd",
              version="0.1",
              openapi_url="/openapi.json")