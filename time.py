# Created by bassam at 9/27/2021

from datetime import datetime

timenow = datetime.now()
income = str(timenow.hour) + str(timenow.minute)
print(income)