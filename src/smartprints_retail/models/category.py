from datetime import datetime
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel


class Category(SmartprintsBaseModel):
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    created_by: Optional[str] = Field(None, alias="createdBy")
    modified_by: Optional[str] = Field(None, alias="modifiedBy")
    id: Optional[int] = Field(None, alias="idCATEGORY")
    description: Optional[str] = None
    position: Optional[int] = None
    name: Optional[str] = None
    status: Optional[str] = None
    name_ar: Optional[str] = None
    description_ar: Optional[str] = None
    tags: Optional[str] = None
    odoo_id: Optional[int] = Field(None, alias="odooId")
    parent_category_name: Optional[str] = Field(None, alias="parentCategoryName")
    parent_category_id: Optional[int] = Field(None, alias="parentCategoryId")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")
