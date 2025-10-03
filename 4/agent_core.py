# 功能：定義高階 Agent 類別，管理修煉狀態、法力、任務
# 修仙隱喻：元神操控法力，自主施展仙法
from memory_system import MemorySystem
from action_logger import log_action
from knowledge_graph import KnowledgeGraph

class AgentCore:
    def __init__(self, name):
        self.name = name
        self.mana = 100  # 法力值
        self.memory = MemorySystem()
        self.knowledge = KnowledgeGraph()
    
    def perform_action(self, action, effect="未知效果"):
        log_action(self.name, action, effect)
        self.memory.remember_short({"action": action, "effect": effect})
        self.knowledge.add_relation(action, effect)
        print(f"[{self.name}] 施展仙法：{action} -> {effect}")
