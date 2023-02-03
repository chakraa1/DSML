"""
Momentum-based gradient descent optimization technique is used to speed up the convergence by using a moving sum of all previous gradients. It is called "momentum" because it feels like a ball rolling downhill using its inertia. Using the momentum technique, the algorithm can converge to an optimal value in a significantly lower time. The two formulas used for this technique are :

v(t+1) = β*v(t) + (1-β)*(∂f/∂x)

where β = momentum constant (fix value as 0.9)
      f = objective fuction(the function over which gradient descent is being applied)
v(t) is the value of v at a certain iteration 't'.
x(t+1) = x(t) - α*v(t+1)

where α = learning rate (fix value as 0.01)
x(t) is the value of input 'x' at a certain iteration 't'.
The first formula is used to update the moving average of gradients and the second formula is used to update the value of x according to the moving average.

You are given an input value 'x' that denotes a point on the objective function 'f'. Using the above two formulas, return the value of 'x' and the value of f(x) after the fourth iteration of the algorithm. Both values should be rounded off to two decimal places.

f(x) = (x-1)²

Input format :

Number of test cases
For each testcase there will be one line of input.
Output format :

A tuple containing value of x after 5th iteration and its corresponding value of the objective function.
Sample input :

2
2
3.5
Sample output :

(1.98, 0.96)
(3.45, 6.03)
Explanation :

For the first test case, after the 4th iteration, the value of x converges from 2 to 1.98, and its f(x) value = (1.98 - 1)² = 0.96
Note: Do not use any inbuilt functions as it may return an error. Also Output to be rounded off to 2 decimal place
"""


# objective function used for gradient descent is (x-1)²
# x-> input value

def obj_func(x):
    return (x * x - 2 * x + 1)


# code starts here

"""
set value of 'alpha' as 0.01 and 'beta' as 0.9
"""
alpha = 0.01
beta = 0.9


def grad(x):
    # return the gradient of the objective function
    return 2 * x - 2


"""
set value of iterations to 4
"""
iterations = 4


# function of momentum based gradient descent
def momentum(x):
    # initalize value of v to zero
    v = 0
    for i in range(iterations):
        # write code to update the value of v on every iteration
        v = beta * v + (1 - beta) * grad(x)

        # write code to update the value of x on every iteration
        x = x - alpha * v

    # finally return the value of x and obj_func(x)
    return round(x, 2), round(obj_func(x), 2)

# code ends here