message = "Hello John"
message = message.replace("John", "Sarah")
print(message)

phone = "123-456-7890"
phone = phone.replace("-", "")
print(phone)

text = "John,Smith"
text = text.replace(",", " ")
print(text)

text = "2026/09/22"
text = text.replace("/", "-")
print(text)

text = "INV-2026-001"
clean_text = text.replace("-", "")
print(clean_text)