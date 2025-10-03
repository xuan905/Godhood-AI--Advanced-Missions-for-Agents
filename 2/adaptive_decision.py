# adaptive_decision.py
# 功能：根據記憶與知識，自動調整行動策略
# 修仙隱喻：元神領悟新法術，自動施展最優仙法

"""
特點：

自動調整策略：根據歷史行動成功率 + 知識圖譜評估

仙界隱喻：元神領悟新法術，自動施展最優仙法

支援策略紀錄 (strategy_log)，方便後續分析與優化
"""

from memory_query import query_actions
from knowledge_graph import KnowledgeGraph  # 假設已實作知識圖譜

class AdaptiveDecisionAgent:
    def __init__(self, name):
        self.name = name
        self.knowledge = KnowledgeGraph()
        self.strategy_log = []

    def evaluate_options(self, options):
        """
        根據歷史行動與知識圖譜評估選項
        :param options: 行動選項列表，如 ["探索靈脈", "修煉法術", "採集靈石"]
        :return: 最佳行動
        """
        scores = {}
        for action in options:
            past_actions = query_actions(agent_name=self.name, action_type=action)
            past_success = sum(a.get("success", 0) for a in past_actions)
            # 知識圖譜加分
            knowledge_score = self.knowledge.evaluate_action(action)
            scores[action] = past_success + knowledge_score
        # 選擇分數最高的行動
        best_action = max(scores, key=scores.get)
        self.strategy_log.append({"action": best_action, "scores": scores})
        return best_action

    def act(self, options):
        """決策並執行行動"""
        best = self.evaluate_options(options)
        print(f"[{self.name}] 元神領悟最佳仙法，施展行動：{best}")
        return best

# 範例測試
if __name__ == "__main__":
    agent = AdaptiveDecisionAgent("高階Agent")
    options = ["探索靈脈", "修煉法術", "採集靈石"]
    for _ in range(3):
        agent.act(options)
