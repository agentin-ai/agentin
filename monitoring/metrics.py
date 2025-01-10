from prometheus_client import Counter, Histogram
import time

class AgentMetrics:
    def __init__(self):
        self.action_counter = Counter(
            'agent_actions_total',
            'Total number of agent actions',
            ['agent_type', 'action_type']
        )
        
        self.action_duration = Histogram(
            'agent_action_duration_seconds',
            'Time spent processing agent actions',
            ['agent_type', 'action_type']
        )
    
    def record_action(self, agent_type: str, action_type: str):
        self.action_counter.labels(
            agent_type=agent_type,
            action_type=action_type
        ).inc()
    
    @contextmanager
    def measure_duration(self, agent_type: str, action_type: str):
        start_time = time.time()
        try:
            yield
        finally:
            duration = time.time() - start_time
            self.action_duration.labels(
                agent_type=agent_type,
                action_type=action_type
            ).observe(duration) 