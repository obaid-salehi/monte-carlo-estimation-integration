import numpy as np
import math
import matplotlib.pyplot as plt
import time

func_string = input("Enter the Python script for f(x): ")
lower = eval(input("Enter the lower bound: "),{"math": math})
upper = eval(input("Enter the upper bound: "),{"math": math})

start = time.time()

def f(x):
    return eval(func_string,{"x": x, "np": np, "math": math})    #evaluates the inputted function as a python script
sims = np.random.uniform(lower,upper,1000000)    #this is the numpy array of 1 million randomly generated x co-ordinates
x_values = sims.copy()   
sims = f(sims)    #applying the user's function on the values through a vectorised operation
estimation = np.mean(sims)*(upper-lower)    #can assume the the area of the rectangle is the same as the value of the integral
print(estimation)

end = time.time()

print("Elapsed time:",end-start,"seconds. ")

plt.scatter(x_values,sims,lw=1,c="b")    #plots all the co-ordinates individually
plt.plot([lower,upper],[np.mean(sims),np.mean(sims)],lw=5,c="r")
plt.plot([lower,lower],[0,np.mean(sims)],lw=5,c="r")
plt.plot([upper,upper],[0,np.mean(sims)],lw=5,c="r")
plt.plot([lower,upper],[0,0],lw=5,c="r")    #producing the rectangle to visualise the direct averaging process
plt.grid()
plt.show()


