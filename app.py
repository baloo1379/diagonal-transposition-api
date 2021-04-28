import fastapi
import uvicorn
from routes.api import router as api_router


app = fastapi.FastAPI()


def prepare_routes():
    app.include_router(api_router)


if __name__ == '__main__':
    prepare_routes()
    uvicorn.run(app)
else:
    prepare_routes()
