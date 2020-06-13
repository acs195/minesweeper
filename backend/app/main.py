"""This is the app main module"""

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router
from core.config import get_settings

settings = get_settings()


def create_app() -> FastAPI:
    """App factory"""
    openapi_url = f"{settings.API_V1_STR}/openapi.json"
    app = FastAPI(title=settings.PROJECT_NAME, openapi_url=openapi_url)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.get("/")
    def root() -> dict:
        """Root endpoint. Just return a json"""
        return {"Welcome": "to the machine"}

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)
