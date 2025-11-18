def split_before_each_uppercases(formula):
    if not formula:
        return []

    result = []
    current_part = formula[0] 

    for char in formula[1:]:
        if char.isupper():
            result.append(current_part)
            current_part = char
        else:
            current_part += char
            
    result.append(current_part)
    
    return result


def split_at_first_digit(formula):
    first_digit_index = -1
    
    for i in range(len(formula)):
        if formula[i].isdigit():
            first_digit_index = i
            break
            
    if first_digit_index == -1:
        return (formula, 1)
    else:
        prefix = formula[:first_digit_index]
        number_str = formula[first_digit_index:]
        number = int(number_str)
        
        return (prefix, number)
