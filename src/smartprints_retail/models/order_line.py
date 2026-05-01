from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel

class OrderLine(SmartprintsBaseModel):
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    id: Optional[int] = Field(None, alias="idORDERLINE")
    amount: Optional[float] = None
    quantity: Optional[float] = None
    ref: Optional[str] = None
    status: Optional[str] = None
    note: Optional[str] = None
    old_qty: Optional[float] = Field(None, alias="oldQty")
    deleted: Optional[bool] = None
    old: Optional[bool] = None
    old_id: Optional[int] = Field(None, alias="oldId")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")
