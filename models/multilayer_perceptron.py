"""
@author: Sergio Rozada

@description: Building a multilayer perceptron to learn a logical XOR. This
is done by using one hidden layer with two neurons and two input neurons, one
for each input to the logical gate. The gate can be seen as the combination of
logical gates (hidden neurons) whose outputs are combined in the output neuron.

The purpose of this script is educative. Optimization of the performance is not
the main point. A more clear cascade pipeline was implemented.
"""

import numpy as np

def sigmoid(z):
    """ Calculate the sigmoid function of a value"""
    return 1/(1+np.exp(-z))

def sigmoidPrime(z):
    """ Calculate the derivative of the sigmoid in a given value"""
    return z*(1-z)
    
def errorPrime(t,o):
    """ Calculate the derivative of the error for a pair target output"""
    return t-o

def calculatePotential(x,w):
    """ Calculate activation potential of a neuron for a given input"""
    
    #Add one column for the bias
    i = np.zeros(3)
    i[0] = 1
    i[1:] = x
    
    return np.dot(i,w)

def calculateWeights(h,delta,w,alpha):
    """ Calculate new weights based on activation states and delta"""
    
    # Adding a column for the bias
    hb = np.zeros(3)
    hb[0] = 1
    hb[1:] = h
    
    # Calculating new weights
    deltaW = alpha*delta*hb
    return w+deltaW

def forwardProp(x,Wih,Who):
    """ Calculate the outputs of the net after the forward propagation"""
    
    # Activation value of the hidden neurons
    h1 = sigmoid(calculatePotential(x,Wih[0,:]))
    h2 = sigmoid(calculatePotential(x,Wih[1,:]))
    hiddenStates = np.array([h1,h2])
    
    # Output value
    o=sigmoid(calculatePotential(np.array([h1,h2]),Who))
    
    return o,hiddenStates

def backwardProp(x,o,t,hiddenStates,alpha,Wih,Who):
    """ Recalculate the weights depending on the error signal"""
    
    # The delta of the output neuron is calculated
    deltaOutput = errorPrime(t,o)*sigmoidPrime(o)
    
    # Recalculate the hidden-output weights
    Who = calculateWeights(hiddenStates,deltaOutput,Who,alpha)
    
    # Calculate deltas of hidden neurons
    deltaHidden1 = deltaOutput*Who[1]*sigmoidPrime(hiddenStates[0])
    deltaHidden2 = deltaOutput*Who[2]*sigmoidPrime(hiddenStates[1])
    
    # Recalculate the hidden-input weights
    Wih1 = calculateWeights(x,deltaHidden1,Wih[0,:],alpha)
    Wih2 = calculateWeights(x,deltaHidden2,Wih[1,:],alpha)
    
    Wih[0,:] = Wih1
    Wih[1,:] = Wih2
    
    return Wih,Who

def train(X,t,alpha,Wih,Who,epochs):
    """ Train the model a given number of epochs"""
    
    for i in range(epochs):
        #Select one of the 4 training points we have
        index = i%4
        
        # Forward propagation
        output, hiddenStates = forwardProp(X[index,:],Wih,Who)
        # Backward propagation
        Wih, Who = backwardProp(X[index,:],output,t[index],hiddenStates,alpha,Wih,Who)
        
    return Wih,Who

# Define the training data
X = np.array([[0,0],[0,1],[1,0],[1,1]])
t = np.array([0,1,1,0])

# Define the parameters of the model
alpha = 0.6
Wih = np.array([[0.5,0.6,0.4],[0.8,0.2,0.4]]) # input to hidden layer
Who = np.array([0.2,0.6,0.4])   # hidden layer to output layer
epochs = 10000

# Train the model
Wih, Who = train(X,t,alpha,Wih,Who,epochs)

# Print the results
print("The bias of the first hidden neuron is: ", Wih[0,0])
print("The weight of the first input and first hidden neuron is: ", Wih[0,1])
print("The weight of the second input and first hidden neuron is: ", Wih[0,2])
print("\n")
print("The bias of the second hidden neuron is: ", Wih[1,0])
print("The weight of the first input and second hidden neuron is: ", Wih[1,1])
print("The weight of the second input and second hidden neuron is: ", Wih[1,2])
print("\n")
print("The bias of the output neuron is: ", Who[0])
print("The weight of the first hidden and output neuron is: ", Who[1])
print("The weight of the second hidden and output neuron is: ", Who[2])
print("\n")

# Predicting some results
for i in range(4):
    o, hiddenStates = forwardProp(X[i,:],Wih,Who)
    print("The value predicted for ",X[i,:]," is: ",int(round(o)))