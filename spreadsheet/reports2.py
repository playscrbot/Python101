from pathlib import Path
from datetime import datetime

report_folder = Path("Reports")
report_folder.mkdir(exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
filename = f"employee_report_{today}.txt"

report = "This is Automated Report"

report_file = report_folder / filename

with open(report_file, "w", encoding="utf-8") as file:
    file.write(report)