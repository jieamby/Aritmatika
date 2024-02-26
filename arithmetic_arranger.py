def arithmetic_arranger(problems, show_answers=False):
  # Check if the number of problems is within limits
  if len(problems) > 5:
      return "Error: Too many problems."

  # Initialize lists to store arranged elements
  first_line = []
  second_line = []
  dash_line = []
  answer_line = []

  # Iterate through each problem
  for problem in problems:
      # Split the problem into operands and operator
    operand1, operator, operand2 = problem.split()

      # Check if operands are digits
    if not operand1.isdigit() or not operand2.isdigit():
          return "Error: Numbers must only contain digits."

      # Check if operands are within 4 digits
    if len(operand1) > 4 or len(operand2) > 4:
          return "Error: Numbers cannot be more than four digits."

      # Check if the operator is valid
    if operator not in ['+', '-']:
          return "Error: Operator must be '+' or '-'."

      # Determine the maximum length of operands
    max_length = max(len(operand1), len(operand2)) + 2

      # Add elements to each line
    first_line.append(operand1.rjust(max_length))
    second_line.append(operator + operand2.rjust(max_length - 1))
    dash_line.append('-' * max_length)

      # Calculate the answer if requested
    if show_answers:
      if operator == '+':
        answer = str(int(operand1) + int(operand2))
      else:
        answer = str(int(operand1) - int(operand2))
      answer_line.append(answer.rjust(max_length))

  # Concatenate the lines
  arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dash_line)
  if show_answers:
      arranged_problems += '\n' + '    '.join(answer_line)

  return arranged_problems
