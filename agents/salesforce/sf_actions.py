from typing import Dict, Any
from core.base_agent import EnterpriseAgent

class SalesforceActions:
    def __init__(self, agent: EnterpriseAgent):
        self.agent = agent
    
    async def create_opportunity(self, data: Dict[str, Any]):
        return await self.agent.execute_action(
            "CREATE_OPPORTUNITY",
            {
                "Name": data["name"],
                "Amount": data["amount"],
                "StageName": data["stage"],
                "CloseDate": data["close_date"]
            }
        )
    
    async def update_account(self, account_id: str, data: Dict[str, Any]):
        return await self.agent.execute_action(
            "UPDATE_ACCOUNT",
            {
                "Id": account_id,
                **data
            }
        ) 