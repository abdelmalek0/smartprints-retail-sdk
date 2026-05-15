from typing import Any, Dict, List
from smartprints_core.client import BaseClient
from ..models.order import Order, OrderSearchRequest, OrderLine, ExportSalesProduct, ExportSalesInvoiceRequest, ProductSalesStatsRequest, ProductSalesStat
from ..models.product import Product

PAGE_SIZE = 1000
EXPORT_PAGE_SIZE = 100000

class OrdersAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    async def search_orders(self, params: OrderSearchRequest) -> List[Order]:
        data = await self.client.get(
            "order/searchOrders",
            params=params.model_dump(by_alias=True, exclude_none=True)
        )
            
        orders = data.get("content", [])
        return [Order.model_validate(o) for o in orders]

    async def fetch_orderlines(self, order_id: int) -> List[OrderLine]:
        data = await self.client.get(f"order/{order_id}/orderlines")
        lines = data.get("_embedded", {}).get("orderline", []) if isinstance(data, dict) else data
        return [OrderLine.model_validate(l) for l in lines]

    async def fetch_orderline_product(self, orderline_id: int) -> Product:
        data = await self.client.get(f"orderline/{orderline_id}/product")
        return Product.model_validate(data)

    async def export_sales_products(
        self,
        request: ExportSalesInvoiceRequest
    ) -> List[ExportSalesProduct]:
        return await self.export_sales_invoice_products(request)

    async def export_sales_invoice_products(
        self,
        request: ExportSalesInvoiceRequest
    ) -> List[ExportSalesProduct]:
        data = await self.client.get(
            "export/salesInvoiceProducts",
            params=request.model_dump(by_alias=True, exclude_none=True)
        )
        content = data if isinstance(data, list) else data.get("content", data)
        return [ExportSalesProduct.model_validate(item) for item in content]

    async def get_products_sales_stats(
        self,
        request: ProductSalesStatsRequest
    ) -> List[ProductSalesStat]:
        data = await self.client.post(
            "order/getProductsSalesStats",
            data=request.model_dump(by_alias=True, exclude_none=True)
        )
        content = data if isinstance(data, list) else data.get("content", data)
        return [ProductSalesStat.model_validate(item) for item in content]

