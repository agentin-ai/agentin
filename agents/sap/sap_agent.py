from core.base_agent import EnterpriseAgent
import pyrfc

class SAPAgent(EnterpriseAgent):
    def __init__(self, credentials):
        super().__init__(credentials)
        self.connection = None
    
    async def authenticate(self):
        self.connection = pyrfc.Connection(
            ashost=self.credentials['host'],
            sysnr=self.credentials['system_number'],
            client=self.credentials['client'],
            user=self.credentials['user'],
            passwd=self.credentials['password']
        )
    
    async def create_purchase_order(self, po_data):
        return await self.execute_action(
            "BAPI_PO_CREATE1",
            {
                "PURCHASEORDER_HEADER": po_data["header"],
                "PURCHASEORDER_ITEMS": po_data["items"]
            }
        ) 