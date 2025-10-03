# Surviving Zombies with AI

簡易的 Python 安裝與虛擬環境建立教學（繁體中文）。

 # Surviving Zombies with AI

簡潔、依序且為新手友善的快速上手說明（繁體中文）。本 README 以「一步一步」的方式把必要的安裝、虛擬環境建立、依賴安裝與快速驗證流程整理出來，讓剛接觸 Python 的使用者也能順利啟動專案。

## 一、快速上手（3 分鐘試跑）

如果你只想短時間內試跑，請依照下面三個步驟：

1. 安裝 Python（選擇適合你的作業系統），或使用線上平台快速執行（參見下方「線上執行 Python」章節）。
2. 在專案資料夾中建立並啟用虛擬環境：

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
```

3. 安裝依賴並執行測試：

```bash
python -m pip install -r requirements.txt
python - <<'PY'
import requests
print('requests ok') if hasattr(__import__('requests'), 'get') else print('requests not found')
PY
```

（若你沒有安裝 `requests` 或想跳過，README 中也有線上平台可直接執行程式。）

## 二、安裝 Python（依作業系統）

推薦使用 Python 3.11 或 3.12。下面針對 macOS 與 Windows 給出簡單命令與連結。

macOS（推薦用 Homebrew）：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
brew install python
python3 --version
python3 -m pip install --upgrade pip
```

Windows（官方安裝程式或 winget）：

1. 官方下載（GUI 安裝程式）：https://www.python.org/downloads/windows/ （安裝時請勾選 "Add Python to PATH"）
2. 或使用 winget（PowerShell）：

```powershell
winget install Python.Python.3
```

若 PowerShell 無法執行 Activate.ps1，請執行：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

進階：若你需要同時管理多個 Python 版本，可使用 `pyenv`（macOS / Linux）或 `conda`（跨平台）。

## 三、建立虛擬環境（詳細步驟）

在每個專案中使用虛擬環境可以避免套件衝突，推薦建立 `.venv`：

macOS / Linux / WSL：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows cmd：

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

離開虛擬環境：

```bash
deactivate
```

## 四、安裝依賴（requirements.txt）

本專案經掃描後偵測到第三方套件：

- matplotlib

安裝方式（在啟用 `.venv` 後執行）：

```bash
python -m pip install -r requirements.txt
```

若你想鎖定版本以利部署或 CI，請在你的虛擬環境執行：

```bash
pip freeze > requirements.txt
```

## 五、快速驗證（範例程式）

在啟用虛擬環境後，執行下列小測試來確認基本功能：

```bash
python - <<'PY'
try:
    import requests
    r = requests.get('https://httpbin.org/get', timeout=5)
    print('OK, status', r.status_code)
except Exception as e:
    print('測試出現錯誤：', e)
PY
```

如果你沒有安裝 `requests`，這段測試會提示錯誤；可改用本機簡單的 `print('hello')` 測試 Python 本身是否可執行。

## 六、VS Code：下載與快速設定

下載： https://code.visualstudio.com/

建議安裝擴充套件：

- Python（ms-python.python）
- Pylance
- Remote - WSL（如使用 WSL）或 Remote - Containers

快速設定：選擇 Interpreter（左下角）指向專案的 `.venv`。若要自動格式化，設定 `black` 並啟用 `editor.formatOnSave`。

## 七、線上執行 Python（當你沒有本機環境時）

快速可用的平台：

- Replit：https://replit.com/
- Google Colab：https://colab.research.google.com/
- Binder：https://mybinder.org/
- PythonAnywhere：https://www.pythonanywhere.com/
- Official Python Shell：https://www.python.org/shell/

提醒：線上平台有使用限制，適合測試或教學示範，但不建議做長期開發或部署。

## 八、專案結構（自動掃描摘要）

本專案以數字資料夾分區（每個資料夾含相關模組）：

- `.venv/` — 本地虛擬環境（通常不放到 Git）
- `1/` … `12/` — 功能模組分區（例如 `3/` 為地圖與導航，`10/` 包含視覺化工具 `matplotlib_map.py`）
- `README.MD` — 本檔

（如需更詳細的樹狀結構或 README 中列出每個模組的使用方法，我可以自動生成一份 `STRUCTURE.md`。）

## 九、.gitignore 建議

新增 `.gitignore`，至少加入：

```
.venv/
__pycache__/
*.pyc
```

## 十、常見問題（FAQ）與排錯

- python 找不到（command not found）：檢查 PATH 是否包含 Python 執行檔；在 mac 可使用 `which python3`；在 Windows 使用 `where python`。 
- pip 權限錯誤：優先使用虛擬環境或加 `--user`。
- macOS SSL 錯誤：若使用 python.org 安裝包，執行 `Install Certificates.command`（在安裝目錄）。
- 套件編譯失敗（C extension）：macOS 可安裝 Xcode Command Line Tools：`xcode-select --install`；Windows 可考慮改用 conda。

## 十一、下一步（你要我幫忙的事）

我可以為你自動完成以下任一項：

1. 建立 `.gitignore` 與 `example.py`（一個簡單的測試程式），並在專案的 `.venv` 裡執行驗證（需要我在工作區執行終端命令）。
2. 在當前 `.venv` 中執行 `pip freeze > requirements.txt` 並把版本鎖定（需我執行終端命令）。
3. 生成更詳細的 `STRUCTURE.md`，列出每個模組檔案與簡短說明。

請回覆要我執行哪一項（例如輸入 `1`、`2` 或 `3`），我會馬上幫你執行並回報結果。
- `1/` — 機器人（robot）命令與循環相關（例如：robot_command.py、robot_loop.py）。

## 專案結構說明

此專案以數字資料夾分區，每個資料夾包含相關功能模組（下方為自動掃描結果與簡短說明）：

- `.venv/` — 推薦用於本地虛擬環境（未包含在版本控制內）。
- `1/` — 機器人（robot）命令與循環相關（例如：robot_command.py、robot_loop.py）。
- `2/` — 玩家（player）與互動（interaction）相關（player.py、robot_ai.py、inventory.py 等）。
- `3/` — 地圖生成與導航（map_generator.py、ai_navigator.py、player_movement.py）。
- `4/` — 距離與偵測（distance_utils.py、zombie_detector.py、interaction_loop.py）。
- `5/` — 戰鬥相關（combat_utils.py、player_combat.py、ai_decision.py、combat_loop.py）。
- `6/` — 行為紀錄與分析（action_logger.py、behavior_analysis.py、preference_stats.py）。
- `7/` — 狀態/策略模組與模擬（state_action.py、ai_strategy.py、simulation_loop.py）。
- `8/` — 物品與庫存模擬（inventory、ai_inventory、item_values）。
- `9/` — 喪屍群組與攻擊模擬（zombie_group.py、zombie_simulation.py、threat_analyzer.py）。
- `10/` — 視覺化工具（matplotlib_map.py、simulation_visual.py、player_visual.py、text_map）。
- `11/` — AI 代理與環境模擬（ai_agent.py、environment.py、ai_simulation.py）。
- `12/` — 進階模組與綜合模擬（adaptive_ai_simulation.py、advanced_zombies.py、rare_items.py、survival_metrics.py）。
- `README.MD` — 專案說明與安裝說明（本檔）。

（上方為掃描專案檔案所得的摘要；若實際用途與此描述不符，請告訴我要如何調整分類。）
