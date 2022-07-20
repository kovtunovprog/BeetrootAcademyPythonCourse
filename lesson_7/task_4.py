day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weeks = {}
weeks_1 = {}

for k, v in enumerate(day, 1):
    weeks.update({k:v})
    weeks_1.update({v:k})
print(weeks, weeks_1)