import uvicorn
from api.routes.api import router as api_router
from events.beanie import init_db
from fastapi import FastAPI
from project.settings import settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, debug=settings.DEBUG, version=settings.VERSION
    )

    application.include_router(api_router, prefix=settings.API_PREFIX)
    return application


app = get_application()


@app.on_event("startup")
async def on_startup():
    await init_db()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)
