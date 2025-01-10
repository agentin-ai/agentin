from typing import List, Dict, Any
from core.base_agent import EnterpriseAgent
import openai

class BusinessProcessAgent:
    def __init__(self, agents: Dict[str, EnterpriseAgent]):
        self.agents = agents
        self.llm = openai.Client()
    
    async def handle_employee_onboarding(self, employee_data: Dict[str, Any]):
        # Create employee in Workday
        workday_employee = await self.agents["workday"].create_employee(employee_data)
        
        # Create user in ServiceNow
        snow_user = await self.agents["servicenow"].create_user({
            "employee_id": workday_employee["id"],
            "email": employee_data["email"]
        })
        
        # Create Salesforce user if sales role
        if employee_data["department"] == "Sales":
            sf_user = await self.agents["salesforce"].create_user({
                "email": employee_data["email"],
                "profile": "Sales_User"
            })
        
        return {
            "workday_id": workday_employee["id"],
            "servicenow_id": snow_user["sys_id"],
            "salesforce_id": sf_user.get("id") if "sf_user" in locals() else None
        } 