from typing import Optional, Any
from datetime import datetime
from pydantic import Field
from smartprints_core.models import SmartprintsBaseModel

class ExportSalesProduct(SmartprintsBaseModel):
    unitary_product_id: Optional[int] = Field(None, alias="unitaryProductId")
    discount_employee_coupon: Optional[str] = Field(None, alias="discountEmployeeCoupon")
    vat_amount: Optional[float] = Field(None, alias="vatAmount")
    city: Optional[str] = None
    cus_name: Optional[str] = Field(None, alias="cusName")
    mada_receipt_amount: Optional[str] = Field(None, alias="madaReceiptAmount")
    discount: Optional[str] = None
    device_name: Optional[str] = Field(None, alias="deviceName")
    product_name: Optional[str] = Field(None, alias="productName")
    product_name_ar: Optional[str] = Field(None, alias="productName_ar")
    category_name: Optional[str] = Field(None, alias="categoryName")
    category_name_ar: Optional[str] = Field(None, alias="categoryName_ar")
    composite: Optional[bool] = None
    device_ref: Optional[str] = Field(None, alias="deviceRef")
    product_id_str: Optional[str] = Field(None, alias="productId")
    id_inventory: Optional[int] = Field(None, alias="idINVENTORY")
    vat_percent: Optional[str] = Field(None, alias="vat")
    product_status: Optional[str] = Field(None, alias="productStatus")
    cus_code: Optional[str] = Field(None, alias="cusCode")
    invoice_no: Optional[str] = Field(None, alias="InvoiceNo")
    total_sales_amount: Optional[float] = Field(None, alias="totalSalesAmount")
    pack: Optional[int] = None
    date: Optional[str] = Field(None, alias="Date") # Using str because format might vary, or I can use datetime
    route: Optional[str] = None
    product_code: Optional[str] = Field(None, alias="productCode")
    id_product: Optional[int] = Field(None, alias="idPRODUCT")
    product_barcode: Optional[str] = Field(None, alias="productBarcode")
    sales_qty: Optional[float] = Field(None, alias="salesQty")
    sales_price_without_vat: Optional[float] = Field(None, alias="salesPriceWithoutVat")
    payment_type: Optional[str] = Field(None, alias="payment_type")
    status: Optional[str] = None
