from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel


class PaymentMethod(SmartprintsBaseModel):
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    created_by: Optional[str] = Field(None, alias="createdBy")
    modified_by: Optional[str] = Field(None, alias="modifiedBy")
    id: Optional[int] = Field(None, alias="idPAYMENT_METHOD")
    name: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    odoo_id: Optional[int] = Field(None, alias="odooId")
    branch_ids: Optional[List[int]] = Field(None, alias="branchIds")
    old_id: Optional[int] = Field(None, alias="oldId")
    client_id: Optional[int] = Field(None, alias="clientId")
    client_name: Optional[str] = Field(None, alias="clientName")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")
