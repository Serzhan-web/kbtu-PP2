from datetime import date,timedelta, datetime
yesterday = datetime.now()-timedelta(1)
tomorrow = datetime.now()+timedelta(1)


yesterday = datetime.timestamp(yesterday)
tomorrow = datetime.timestamp(tomorrow)

print(tomorrow-yesterday)