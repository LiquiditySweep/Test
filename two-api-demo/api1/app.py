import logging
import os
import requests
from fastapi import FastAPI, Request

API2_URL = os.getenv("API2_URL", "http://api2:8000")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [API1] %(message)s"
)

app = FastAPI(title="API1 Service")

@app.get("/call-api2")
def call_api2(name: str = "world", request: Request = None):
    client_ip = request.client.host if request else "?"
    logging.info(f"/call-api2 received from {client_ip=}; forwarding to API2")

    try:
        r = requests.get(f"{API2_URL}/hello", params={"name": name}, timeout=5)
        r.raise_for_status()
        upstream = r.json()
        logging.info(f"Upstream API2 OK status={r.status_code}")
    except Exception as e:
        logging.exception("Error calling API2")
        return {"service": "api1", "error": str(e)}

    return {"service": "api1", "upstream": upstream}

@app.get("/health")
def health():
    return {"status": "ok", "service": "api1", "api2_url": API2_URL}
