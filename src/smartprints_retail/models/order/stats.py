from typing import Any, List, Optional
from pydantic import BaseModel, model_validator

class ProductSalesStat(BaseModel):
    client_id: Optional[int]
    branch_id: Optional[int]
    product_id: Optional[int]
    device_id: Optional[int]
    product_name: Optional[str]
    product_name_ar: Optional[str]
    ref: Optional[str]
    barcode: Optional[str]
    category_name: Optional[str]
    branch_name: Optional[str]
    qty_sold: Optional[float]
    unit_price: Optional[float]
    total_price: Optional[float]
    unknown_field: Any  # usually 0, meaning not sure yet

    @model_validator(mode='before')
    @classmethod
    def parse_from_list(cls, data: Any) -> Any:
        if isinstance(data, list) and len(data) >= 14:
            return {
                "client_id": data[0],
                "branch_id": data[1],
                "product_id": data[2],
                "device_id": data[3],
                "product_name": data[4],
                "product_name_ar": data[5],
                "ref": data[6],
                "barcode": data[7],
                "category_name": data[8],
                "branch_name": data[9],
                "qty_sold": data[10],
                "unit_price": data[11],
                "total_price": data[12],
                "unknown_field": data[13],
            }
        return data
