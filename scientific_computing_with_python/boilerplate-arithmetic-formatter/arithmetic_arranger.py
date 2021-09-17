def arithmetic_arranger(problems, answers = False):
    # Check for number of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Split strings into lists
    for index, str in enumerate(problems):
        problems[index] = str.split(' ')

        # Check for error situations for each problem
        if not (problems[index][0].isnumeric() and problems[index][2].isnumeric()):
            return 'Error: Numbers must only contain digits.'

        if int(problems[index][0]) > 9999 or int(problems[index][2]) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        if problems[index][1] != '+' and problems[index][1] != '-':
            return "Error: Operator must be '+' or '-'."

    # Create a list of string and fill them with formated string from lists
    lines = ['','','']

    for index, split_problem in enumerate(problems):
        width = len(max(split_problem, key = len)) + 2
        lines[0] += split_problem[0].rjust(width, ' ')
        lines[1] += split_problem[1]
        lines[1] += split_problem[2].rjust(width - 1, ' ')
        lines[2] += ''.ljust(width, '-')

        lines[0] += '    '
        lines[1] += '    '
        lines[2] += '    '

        # Calculate results and add them to a new line
        if answers:
            lines.append('')
            if split_problem[1] == '+':
                result = int(split_problem[0]) + int(split_problem[2])
            else:
                result = int(split_problem[0]) - int(split_problem[2])
            
            lines[3] += f'{result}'.rjust(width, ' ')
            lines[3] += '    '
            
    # Strip lines and add new line characters
    lines[0] = lines[0].rstrip(' ')
    lines[1] = lines[1].rstrip(' ')
    lines[2] = lines[2].rstrip(' ')
    lines[0] += '\n'
    lines[1] += '\n'
    if answers:
        lines[2] += '\n'
        lines[3] = lines[3].rstrip(' ')

    # Concatenate string from lines list to final string
    arranged_problems = ''
    for i in lines:
        arranged_problems += i

    return arranged_problems
