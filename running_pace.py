#code wars Kata link: https://www.codewars.com/kata/578b8c0e84ac69a4d20004c8
def running_pace(distance, time):
    if len(time) > 4:
        min = int(time[:-3])
        sec = time[-2::]
    else:
        min = int(time[0])
        sec = time[-2::]

    sec = int(sec) + (min*60)
    pace = (sec/distance)/60
    flt_calc = int((float(pace) - int(pace))*60)

    if int(flt_calc) == 0:
        flt_calc = '00'
    elif flt_calc < 10:
        flt_calc ='0'+str(flt_calc)
    
    return str(int(pace))+':'+ str(flt_calc)

print (running_pace(28.0, '253:57'))