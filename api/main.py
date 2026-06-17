from fastapi import FastAPI

from api.routes.analytics import router

app = FastAPI(
    title="E-Commerce Analytics API"
)

app.include_router(router)