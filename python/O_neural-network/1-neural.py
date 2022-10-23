# https://www.youtube.com/watch?v=lGLto9Xd7bU&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=2&ab_channel=sentdex
# dla jednego neuronu 3 wejscia i kazde wejscie ma inna wage, bias to id neuronu
# modeling one neuron !!!
# inputs = [1.2, 5.1, 2.1] 
# weights = [3.1, 2.1, 8.7]
# bias = 3

# output = sum(i*j for i,j in zip(inputs, weights)) + bias
# print(output)

# for 3 neurons
inputs = [1, 2, 3, 2.5]
 
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]

bias1 = 2
bias2 = 3
bias3 = 0.5

biases = [2, 3, 0.5]

output123 = [sum(i*j for i,j in zip(inputs, weights1)) + bias1,
             sum(i*j for i,j in zip(inputs, weights2)) + bias2,
             sum(i*j for i,j in zip(inputs, weights3)) + bias3]
print(output123)
# output0 = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
# print(output0)


