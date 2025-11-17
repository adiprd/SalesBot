
from fastapi import APIRouter
from pydantic import BaseModel
from app.llm_client import call_openrouter
from app.db_helper import (
    get_sales_summary, get_top_products, get_sales_by_category,
    get_sales_trend, get_top_customers, get_payment_methods,
    execute_query
)

router = APIRouter()

class ChatReq(BaseModel):
    message: str

@router.post("/chat")
def chat(req: ChatReq):
    # Detect intent and provide context
    msg = req.message.lower()
    context = ""

    # Build context based on query
    if any(word in msg for word in ["summary", "overview", "total", "ringkasan"]):
        data = get_sales_summary()
        context = f"Sales Summary Data: {data}\n\n"

    if any(word in msg for word in ["produk", "product", "barang", "item"]):
        data = get_top_products(10)
        context += f"Top Products Data: {data}\n\n"

    if any(word in msg for word in ["kategori", "category"]):
        data = get_sales_by_category()
        context += f"Category Data: {data}\n\n"

    if any(word in msg for word in ["customer", "pelanggan", "pembeli"]):
        data = get_top_customers(10)
        context += f"Top Customers Data: {data}\n\n"

    system_prompt = """You are a sales analytics assistant. 
    Answer questions about sales data based on the provided context.
    Be concise and provide actionable insights.
    If you mention numbers, format them nicely with thousand separators.
    Respond in Indonesian if the question is in Indonesian, English otherwise."""

    user_prompt = context + req.message

    reply = call_openrouter(system_prompt, user_prompt)
    return {"reply": reply}

@router.get("/analytics/summary")
def analytics_summary():
    return get_sales_summary()

@router.get("/analytics/top-products")
def analytics_top_products(limit: int = 10):
    return get_top_products(limit)

@router.get("/analytics/categories")
def analytics_categories():
    return get_sales_by_category()

@router.get("/analytics/trend")
def analytics_trend(period: str = 'month'):
    return get_sales_trend(period)

@router.get("/analytics/top-customers")
def analytics_top_customers(limit: int = 10):
    return get_top_customers(limit)

@router.get("/analytics/payment-methods")
def analytics_payment_methods():
    return get_payment_methods()
