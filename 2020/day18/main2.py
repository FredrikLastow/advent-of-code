def main():
  calc = list()

  with open('input.txt') as f:
    for line in f:
      expr = line.strip().replace(" ", "")

      start = 0
      pars = list()

      while(True):
        for i in range(start, len(expr)):
          if expr[i] == '(':
            pars.append(i)
          elif expr[i] == ')':
            par_i = pars.pop()
            val = evaluate(expr[par_i+1:i])
            start = par_i

            expr = expr[:par_i] + str(val) + expr[i+1:]
            break

        if expr.count('(') == 0:
          calc.append(evaluate(expr))
          break
  
  print("sum", sum(calc))

def evaluate(expr):
  n = 0

  while(True):
    op_i = -1
    op = None
    
    op_found = False

    n1_i = 0
    n2_i = -1

    for i, c in enumerate(expr):
      if c == '+' or c == '*':
        if op_found:
          n2_i = i
          break
        else:
          if c == '+' or expr.count('+') == 0:
            op_found = True
            op_i = i
            op = c
          else:
            n1_i = i + 1

      if i == len(expr) - 1:
        n2_i = i + 1
    
    n1 = int(expr[n1_i:op_i])
    n2 = int(expr[op_i+1:n2_i])

    if op == '+':
      n = n1 + n2
    elif op == '*':
      n = n1 * n2
    
    expr = expr[:n1_i] + str(n) + expr[n2_i:]

    if expr.count('+') + expr.count('*') == 0:
      return n

if __name__ == '__main__':
  main()