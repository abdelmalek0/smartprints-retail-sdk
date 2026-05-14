from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel


class Product(SmartprintsBaseModel):
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    created_by: Optional[str] = Field(None, alias="createdBy")
    modified_by: Optional[str] = Field(None, alias="modifiedBy")
    id: Optional[int] = Field(None, alias="idPRODUCT")
    name: Optional[str] = None
    name_ar: Optional[str] = None
    description: Optional[str] = None
    description_ar: Optional[str] = None
    price: Optional[float] = None
    buying_price: Optional[float] = Field(None, alias="buyingPrice")
    wap: Optional[float] = None
    status: Optional[str] = None
    barcode: Optional[str] = None
    list_barcodes: Optional[str] = Field(None, alias="listBarcodes")
    ref: Optional[str] = None
    tags: Optional[str] = None
    color: Optional[str] = None
    image_id: Optional[str] = Field(None, alias="imageId")
    position: Optional[int] = None
    weight: Optional[float] = None
    volume: Optional[float] = None
    vat: Optional[float] = None
    pack: Optional[int] = None
    qty: Optional[int] = None
    old_qty: Optional[int] = Field(None, alias="oldQty")
    min_qty: Optional[int] = Field(None, alias="minQty")
    capacity_min: Optional[int] = Field(None, alias="capacityMin")
    capacity_max: Optional[int] = Field(None, alias="capacityMax")
    buying_package: Optional[int] = Field(None, alias="buyingPackage")
    odoo_id: Optional[int] = Field(None, alias="odooId")
    odoo_template_id: Optional[int] = Field(None, alias="odooTemplateId")
    odoo_tax_id: Optional[int] = Field(None, alias="odooTaxId")
    odoo_price_include: Optional[bool] = Field(None, alias="odooPriceInclude")
    category_id: Optional[int] = Field(None, alias="categoryId")
    category_name: Optional[str] = Field(None, alias="categoryName")
    category_odoo_id: Optional[int] = Field(None, alias="categoryOdooId")
    manual_display: Optional[bool] = Field(None, alias="manualDisplay")
    composite: Optional[bool] = None
    discountable: Optional[bool] = None
    last_import: Optional[datetime] = None
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")
