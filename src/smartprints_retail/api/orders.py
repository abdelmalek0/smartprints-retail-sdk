from typing import List
from smartprints_core.client import BaseClient
from ..models.order import Order, OrderSearchRequest, OrderLine
from ..models.product import Product

class OrdersAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    async def search_orders(self, params: OrderSearchRequest) -> List[Order]:
        data = await self.client.get(
            "order/search/searchOrders", 
            params=params.model_dump(by_alias=True, exclude_none=True)
        )
        orders = data.get("_embedded", {}).get("order", []) if isinstance(data, dict) else []
        return [Order.model_validate(o) for o in orders]

    async def fetch_orderlines(self, order_id: int) -> List[OrderLine]:
        data = await self.client.get(f"order/{order_id}/orderlines")
        lines = data.get("_embedded", {}).get("orderline", []) if isinstance(data, dict) else data
        return [OrderLine.model_validate(l) for l in lines]

    async def fetch_orderline_product(self, orderline_id: int) -> Product:
        data = await self.client.get(f"orderline/{orderline_id}/product")
        return Product.model_validate(data)
