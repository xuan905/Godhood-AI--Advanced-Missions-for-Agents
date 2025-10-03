# 功能：設定長短期目標與 Reward 函數
# 修仙隱喻：修士立下修煉大計

class GoalManager:
    def __init__(self):
        self.long_term_goals = []
        self.short_term_goals = []

    def add_goal(self, goal, type="short"):
        if type == "short":
            self.short_term_goals.append(goal)
        else:
            self.long_term_goals.append(goal)

    def list_goals(self):
        return {"short": self.short_term_goals, "long": self.long_term_goals}

    def evaluate_goal(self, goal):
        # 假設回傳簡單分數，實際可結合 memory/knowledge
        return 1
