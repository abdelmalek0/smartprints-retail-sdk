from typing import Optional

from smartprints_core.client import BaseClient

from .api.user import UserAPI
from .api.discovery import DiscoveryAPI
from .api.orders import OrdersAPI
from .api.stock_status import StockStatusAPI

class SmartRetailClient(BaseClient):
    """Integrated client for Retail POS operations."""

    def _construct_base_url(self, environment: str, version: Optional[str]) -> str:
        if environment == "dev":
            return "https://api-retail-dev.smartprints-ksa.com"
        return "https://api-retail.smartprints-ksa.com"

    def __init__(
        self, 
        token: Optional[str] = None, 
        environment: str = "prod",
        version: Optional[str] = None,
        **kwargs
    ):
        super().__init__(token=token, environment=environment, version=version, **kwargs)
        self.user = UserAPI(self)
        self.discovery = DiscoveryAPI(self)
        self.orders = OrdersAPI(self)
        self.stock_status = StockStatusAPI(self)
