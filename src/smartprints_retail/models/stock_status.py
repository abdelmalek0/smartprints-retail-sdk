from typing import Any, Dict, Optional

from pydantic import Field

from smartprints_core.models import SmartprintsBaseModel


class StockStatus(SmartprintsBaseModel):
    """A single stock status record returned by /stockStatus/search/findByClient."""

    id: Optional[int] = Field(None, alias="idSTOCKSTATUS")
    qty: Optional[float] = None

    product_id: Optional[int] = Field(None, alias="productId")
    product_name: Optional[str] = Field(None, alias="productName")
    product_ref: Optional[str] = Field(None, alias="productRef")

    inventory_id: Optional[int] = Field(None, alias="inventoryId")
    inventory_name: Optional[str] = Field(None, alias="inventoryName")

    category_id: Optional[int] = Field(None, alias="categoryId")

    links: Optional[Dict[str, Any]] = Field(None, alias="_links")
