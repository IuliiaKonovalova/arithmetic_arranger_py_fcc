def arithmetic_arranger(problems, need_solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    line_1 = ''
    line_2 = ''
    line_3 = ''
    line_4 = ''
    for problem in problems:
        problem1 = problem.split()
        number_1 = problem1[0]
        number_2 = problem1[2]
        if not number_1.isdigit() or not number_2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(number_1) > 4 or len(number_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        operator = problem1[1]
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        length_of_column = max(len(number_1), len(number_2)) + 2
        line_1 += number_1.rjust(length_of_column) + ' '*4
        line_2 += (operator + " " + (number_2).rjust(length_of_column-2)) + ' '*4
        line_3 += '-' * (length_of_column) + ' '*4
        line_4 += str(eval(number_1 + operator + number_2)).rjust(length_of_column)  + ' '*4
    if need_solution:
        return line_1.rstrip() + '\n' + line_2.rstrip() + '\n' + line_3.rstrip() + '\n' + line_4.rstrip()
    return line_1.rstrip() + '\n' + line_2.rstrip() + '\n' + line_3.rstrip()


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))