# practice Data
x = [1, 2, 3, 4, 5]   # independent data
y = [3, 4, 2, 4, 5]   # dependent data

# means of dependent and independent variables
sum_x = 0
sum_y = 0
for i,j in zip(x,y):
   sum_x += i
   sum_y += j
x_mean = sum_x / len(x)
y_mean = sum_y / len(y)

# calclating slope(m) for fit line [m = summation(x - x_mean)*(y - y_mean) / summation(x - x_mean)^2]
num = 0
den = 0
for i,j in zip(x,y):
    num += (i - x_mean)*(j - y_mean)
    den += (i - x_mean) ** 2
    
m = num / den

# intercept for fit line
c = y_mean - m * x_mean

# predict the value using line fit
def y_pred(x):
    return m * x + c

# calculating r2_score
n1 = 0
d1 = 0
for i,j in zip(x,y):
    n1 += (y_pred(i) - y_mean) ** 2
    d1 += (j - y_mean) ** 2   
r2_score = n1 / d1
