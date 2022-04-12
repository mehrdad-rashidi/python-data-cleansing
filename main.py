# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    from DateAndTimeUtillity import convertJalaliToGregorian
    file = open('C:/Users/Mehrdad/Desktop/1010122162111_1400-1401.txt', 'r', encoding='utf8')
    line = file.readline()
    line_list = line.split(',')
    # print(line_list)
    duration = line_list[0]
    durationStart = duration[:8]
    durationEnd = duration[8:16]
    durationEndGregorian = convertJalaliToGregorian(durationEnd)
    durationStartGregorian = convertJalaliToGregorian(durationStart)
    print(durationStart, durationStartGregorian)
    print(durationEnd, durationEndGregorian)
    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
