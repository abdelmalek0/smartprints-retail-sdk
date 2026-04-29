from typing import Optional
from smartprints_core import CoreClient

class SmartRetailClient(CoreClient):
    """Integrated client for Retail POS operations."""

    def _construct_base_url(self, environment: str, version: Optional[str]) -> str:
        if environment == "dev":
            return "https://api-retail-dev.smartprints-ksa.com"
        return "https://api-retail.smartprints-ksa.com"

    def __init__(
        self, 
        token: Optional[str] = None, 
        base_url: Optional[str] = None,
        environment: str = "prod",
        version: Optional[str] = None,
        **kwargs
    ):
        super().__init__(token=token, base_url=base_url, environment=environment, version=version, **kwargs)
