# multi_task_agent.py
# 功能：高階 Agent 多任務處理系統
# 修仙比喻：元神分神，並行修煉多種仙法法術

import threading
import time

class MultiTaskAgent:
    def __init__(self, name):
        self.name = name
        self.tasks = []  # 任務列表
        print(f"[Agent初始化] {self.name} 元神覺醒，準備分神修煉")

    def add_task(self, task_name, duration):
        """新增任務到任務列表"""
        self.tasks.append({'task': task_name, 'duration': duration})
        print(f"[任務加入] {task_name}，預計修煉時間 {duration}s")

    def _execute_task(self, task):
        """內部方法：執行單個任務"""
        print(f"[開始修煉] {task['task']}...")
        time.sleep(task['duration'])  # 模擬修煉耗時
        print(f"[完成修煉] {task['task']} 修煉結束")

    def run_tasks(self):
        """同時處理所有任務"""
        threads = []
        for task in self.tasks:
            t = threading.Thread(target=self._execute_task, args=(task,))
            t.start()
            threads.append(t)

        # 等待所有任務完成
        for t in threads:
            t.join()

        print(f"[任務完成] {self.name} 元神所有分神任務結束")

# 範例使用
if __name__ == "__main__":
    agent = MultiTaskAgent("玄靈元神")
    
    # 分神任務
    agent.add_task("吸收天地靈氣", 2)
    agent.add_task("練習火系仙法", 3)
    agent.add_task("鍛鍊劍道心法", 1)

    # 執行任務
    agent.run_tasks()
