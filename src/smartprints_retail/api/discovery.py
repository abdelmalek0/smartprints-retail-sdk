from typing import List
from smartprints_core.client import BaseClient
from ..models.client import Client
from ..models.category import Category
from ..models.branch import Branch
from ..models.payment import PaymentMethod


class DiscoveryAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    async def fetch_client_info(self, client_id: int) -> Client:
        return await self.client.get(f"client/{client_id}", response_model=Client)

    async def fetch_client_categories(self, client_id: int) -> List[Category]:
        data = await self.client.get(f"client/{client_id}/categories")
        categories = data.get("_embedded", {}).get("category", []) if isinstance(data, dict) else []
        return [Category.model_validate(c) for c in categories]

    async def fetch_client_branches(self, client_id: int) -> List[Branch]:
        data = await self.client.get(f"client/{client_id}/branches")
        branches = data.get("_embedded", {}).get("branch", []) if isinstance(data, dict) else []
        return [Branch.model_validate(b) for b in branches]

    async def fetch_payment_methods(self, client_id: int) -> List[PaymentMethod]:
        data = await self.client.get(f"client/{client_id}/paymentMethods")
        methods = data.get("_embedded", {}).get("paymentMethod", []) if isinstance(data, dict) else []
        return [PaymentMethod.model_validate(p) for p in methods]
