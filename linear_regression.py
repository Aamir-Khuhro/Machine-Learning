import matplotlib.pyplot as plt
from scipy import stats
#%% 
x=[5,7,8,7,2,127,2,9,4,11,12,9,6]
y=[99,2,87,234,0,86,1,87,94,78,7,85,12]
#%%
plt.scatter(x, y)
plt.show()
#%%
s,i,r,p,Std_err=stats.linregress(x,y)
def myfunc(x):
    return s*x+i
mymodel = (list(map(myfunc,x)))
#%%
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print(r)
