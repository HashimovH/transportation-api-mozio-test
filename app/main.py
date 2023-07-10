from fastapi import FastAPI
from app import settings
from app.routers import booking


app = FastAPI(
    title="Transportation Booking API",
    description="API for aggregating booking transportation services",
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/public/openapi.json",
    debug=bool(settings.DEBUG or False),
)

app.include_router(booking.router)
