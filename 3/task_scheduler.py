# 功能：任務排程與多工具協作
# 修仙隱喻：元神分神施法，各法寶同時運轉

import threading

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, func, *args, **kwargs):
        """新增任務"""
        self.tasks.append((func, args, kwargs))
        print(f"[TaskScheduler] 任務加入隊列")

    def run_all(self):
        """同時執行所有任務"""
        threads = []
        for func, args, kwargs in self.tasks:
            t = threading.Thread(target=func, args=args, kwargs=kwargs)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        print("[TaskScheduler] 所有法寶施展完成")
        self.tasks.clear()
