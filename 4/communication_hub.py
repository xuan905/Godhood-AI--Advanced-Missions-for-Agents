# 功能：多 Agent 間通訊
# 修仙隱喻：仙界傳訊陣，元神互通

class CommunicationHub:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, content):
        self.messages.append({"from": sender, "to": receiver, "content": content})
        print(f"[訊息] {sender} -> {receiver}: {content}")

    def receive_messages(self, agent_name):
        inbox = [m for m in self.messages if m["to"] == agent_name]
        return inbox
