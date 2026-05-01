from typing import Optional

from smartprints_core.client import BaseClient

from .api.user import UserAPI

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
