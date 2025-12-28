from fastapi import FastAPI
from routers import aws


app = FastAPI(
    title="Internal DevOps utilities test API",
    description="This is an Internal test API utilities App for Monitiring matrics, AWS usage, Log Anlysis etc",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def hello():
    return {"Message": "Hello this is a test message from devops utilities api."}

app.include_router(aws.router, prefix="/aws")