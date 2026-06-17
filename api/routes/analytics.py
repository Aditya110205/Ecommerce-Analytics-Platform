from fastapi import APIRouter

from api.services.analytics_service import (
    get_daily_revenue,
    get_top_products,
    get_top_customers,
    get_monthly_sales
)

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.get("/daily-revenue")
def daily_revenue():
    return get_daily_revenue()


@router.get("/top-products")
def top_products():
    return get_top_products()


@router.get("/top-customers")
def top_customers():
    return get_top_customers()


@router.get("/monthly-sales")
def monthly_sales():
    return get_monthly_sales()