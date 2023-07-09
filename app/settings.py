import os

MOZIO_API_KEY = os.getenv("MOZIO_API_KEY")
MOZIO_BASE_URL = os.getenv(
    "MOZIO_BASE_URL", "https://api-testing.mozio.com/v2/")
MOZIO_ENVIRONMENT = os.getenv("MOZIO_ENVIRONMENT", "development")
