from art_calc import logo
print(logo)


def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2
operator={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num1=float(input("What is the first number?: "))
  
  for key in operator:
    print(key)
  should_continue = True

  while should_continue:
    operator_symbol=input("Choose any operation  : ")
    num2=float(input("What is the next number?: "))
    calculation=operator[operator_symbol]
    answer=calculation(num1,num2)
    print(f"{num1} {operator_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()

