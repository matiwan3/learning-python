# libs: NumPy, Pandas, SciPy,tenserFlow, matplotlib, Keras, SciKit-Learn, PyTorch, Scrapy, BeautifulSoap, LightGBM, ELI5, Theano, NuPIC, Ramp, Pipenv, Bob, PyBrain, Caffe2, Chainer
 
#python -m venv venv_name
# source venv_name/bin/activate
# pip install numpy scikit-learn matplotlib
# deactivate

# https://www.simplilearn.com/top-python-libraries-for-data-science-article
# /Users/mateuszwandzlewicz/Desktop/PYTHON-main/python/2023.08/ds/dsvenv/bin/python 1.py
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import sys

print(sys.path)
# Generate a list of 50 numbers
np.random.seed(0)
X = np.linspace(0, 10, 50)
y = 2 * X + 1 + np.random.normal(0, 1, 50)  # y = 2X + 1 with some noise

# Reshape the data
X = X.reshape(-1, 1)

# Create a Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Generate 50 new numbers for prediction
X_new = np.linspace(11, 20, 50).reshape(-1, 1)

# Predict the corresponding y values using the model
y_pred = model.predict(X_new)

# Plot the original data and the predicted values
plt.scatter(X, y, label='Original Data')
plt.plot(X_new, y_pred, color='red', label='Predicted Data')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Prediction')
plt.legend()
plt.show()




