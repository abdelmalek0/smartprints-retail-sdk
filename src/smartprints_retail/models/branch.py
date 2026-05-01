from datetime import datetime
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel


class Branch(SmartprintsBaseModel):
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    created_by: Optional[str] = Field(None, alias="createdBy")
    modified_by: Optional[str] = Field(None, alias="modifiedBy")
    id: Optional[int] = Field(None, alias="idINVENTORY")
    address: Optional[str] = None
    city: Optional[str] = None
    location: Optional[str] = None
    name: Optional[str] = None
    name_ar: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None
    with_shelves: Optional[bool] = Field(None, alias="withShelves")
    has_automation: Optional[bool] = Field(None, alias="hasAutomation")
    client_name: Optional[str] = Field(None, alias="clientName")
    client_name_ar: Optional[str] = Field(None, alias="clientName_ar")
    client_id: Optional[int] = Field(None, alias="clientId")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")
