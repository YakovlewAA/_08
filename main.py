# для моего первого репозитория

import math

def U (a, b, c, x, y):
  return (math.tan(y)**3+math.sin(x)**5*math.sqrt(b-c))/math.sqrt((a-b+c))

start = 2
end = 90
h = (end - start) / 19
x = []
t = []
t1 = []
t2 = []
t3 = []

for i in range (20):
  x.append(start + i * h)
  t.append(U(14,6,2,x[i],5))
  t1.append(U(14,8,3,x[i],4))
  t2.append(U(14,7,3,x[i],1))
  t3.append(U(14,6,2,x[i],7))

  from matplotlib import pyplot as plt

  plt.figure(figsize=(10, 5))
  plt.plot(x, t, color='m', marker='p', linestyle='--', label='x,t')
  plt.plot(x, t1, color='r', marker='+', linestyle=':', label='x,t1')
  plt.plot(x, t2, color='g', marker='d', linestyle='-.', label='x,t2')
  plt.plot(x, t3, color='b', marker='x', label='x,t3')
  plt.xlabel('Ось x')
  plt.ylabel('Ось U(a, b, c, x, y)')
  plt.title('График значений (x, (t, t1, t2, t3))')
  plt.show()
