import os
import logging
from datetime import datetime, timezone
from typing import Optional

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Profile API with Cat Facts",
    description="RESTful API endpoint that returns profile information with dynamic cat facts",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
CAT_FACT_API_URL = os.getenv("CAT_FACT_API_URL", "https://catfact.ninja/fact")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "5"))
USER_EMAIL = os.getenv("USER_EMAIL", "your.email@example.com")
USER_NAME = os.getenv("USER_NAME", "Your Full Name")
USER_STACK = os.getenv("USER_STACK", "Python/FastAPI")


async def fetch_cat_fact() -> Optional[str]:
    """Fetch a random cat fact from the Cat Facts API."""
    try:
        logger.info(f"Fetching cat fact from: {CAT_FACT_API_URL}")
        
        async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
            response = await client.get(CAT_FACT_API_URL)
            response.raise_for_status()
            
            data = response.json()
            fact = data.get("fact", None)
            
            if fact:
                logger.info("Successfully fetched cat fact")
                return fact
            else:
                logger.warning("Cat fact API returned empty fact")
                return None
                
    except httpx.TimeoutException:
        logger.error(f"Timeout while fetching cat fact (timeout={API_TIMEOUT}s)")
        return None
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error while fetching cat fact: {e.response.status_code}")
        return None
    except httpx.RequestError as e:
        logger.error(f"Network error while fetching cat fact: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error while fetching cat fact: {str(e)}")
        return None


@app.get("/me")
async def get_profile():
    """
    GET endpoint that returns user profile information along with a dynamic cat fact.
    """
    logger.info("GET /me endpoint called")
    
    # Get current UTC timestamp in ISO 8601 format
    current_timestamp = datetime.now(timezone.utc).isoformat()
    
    # Fetch cat fact from external API
    cat_fact = await fetch_cat_fact()
    
    # Fallback message if API fails
    if cat_fact is None:
        logger.warning("Using fallback cat fact due to API failure")
        cat_fact = "Unable to fetch cat fact at this moment. Please try again later."
    
    # Construct and return response
    return {
        "status": "success",
        "user": {
            "email": USER_EMAIL,
            "name": USER_NAME,
            "stack": USER_STACK
        },
        "timestamp": current_timestamp,
        "fact": cat_fact
    }


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Profile API with Cat Facts",
        "endpoints": {
            "/me": "GET - Returns profile information with a cat fact",
            "/docs": "GET - Interactive API documentation",
            "/redoc": "GET - Alternative API documentation"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", "8000"))
    
    logger.info(f"Starting server on port {port}")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )