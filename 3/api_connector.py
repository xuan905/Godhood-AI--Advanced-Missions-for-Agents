# 功能：串接外部 API 與數據服務
# 修仙隱喻：元神與天界靈脈溝通，收集靈氣與資源
"""
pip install requests
"""
import requests

class APIConnector:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self, endpoint, params=None):
        """從 API 獲取資料"""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            print(f"[APIConnector] 元神接收靈脈訊息：{endpoint}")
            return response.json()
        except Exception as e:
            print(f"[APIConnector] 連線失敗：{e}")
            return None
