def lone_sum(a, b, c):
  sum = a + b + c

  if a == b:
    sum = c

  if a == c:
      sum = b

  if b == c:
      sum = a

  if a == b and a == c:   
      sum = 0  
    
  return(sum)


lone_sum(1, 1, 3)
