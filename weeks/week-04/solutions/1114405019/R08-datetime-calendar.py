# R08-datetime-calendar.py. Datetime Calendar (2.20)

x = "2023-04-17"
y = x.split("-")
print(y) # ['2023', '04', '17'], split date string

x = 2023
y = 4
print(f"{x}-{y:02d}") # 2023-04, format year-month

x = 31
y = 12
print(f"Days in month: {x}, Month: {y}") # Days in month: 31, Month: 12
