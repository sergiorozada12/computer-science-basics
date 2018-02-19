"""
@author: Sergio Rozada

@description: Building a perceptron to learn a logical AND gate. The perceptron 
has two inputs, one for each input of the logical AND. The activation function
is the step function.

The purpose of this script is educative. Optimization of the performance is not
the main point. A more clear cascade pipeline was implemented.
"""

import numpy as np

def stepFunction(x):
    """ Step function evaluates the potential: if greater 
    than 0, output is positive. Negative otherwise """
    if x > 0: return 1
    else:   return 0

def deltaW(x,t,W,alpha):
    """ Calculates the modification on the weights 
    according to the perceptron learning algorithm """
    
    # Input adding a first column for the bias
    i = np.zeros(3)
    i[0] = 1
    i[1:] = x
    
    # Potential of the neuron
    U = np.dot(i,W)
    
    # Output of the neuron
    o = stepFunction(U)
    
    # Delta of the weights
    return alpha*(t-o)*i

def train(X,t,alpha,W,epochs):
    """ Train the model a given number of epochs"""
    
    for i in range(epochs):
        # Select one of the 4 training points we have
        index = i%4
        
        # Modify weights with the calculated delta W
        dW = deltaW(X[index,:],t[index],W,alpha)
        W = W+dW
    
    return W

# Training examples for an AND gate
X = np.array([[0,0],[0,1],[1,0],[1,1]])
t = np.array([0,0,0,1])

# Parameters of the model
alpha = 0.2
W = np.array([1,1,1])
epochs = 100

# Train and obtain the weights
W = train(X,t,alpha,W,epochs)

# Printing the parameters
print("The bias of the output neuron is: ",W[0])
print("The weight of the first input is: ",W[1])
print("The weight of the second neuron is: ",W[2])