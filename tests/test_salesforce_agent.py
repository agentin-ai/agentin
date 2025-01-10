import pytest
from agents.salesforce.sf_agent import SalesforceAgent

@pytest.mark.asyncio
async def test_salesforce_opportunity_creation():
    agent = SalesforceAgent({
        "username": "test_user",
        "password": "test_pass",
        "security_token": "test_token"
    })
    
    opportunity_data = {
        "name": "Test Opportunity",
        "amount": 10000,
        "stage": "Prospecting",
        "close_date": "2024-12-31"
    }
    
    result = await agent.create_opportunity(opportunity_data)
    assert result["success"] == True
    assert result["id"] is not None 