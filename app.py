from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
import httpx
from datetime import datetime, timezone


app = FastAPI(title="Cat Facts API Integration", version="1.0")


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)
logger = logging.getLogger(__name__)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


CAT_FACTS_URL = "https://catfact.ninja/fact"


@app.get("/", response_model=dict)
async def root():
    """Root endpoint"""
    return {"message": "Hello, World!"}


@app.get("/health", response_model=dict)
async def health_check():
    """Health check endpoint"""
    return JSONResponse(
        content={"status": "ok"},
        status_code=status.HTTP_200_OK
    )


async def call_cat_api() -> dict:
    """Fetch a random cat fact with error handling and timeout.
    
    Returns:
        dict: A dictionary containing the cat fact or an error message.
    """
    timeout = httpx.Timeout(5.0, connect=2.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            response = await client.get(CAT_FACTS_URL)
            response.raise_for_status()
            data = response.json()
            return {"fact": data.get("fact", "No fact available")}
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Cat Facts API: {e.response.status_code}")
            return {"error": "Failed to fetch cat fact from API"}
        except httpx.RequestError as e:
            logger.error(f"Network error calling Cat Facts API: {str(e)}")
            return {"error": "External API request failed or timed out"}


@app.get("/me", response_model=dict)
async def get_me():
    """Get user info along with a random cat fact.
    
    Returns:
        dict: A dictionary containing user info, timestamp, and a cat fact or error message.
        
    """
    fact_data = await call_cat_api()
    timestamp = datetime.now(timezone.utc).isoformat()

    return JSONResponse(
        content={
            "status": "success",
            "user": {
                "email": "afariogun.john2002@gmail.com",
                "name": "John Afariogun",
                "stack": "Python/FastAPI",
            },
            "timestamp": timestamp,
            "fact": f"No cats today {fact_data["error"]}" if "error" in fact_data else fact_data["fact"],
        },
        status_code=status.HTTP_200_OK,
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080)
