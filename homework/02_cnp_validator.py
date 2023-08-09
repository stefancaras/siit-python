import re
import datetime


def cnp_validator(cnp):
    # delete whitespaces
    cnp = cnp.strip()
    # check length
    if len(cnp) != 13:
        return False
    # search for non-digits
    if re.search('\D', cnp):
        return False
    # split string
    sex, year, month, day, county, x, y = re.findall('..', ' ' + cnp)
    # test sex
    if not int(sex):
        return False
    # test date
    century = '19' if int(sex) in [1, 2] else '18' if int(sex) in [3, 4] else '20'
    try:
        datetime.datetime(int(century + year), int(month), int(day))
    except ValueError:
        return False
    # test county
    if int(county) > 52 or (int(county) in [0, *range(47, 51)]):
        return False
    # test code
    if x + y[0] == '000':
        return False
    # test control digit
    code = "279146358279"
    total = 0
    for i in range(12):
        total += int(cnp[i]) * int(code[i])
    if str(total % 11)[0] != cnp[-1]:
        return False
    # if all else fails
    return True


print('CNP valid' if cnp_validator(input('Introdu un CNP: ')) else 'CNP invalid')
