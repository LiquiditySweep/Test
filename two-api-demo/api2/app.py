import logging
from fastapi import FastAPI, Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [API2] %(message)s"
)

app = FastAPI(title="API2 Service")

@app.get("/hello")
async def hello(name: str = "world", request: Request = None):
    client_ip = request.client.host if request else "?"
    logging.info(f"/hello called from {client_ip=}, name={name}")
    return {"service": "api2", "message": f"Hello {name} from API2!"}

@app.get("/health")
async def health():
    return {"status": "ok", "service": "api2"}
