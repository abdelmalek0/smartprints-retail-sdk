from smartprints_core.client import BaseClient

from ..models.user import Userdb


class UserAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    async def find_user_by_username(self, username: str) -> Userdb:
        data = await self.client.get("userdbs/search/findByUsername", params={"username": username})
        return Userdb.model_validate(data)