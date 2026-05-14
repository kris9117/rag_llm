from fastapi import Header, HTTPException

API_SECRET = "rag-secret"

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_SECRET:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )