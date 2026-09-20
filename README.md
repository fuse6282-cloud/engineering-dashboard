การติดตั้งและการเริ่มใช้งาน
1. โคลนคลังโค้ด (Clone Repository)
Bash
git clone [https://github.com/fuse6282-cloud/engineering-dashboard.git](https://github.com/fuse6282-cloud/engineering-dashboard.git)
cd engineering-dashboard
2. สร้างและเปิดใช้งาน Virtual Environment
Windows:

PowerShell
python -m venv .venv
.venv\Scripts\activate
macOS / Linux:

Bash
python3 -m venv .venv
source .venv/bin/activate
3. ติดตั้ง Dependencies
Bash
pip install -r requirements.txt
4. รันแอปพลิเคชัน
Bash
streamlit run app.py
การทดสอบระบบ (Running Tests)
ทดสอบการทำงานของโมดูลต่าง ๆ ผ่าน pytest:

Bash
pytest