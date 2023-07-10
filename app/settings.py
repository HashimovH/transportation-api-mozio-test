import os

MOZIO_API_KEY = os.getenv("MOZIO_API_KEY", "6bd1e15ab9e94bb190074b4209e6b6f9")
MOZIO_BASE_URL = os.getenv("MOZIO_BASE_URL", "https://api-testing.mozio.com/v2/")
MOZIO_ENVIRONMENT = os.getenv("MOZIO_ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", True)
