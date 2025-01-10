from typing import Dict, Any
import openai

class IncidentManager:
    def __init__(self, snow_agent):
        self.agent = snow_agent
        self.llm = openai.Client()
    
    async def process_incident(self, incident_data: Dict[str, Any]):
        # Analyze incident using AI
        analysis = await self._analyze_with_ai(incident_data)
        
        # Create incident with AI-generated categorization
        incident = await self.agent.create_incident({
            "short_description": analysis["summary"],
            "priority": analysis["priority"],
            "category": analysis["category"],
            "assignment_group": analysis["assignment_group"]
        })
        
        # Generate and attach AI solution recommendations
        solutions = await self._generate_solutions(incident_data)
        await self.agent.update_incident(
            incident["sys_id"],
            {"work_notes": solutions["recommendations"]}
        )
        
        return incident 