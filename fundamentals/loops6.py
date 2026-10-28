files = ["report.pdf", "data.csv", "invoice.xlsx", "summary.pdf"]

for filename in files:
    print(f"Checking {filename}")

    if filename == "invoice.xlsx":
        print("File found!")
        break