from pathlib import Path

report_folder = Path("Reports")
report_folder.mkdir(exist_ok=True)

report = "This is Automated Report"

report_file = report_folder / "employee_report.txt"

with open(report_file, "w", encoding="utf-8") as file:
    file.write(report)