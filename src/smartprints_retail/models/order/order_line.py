from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel
from ..product import Product


class Shelf(SmartprintsBaseModel):
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    created_by: Optional[str] = Field(None, alias="createdBy")
    modified_by: Optional[str] = Field(None, alias="modifiedBy")
    id: Optional[int] = Field(None, alias="idINVENTORY")
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    number: Optional[str] = None
    notes: Optional[str] = None
    coordinates: Optional[str] = None
    capacity: Optional[int] = None
    branch_id: Optional[int] = Field(None, alias="branchId")
    branch_name: Optional[str] = Field(None, alias="branchName")
    client_id: Optional[int] = Field(None, alias="clientId")
    client_name: Optional[str] = Field(None, alias="clientName")
    product_id: Optional[int] = Field(None, alias="productId")
    product_name: Optional[str] = Field(None, alias="productName")
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")


class OrderLine(SmartprintsBaseModel):
    id: Optional[int] = Field(None, alias="idORDERLINE")
    amount: Optional[float] = None
    quantity: Optional[float] = None
    discount: Optional[float] = None
    discount_employee_coupon: Optional[float] = Field(None, alias="discountEmployeeCoupon")
    qte_served: Optional[int] = Field(None, alias="qteServed")
    ref: Optional[str] = None
    status: Optional[str] = None
    note: Optional[str] = None
    log: Optional[Any] = None
    old_qty: Optional[float] = Field(None, alias="oldQty")
    deleted: Optional[bool] = None
    old: Optional[bool] = None
    old_id: Optional[int] = Field(None, alias="oldId")
    shelf_id: Optional[int] = Field(None, alias="shelfId")
    shelf: Optional[Shelf] = None
    product: Optional[Product] = None
    links: Optional[Dict[str, Any]] = Field(None, alias="_links")
