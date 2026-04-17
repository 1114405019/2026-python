# R09-datetime-timezone.py. Datetime Timezone (2.20)

x = 8  # UTC+8 offset
y = 0  # UTC
print(x - y) # 8, timezone difference

x = "Asia/Taipei"
print(x) # Asia/Taipei, timezone name

x = 3600  # seconds in hour
y = 8
print(x * y) # 28800, offset seconds
