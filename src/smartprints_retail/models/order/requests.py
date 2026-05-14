from typing import Optional, Union
from pydantic import Field, field_validator, ConfigDict
from smartprints_core.models import SmartprintsBaseModel
from .enums import OrderStatus


class OrderSearchRequest(SmartprintsBaseModel):
    start: str = Field(description="Start date in ISO 8601 format (e.g., '2026-04-01T00:00:00.000Z')")
    end: str = Field(description="End date in ISO 8601 format (e.g., '2026-04-30T23:59:59.999Z')")
    id_client: int = Field(0, alias="idCLIENT")
    id_inventory: int = Field(0, alias="idINVENTORY")
    id_kiosk: int = Field(0, alias="idKIOSK")
    id_payment_method: int = Field(0, alias="idPAYMENT_METHOD")
    fraud_detected: str = Field("0", alias="fraudDetected")
    real_fraud: str = Field("0", alias="realFraud")
    status: Union[OrderStatus, str] = "0"
    sync: str = "0"
    page: Optional[int] = None
    size: Optional[int] = None
    sort: str = "idORDER,desc"

    model_config = ConfigDict(populate_by_name=True)

    @field_validator('start', 'end')
    @classmethod
    def validate_iso_date(cls, v):
        if not isinstance(v, str) or "T" not in v:
            raise ValueError("start and end must be ISO 8601 strings, e.g., '2026-04-01T00:00:00.000Z'")
        return v


class ExportSalesInvoiceRequest(SmartprintsBaseModel):
    """Request parameters for exporting sales invoice products."""
    start_date: str = Field(..., alias="startDate", description="Start date in GMT format (e.g., 'Thu, 01 Apr 2026 00:00:00 GMT')")
    end_date: str = Field(..., alias="endDate", description="End date in GMT format (e.g., 'Thu, 30 Apr 2026 23:59:59 GMT')")
    id_client: int = Field(..., alias="idCLIENT")
    id_branch: int = Field(0, alias="idBRANCH")
    page: int = 0
    size: int = 1000

    model_config = ConfigDict(populate_by_name=True)