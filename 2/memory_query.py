# memory_query.py
# 功能：查詢歷史事件與行動，提供決策參考
# 修仙隱喻：元神心眼，瞬間回顧過往修煉心得

"""
特點：

支援 多條件查詢：Agent/玩家名稱、行動類型、最近 n 條

仙界隱喻：元神心眼，可瞬間回顧過往修煉心得

與 action_logger.py 無縫整合，便於 AI 策略決策

範例測試展示不同查詢方式
"""

import json
import os

LOG_FILE = "action_log.json"

# 讀取歷史行動紀錄
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        action_log = json.load(f)
else:
    action_log = []

def query_actions(agent_name=None, action_type=None, last_n=None):
    """
    查詢行動紀錄
    :param agent_name: 指定 Agent 或玩家名稱
    :param action_type: 指定行動類型
    :param last_n: 只取最近 n 條
    :return: 過濾後的行動列表
    """
    results = action_log

    if agent_name:
        results = [a for a in results if a["agent"] == agent_name]
    if action_type:
        results = [a for a in results if a["action"] == action_type]
    if last_n:
        results = results[-last_n:]
    return results

def print_recent(agent_name=None, action_type=None, last_n=5):
    """列印最近行動紀錄"""
    records = query_actions(agent_name, action_type, last_n)
    if not records:
        print("無相關行動紀錄。")
        return
    print(f"最近 {len(records)} 條行動紀錄：")
    for r in records:
        print(f"[{r['time']}] {r['agent']} 行動：{r['action']} -> {r['detail']}")

# 範例測試
if __name__ == "__main__":
    print_recent(last_n=3)
    print_recent(agent_name="高階Agent")
    print_recent(action_type="探索靈脈")
