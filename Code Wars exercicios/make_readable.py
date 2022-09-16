#code wars Kata link: https://www.codewars.com/kata/52685f7382004e774f0001f7
def make_readable(seconds):

    def zero_add(a):
        tt = '0' + str(int(a)) if len(str(int(a))) == 1 else str(int(a))
        return tt

    hour = seconds/3600
    hh=zero_add(hour)
    minutes = (float(hour) - int(hour)) *60
    mm = zero_add(minutes)
    sec = round((float(minutes) - int(minutes))*60)
    ss = zero_add(sec)

    return hh + ':' + mm + ':' +ss

print(make_readable(7799))
