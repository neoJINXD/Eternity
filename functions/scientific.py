

def convert_to_sn(number: float) -> str:
    output = ''
    num_as_str = str(number)
    # if python already converted to scientific notation
    if 'e' in num_as_str:
        return num_as_str
    if len(num_as_str.split('.')) == 2:
        whole_part, decimal_part = num_as_str.split('.')
    else:
        whole_part = num_as_str
        decimal_part = ''
    if int(whole_part) == 0:
        # no whole part, negative exponent
        exp = -1
        pos = 0
        for i in decimal_part:
            if i == '0':
                exp -= 1
                pos += 1
            else:
                break
        output = decimal_part[pos] + '.' + decimal_part[pos+1:] + 'e' + str(exp)
    else:
        # has whole part, positive exponent
        exp = len(whole_part[1:])
        output = whole_part[0] + '.' + whole_part[1:] + decimal_part + 'e+' + str(exp)
    return output


print(convert_to_sn(0.0056))
print(convert_to_sn(0.00000856))
print(convert_to_sn(0.075056))
print(convert_to_sn(750.56))
print(convert_to_sn(7506235474))
