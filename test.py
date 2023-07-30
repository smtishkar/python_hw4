import datetime
logs =[]

def logging(logs, sum):
    time = str(datetime.datetime.now())
    logs.append((sum, time))
    return logs


time = datetime.datetime.now()
print(time)
print(logging(logs, 100))