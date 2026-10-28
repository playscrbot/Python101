# Message Simplified
items_checked = 125
missing_items = 4
completed_by = "Alex"

message = f"""
Hello,

Today's inventory check has been completed.

Items checked: {items_checked}
Missing items: {missing_items}
Completed by: {completed_by}

Regards,
Automated System
"""

# Subject Line Simplified
missing_items = 4
subject = f"Inventory Report - {missing_items} items missing"

# Template
template = """
Hello {name},
The {task} has been {status}.
You have {count} items to process.
"""

message = template.format(
    name="Alex",
    task="document processing",
    status="Completed",
    count=48
)

# Email Message
from email.message import EmailMessage

email = EmailMessage()

email["From"] = "you@gmail.com"
email["To"] = "someone@example.com"
email["Subject"] = "Daily Report"

email.set_content("""
Today's report has been completed.

Items processed: 125
Missing items: 4
""")

# Connect each of them to smtp.py to try out your email