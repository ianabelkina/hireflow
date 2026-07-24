from fastapi import FastAPI

app = FastAPI(
    title="HireFlow API",
    description="Backend API for the HireFlow recruitment platform",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "HireFlow API is running"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}