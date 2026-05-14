from typing import List

from smartprints_core.client import BaseClient

from ..models.stock_status import StockStatus


class StockStatusAPI:
    """Wraps the retail /stockStatus/search/findByClient endpoint."""

    def __init__(self, client: BaseClient):
        self.client = client

    async def find_by_client(self, client_id: int) -> List[StockStatus]:
        """Fetch all stock status records for a given client.

        Args:
            client_id: The ``idCLIENT`` to filter by.

        Returns:
            A flat list of :class:`StockStatus` objects.
        """
        data = await self.client.get(
            "stockStatus/search/findByClient",
            params={"idCLIENT": client_id},
        )

        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            embedded = data.get("_embedded", {})
            items = embedded.get("stockStatus", data.get("content", []))
        else:
            items = []

        return [StockStatus.model_validate(item) for item in items]
