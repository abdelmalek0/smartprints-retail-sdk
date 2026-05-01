from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel


class Userdb(SmartprintsBaseModel):
    branch_id: Optional[int] = Field(None, alias="branchId")
    branch_name: Optional[str] = Field(None, alias="branchName")
    client_id: Optional[int] = Field(None, alias="clientId")
    client_name: Optional[str] = Field(None, alias="clientName")
    id_branches: Optional[str] = Field(None, alias="idBRANCHES")
    id_user: Optional[int] = Field(None, alias="idUSER")
    kiosk_id: Optional[int] = Field(None, alias="kioskId")
    kiosk_name: Optional[str] = Field(None, alias="kioskName")
    password: Optional[str] = Field(None, alias="password")
    status: Optional[str] = Field(None, alias="status")
    user_type: Optional[str] = Field(None, alias="type")
    username: Optional[str] = Field(None, alias="username")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")