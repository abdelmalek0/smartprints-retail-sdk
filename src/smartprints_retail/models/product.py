from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel

class Product(SmartprintsBaseModel):
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    id: Optional[int] = Field(None, alias="idPRODUCT")
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    status: Optional[str] = None
    barcode: Optional[str] = None
    name_ar: Optional[str] = None
    description_ar: Optional[str] = None
    image_path: Optional[str] = Field(None, alias="imagePath")
    category_id: Optional[int] = Field(None, alias="categoryId")
    category_name: Optional[str] = Field(None, alias="categoryName")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")
