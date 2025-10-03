# simulation.py
# 功能：整合 Goal → Plan → Act → Learn 模組，模擬仙界 Agent 修煉
# 修仙隱喻：元神自主修煉，累積經驗，悟出高級仙法

from goal_manager import GoalManager
from plan_builder import PlanBuilder
from autonomous_actor import AutonomousActor
from feedback_updater import FeedbackUpdater
from goal_monitor import GoalMonitor
from action_logger import log_action

# 初始化模組
agent_name = "仙界高階Agent"
goal_manager = GoalManager()
plan_builder = PlanBuilder()
actor = AutonomousActor(agent_name)
feedback = FeedbackUpdater()
monitor = GoalMonitor()

# 1️⃣ 設定長短期目標
goal_manager.add_goal("收集靈石10顆", type="short")
goal_manager.add_goal("完成靈脈探索", type="short")
goal_manager.add_goal("建構知識圖譜", type="long")
goal_manager.add_goal("自主學習高級仙法", type="long")

# 2️⃣ 拆解計畫
for g_type, goals in goal_manager.list_goals().items():
    for goal in goals:
        plan_builder.add_task(goal)

plan = plan_builder.build_plan()
log_action(agent_name, "計畫生成", f"完整修煉計畫：{plan}")

# 3️⃣ 多回合自主修煉
rounds = 3
for r in range(1, rounds + 1):
    print(f"\n=== 修煉回合 {r} ===")
    for task in plan:
        result = actor.execute_task(task)
        # 4️⃣ 回饋更新
        feedback.update_strategy(task, f"成功-{r}")
    # 5️⃣ 追蹤進度
    progress = monitor.track_progress()
    print(f"[回合 {r}] 修煉進度：{progress}")

# 6️⃣ 修煉結束，查看近期行動
from action_logger import get_recent_actions
recent = get_recent_actions(10)
print("\n=== 最近行動紀錄 ===")
for act in recent:
    print(f"{act['time']} | {act['agent']} | {act['action']} -> {act['detail']}")

# 7️⃣ 可視化知識圖譜
feedback.knowledge.visualize()
