# 功能：任務拆解與 DAG 排程
# 修仙隱喻：元神分解心法步驟

class PlanBuilder:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, dependencies=None):
        self.tasks.append({"task": task, "dependencies": dependencies or []})

    def build_plan(self):
        # 返回依賴順序列表，簡單示範
        plan = [t["task"] for t in self.tasks]
        return plan
