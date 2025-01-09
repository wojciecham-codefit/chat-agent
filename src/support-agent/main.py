import os
import uvicorn

RELOAD = os.getenv("UVICORN_RELOAD", "True").lower() in ("true", "1")
HOST = os.getenv("UVICORN_HOST", "0.0.0.0")
PORT = os.getenv("UVICORN_PORT", 8855)

if __name__ == "__main__":
    uvicorn.run(app="api.application:app", reload=RELOAD, port=PORT, host=HOST)