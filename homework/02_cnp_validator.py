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
    if int(sex) in [0, 3, 4]:
        return False
    # test date
    try:
        datetime.datetime(int('19' + year), int(month), int(day))
        false_date = False
    except ValueError:
        false_date = True
    if false_date:
        return False
    # test county
    if int(county) > 52 or (46 < int(county) < 51):
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
