# action_logger.py
# 功能：記錄高階 Agent 行動，提供策略分析依據
# 修仙比喻：元神筆記，將修煉過程完整記錄，助於精進

import json
import os

JSON_FILE = "agent_actions.json"

# 先讀取既有紀錄，如果沒有則初始化空列表
if os.path.exists(JSON_FILE):
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        action_log = json.load(f)
else:
    action_log = []

def log_action(action_type, detail):
    """
    紀錄一次 Agent 行動
    :param action_type: 行動類型（探索/修煉/戰鬥/資源收集）
    :param detail: 具體內容（例如目標資源、法術、敵人）
    """
    entry = {'type': action_type, 'detail': detail}
    action_log.append(entry)
    print(f"[行動紀錄] {action_type} -> {detail}")
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(action_log, f, ensure_ascii=False, indent=2)

# 範例使用
if __name__ == "__main__":
    log_action("探索", "靈石洞窟")
    log_action("修煉", "煉化天地真氣")
    log_action("戰鬥", "擊退妖獸巡邏")
    log_action("資源收集", "獲得法寶精華")
