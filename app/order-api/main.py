import json
import logging
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Order API",
    version="0.1.0",
)


orders = [
    {
        "id": "1001",
        "customer": "jason",
        "product": "laptop",
        "quantity": 1,
        "amount": 1299.99,
        "status": "confirmed",
    },
    {
        "id": "1002",
        "customer": "rick",
        "product": "keyboard",
        "quantity": 2,
        "amount": 149.98,
        "status": "processing",
    },
    {
        "id": "1003",
        "customer": "charlie",
        "product": "monitor",
        "quantity": 1,
        "amount": 399.99,
        "status": "shipped",
    },
]


logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)

logger = logging.getLogger("order-api")


def log_event(event: str, status: int, order_id: str | None = None):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": "INFO",
        "service": "order-api",
        "event": event,
        "status": status,
    }

    if order_id:
        log_entry["order_id"] = order_id

    logger.info(json.dumps(log_entry))


@app.get("/health")
def health():
    log_event("health_check", 200)

    return {
        "status": "ok",
        "service": "order-api",
    }


@app.get("/ready")
def ready():
    log_event("readiness_check", 200)

    return {
        "status": "ready",
        "service": "order-api",
    }


@app.get("/orders")
def get_orders():
    log_event("orders_request", 200)

    return orders

@app.get("/orders/test-error")
def test_error():
    log_event("test_error", 500)

    return JSONResponse(
        status_code=500,
        content={"error": "intentional test error"},
    )

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    for order in orders:
        if order["id"] == order_id:
            log_event("order_request", 200, order_id)
            return order

    log_event("order_request", 404, order_id)

    return JSONResponse(
        status_code=404,
        content={"error": "order not found"},
    )


@app.get("/")
def root():
    return {
        "service": "order-api",
        "version": "0.1.0",
        "docs": "/docs",
    }