import datetime

mytime = datetime.time(hour=2, minute=20, second=1, microsecond=20)
print(mytime.minute)
print(mytime)

print(mytime.microsecond)
print(type(mytime))

#########################################################################

# Date

from datetime import date

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
result = date1 - date2
print(result)
print(type(result))

#########################################################################

from datetime import datetime

datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)

result2 = datetime1 - datetime2
print(result2)