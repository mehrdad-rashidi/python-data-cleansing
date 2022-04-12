import jdatetime


def convertJalaliToGregorian(date):
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    print(year)
    gregorian_date = jdatetime.date(year, month, day).togregorian()
    return gregorian_date


def convertGregorianToJalali(date):
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    jalali_date = jdatetime.date.fromgregorian(day=day, month=month, year=year)
    return jalali_date
