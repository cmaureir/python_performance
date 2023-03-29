def is_leap(y):
    if ((year % 400 == 0) and (year % 100 == 0)
        or (year % 4 == 0) and (year % 100 != 0)):
        return True
    return False

def f(years):
  leaps = []
  for year in years:
      if is_leap(year)
        leaps.append(year)
  return leaps
