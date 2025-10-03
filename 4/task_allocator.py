# 功能：任務分派與優先級管理
# 修仙隱喻：門派長老分派修煉法門

class TaskAllocator:
    def __init__(self):
        self.tasks = []

    def add_task(self, agent, task, priority=1):
        self.tasks.append({"agent": agent, "task": task, "priority": priority})
        print(f"[任務分派] {agent} 接收任務：{task} (優先級 {priority})")

    def get_tasks(self, agent_name):
        return [t for t in self.tasks if t["agent"] == agent_name]
