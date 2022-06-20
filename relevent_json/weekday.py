import datetime
end = '20220617'
startTime = datetime.datetime.strptime(end, "%Y%m%d")
count = 10 # 倒推count天
while count:
    startTime = (startTime + datetime.timedelta(days=-1)).strftime("%Y%m%d")
    startTime = datetime.datetime.strptime(startTime, "%Y%m%d")
    p = startTime.isoweekday()
    if p >= 1 and p <= 5 :
        count -= 1

print(startTime.strftime("%Y%m%d"))