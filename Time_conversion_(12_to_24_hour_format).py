from datetime import datetime
m2 = input()
in_time=datetime.strptime(m2,"%I:%M %p")
out_time=datetime.strftime(in_time,"%H:%M")
print(out_time)