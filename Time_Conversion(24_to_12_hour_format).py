from datetime import datetime
a=input()
d=datetime.strptime(a,"%H:%M")
print(d.strftime("%I:%M %p"))