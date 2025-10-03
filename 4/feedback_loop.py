# 功能：策略回饋
# 修仙隱喻：元神感悟修煉法則，自動調整仙法

from action_logger import get_recent_actions

class FeedbackLoop:
    def __init__(self, agent_name):
        self.agent_name = agent_name

    def evaluate(self):
        recent = get_recent_actions(self.agent_name, n=5)
        for act in recent:
            print(f"[回饋] {self.agent_name} 最近行動：{act['action']} -> {act['detail']}")
