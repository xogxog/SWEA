# 연월일 달력
# test case...????

def year_month_day(day) :
  pass
  str_day = str(day)
  year = str_day[0:4]
  month = str_day[4:6]
  date = str_day[6:8]
  #print(year)
  #print(month)
  #print(date)

  # 1~12월 인지 확인
  if int(month) <= 0 or int(month) > 12 :
    return -1

  # 30일이 max인 달
  if int(month) ==4 or int(month) == 6 or int(month) ==9 or int(month) == 11 :
    if int(date) > 30 : return -1
    else : return year+'/'+month+'/'+date

  # 28일이 max인 달
  elif int(month) == 2 :
    if int(date) > 28 : return -1
    else : return year+'/'+month+'/'+date
  
  #31일이 max인 달
  else : 
    if int(date) >30 : return -1
    else : return year+'/'+month+'/'+date
  







print(year_month_day(22220228))
print(year_month_day(20150002))
print(year_month_day('01010101'))
print(year_month_day(20140230))
print(year_month_day(11111111))