def alarm_clock(day, vacation):
  sun = 0
  mon = 1
  tues = 2
  wed = 3
  thus = 4
  fri = 5
  sat = 6
  
  if day >= 1 and day <= 5 and vacation == False:
    print("7:00")
    
  elif day == 0 and vacation == False or day == 6 and vacation == False:
    print("10:00")
    
  if day >= 1 and day <= 5 and vacation == True:
    print("10:00")

  elif day == 0 or day == 6 and vacation == True:
    print("rest")

alarm_clock(2, True)
