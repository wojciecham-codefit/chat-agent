﻿import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="api.application:app", reload=True, port=8855)