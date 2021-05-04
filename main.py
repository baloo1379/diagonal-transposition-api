import fastapi
import uvicorn
from routes.api import router as api_router


app = fastapi.FastAPI()


def prepare_routes():
    app.include_router(api_router)


@app.on_event("startup")
def startup_event():
    prepare_routes()


if __name__ == '__main__':
    uvicorn.run(app)
