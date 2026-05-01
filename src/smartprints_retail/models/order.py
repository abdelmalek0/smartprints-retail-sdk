from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import Field, field_validator
from smartprints_core.models import SmartprintsBaseModel

class Order(SmartprintsBaseModel):
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    created_by: Optional[str] = Field(None, alias="createdBy")
    modified_by: Optional[str] = Field(None, alias="modifiedBy")
    id: Optional[int] = Field(None, alias="idORDER")
    vat: Optional[float] = None
    total: Optional[float] = None
    subtotal: Optional[float] = None
    date: Optional[datetime] = None
    business_day: Optional[datetime] = Field(None, alias="businessDay")
    date_complete: Optional[datetime] = Field(None, alias="date_complete")
    lang: Optional[str] = None
    payment_ref: Optional[str] = Field(None, alias="payment_ref")
    payment_type: Optional[str] = Field(None, alias="payment_type")
    takeout: Optional[int] = None
    sync: Optional[bool] = None
    ticket_number: Optional[str] = Field(None, alias="ticket_number")
    discount_total: Optional[float] = Field(None, alias="discountTotal")
    status: Optional[str] = None
    order_uuid: Optional[str] = Field(None, alias="order_uuid")
    client_id: Optional[int] = Field(None, alias="clientId")
    client_name: Optional[str] = Field(None, alias="clientName")
    branch_name: Optional[str] = Field(None, alias="branchName")
    branch_id: Optional[int] = Field(None, alias="branchId")
    kiosk_name: Optional[str] = Field(None, alias="kioskName")
    kiosk_id: Optional[int] = Field(None, alias="kioskId")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")

class OrderSearchRequest(SmartprintsBaseModel):
    start: str = Field(description="Start date in HTTP-date string format (e.g., 'Wed, 01 May 2026 00:00:00 GMT')")
    end: str = Field(description="End date in HTTP-date string format (e.g., 'Fri, 30 Apr 2026 23:59:59 GMT')")
    id_client: int = Field(0, alias="idCLIENT")
    id_inventory: int = Field(0, alias="idINVENTORY")
    id_kiosk: int = Field(0, alias="idKIOSK")
    id_payment_method: int = Field(0, alias="idPAYMENT_METHOD")
    fraud_detected: str = Field("", alias="fraudDetected")
    real_fraud: str = Field("", alias="realFraud")
    status: str = ""
    sync: str = ""
    page: int = 0
    size: int = 1000
    sort: str = "idORDER,desc"

    @field_validator('start', 'end')
    @classmethod
    def validate_http_date(cls, v):
        if not isinstance(v, str) or "," not in v or "GMT" not in v:
            raise ValueError("start and end must be HTTP-date strings, e.g., 'Wed, 01 May 2026 00:00:00 GMT'")
        return v
