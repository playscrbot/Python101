import os
import datetime
from datetime import datetime

file_path = "path/to/file"

file_name = os.path.basename(file_path)
name = file_name.lower()

if name.startswith("invoice_"):
    category = "Invoices"

elif "employee" in name:
    category = "Employee Reports"

elif "meeting" in name:
    category = "Meetings"

else:
    category = "Unknown"

file_stats = os.stat(file_path)
timestamp = file_stats.st_mtime
modified = datetime.fromtimestamp(timestamp)
print(modified)