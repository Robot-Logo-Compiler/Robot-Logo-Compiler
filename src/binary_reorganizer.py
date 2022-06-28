EQ_SYMBOLS = ["BIN_OP", "PARAMETER", "SYMBOL"]

def locate_equations(tokens):
    equation_start = -1
    currently_equation = False
    equations = []
    for index in range(len(tokens)):
        if tokens[index][0] in EQ_SYMBOLS and not currently_equation:
            equation_start = index
            currently_equation = True
            #print(index)
        elif currently_equation and tokens[index][0] not in EQ_SYMBOLS:
            equations.append((equation_start, index))
            equation_start = -1
            currently_equation = False
    if tokens[len(tokens)-1][0] in EQ_SYMBOLS:
        #print(1)
        equations.append((equation_start, len(tokens)))
    return equations

def find_dominant(tokens, position):
    balance = 0
    result = -1
    #print(position)
    if position[1] - position[0] <= 2:
        return None
    for index in range(position[0] + 1, position[1]-1):
        if tokens[index][1] == "left_paren":
            balance += 1
        elif tokens[index][1] == "right_paren":
            balance -= 1
        elif balance == 0:
            if tokens[index][1] in ["multiply", "divide"]:
                result = index
            elif tokens[index][1] in ["minus", "plus"]:
                return index
    return result if result != -1 else None

def reorder_equation(tokens, position):
    divider = find_dominant(tokens, position)
    if divider is None:
        return [token for token in tokens[position[0]: position[1]] if token[0] == "PARAMETER"]
    #print(divider, tokens[divider])
    return [tokens[divider]] + reorder_equation(
        tokens, (position[0] + 1, divider)) + reorder_equation(
            tokens, (divider + 1, position[1] - 1))


def reorder_token_list(tokens):
    new_token_list = []
    equatio_locations = locate_equations(tokens)
    #print(equatio_locations)
    equation_index = -1 if len(equatio_locations) == 0 else equatio_locations[0][0]
    equation_number = 0
    index = 0
    while index < len(tokens):
        if index == equation_index:
            new_token_list += reorder_equation(tokens , equatio_locations[equation_number])
            index = equatio_locations[equation_number][1]
            equation_number += 1
            equation_index = -1 if len(equatio_locations) <= equation_number else equatio_locations[equation_number][0]
        else:
            new_token_list.append(tokens[index])
        index += 1
    return new_token_list


if __name__ == "__main__":
    tokens = [("SYMBOL", "left_paren"), ("SYMBOL", "left_paren"), ("PARAMETER", "2"), ("BIN_OP", "plus"), ("PARAMETER", "1") , ("SYMBOL", "right_paren"), ("BIN_OP", "minus"), ("PARAMETER", "1"), ("SYMBOL", "right_paren")]
    print(reorder_token_list(tokens))
