from datetime import date,  timedelta, datetime
time = datetime.now()-timedelta(1)
yesterday = time.strftime("%d-%m-%Y")

print("Yesterday: ",yesterday)

time = datetime.now()
today = time.strftime("%d-%m-%Y")

print("Today: ",today)

time = datetime.now()+timedelta(1)
tomorrow = time.strftime("%d-%m-%Y")

print("Tomorrow: ", tomorrow)