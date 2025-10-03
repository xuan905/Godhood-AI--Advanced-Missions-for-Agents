# 功能：收集歷史行動，更新策略
# 修仙隱喻：回顧修煉筆記，悟出高級法術

from memory_system import MemorySystem
from knowledge_graph import KnowledgeGraph

class FeedbackUpdater:
    def __init__(self):
        self.memory = MemorySystem()
        self.knowledge = KnowledgeGraph()

    def update_strategy(self, action, outcome):
        # 記錄到短期記憶
        self.memory.remember_short({"action": action, "effect": outcome})
        # 自動更新知識圖譜
        self.knowledge.add_relation(action, outcome)
