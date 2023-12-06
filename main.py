from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from app.routes import userRoute
from app.db import connect

app = FastAPI()
connect.db_connect()
"""
TODO: include all routes from app.routes file
"""
app.include_router(userRoute.router, prefix="/api/v1/users")


@app.get("/health", tags=["Health"])
async def health():
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message": "API health perfect"
    })