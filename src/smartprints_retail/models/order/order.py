from .order_line import OrderLine
from datetime import datetime
from typing import Any, Dict, Optional, List
from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel
from .enums import OrderStatus


class OrderBase(SmartprintsBaseModel):
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    created_by: Optional[str] = Field(None, alias="createdBy")
    modified_by: Optional[str] = Field(None, alias="modifiedBy")
    id: Optional[int] = Field(None, alias="idORDER")
    vat: Optional[float] = None
    total: Optional[float] = None
    subtotal: Optional[float] = None
    date: Optional[datetime] = None
    lang: Optional[str] = None
    # API returns both snake_case and camelCase for these
    payment_ref: Optional[str] = Field(None, alias="payment_ref")
    payment_type: Optional[str] = Field(None, alias="payment_type")
    payment_ref_camel: Optional[str] = Field(None, alias="paymentRef")
    payment_type_camel: Optional[str] = Field(None, alias="paymentType")
    status: Optional[OrderStatus] = None
    discount_total: Optional[float] = Field(None, alias="discountTotal")
    sync: Optional[bool] = None
    log: Optional[Any] = None
    external_reference: Optional[str] = Field(None, alias="externalReference")
    ticket_number: Optional[str] = Field(None, alias="ticket_number")
    xml: Optional[str] = None
    zatca_error: Optional[str] = Field(None, alias="zatcaError")
    zatca_status: Optional[str] = Field(None, alias="zatcaStatus")
    icv: Optional[str] = None
    ih: Optional[str] = None
    qr: Optional[str] = None
    fraud_detected: Optional[bool] = Field(None, alias="fraudDetected")
    real_fraud: Optional[bool] = Field(None, alias="realFraud")
    video_url: Optional[str] = Field(None, alias="videoUrl")
    reason: Optional[str] = None
    error_discount: Optional[bool] = Field(None, alias="errorDiscount")
    shift_id: Optional[int] = Field(None, alias="shiftId")
    client_name: Optional[str] = Field(None, alias="clientName")
    branch_name: Optional[str] = Field(None, alias="branchName")
    branch_id: Optional[int] = Field(None, alias="branchId")
    kiosk_name: Optional[str] = Field(None, alias="kioskName")
    kiosk_id: Optional[int] = Field(None, alias="kioskId")
    bought_qty: Optional[int] = Field(None, alias="boughtQty")
    expected_qty: Optional[int] = Field(None, alias="expectedQty")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")


class Order(OrderBase):
    customer: Optional[Any] = None
    orderlines: Optional[List[OrderLine]] = None
    employee_coupon_orders: Optional[List[Any]] = Field(None, alias="employeeCouponOrders")
    offer_orders: Optional[List[Any]] = Field(None, alias="offerOrders")
    shift: Optional[Any] = None
    payments: Optional[List[Any]] = None