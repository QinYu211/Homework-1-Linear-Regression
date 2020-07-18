import numpy as np
import matplotlib.pyplot as plt

#Return fitted model parameters to the dataset at datapath for each choice in degrees.
#Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
#Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
#coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []

    #fill in
    #read the input file, assuming it has two columns, where each row is of the form [x y] as
    #in poly.txt.
    #iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    #for the model parameters in each case. Append the result to paramFits each time.

    return paramFits


#Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
#samples in x.
#Input: x as a list of the independent variable samples, and d as an integer.
#Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
#for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):

    #fill in
    #There are several ways to write this function. The most efficient would be a nested list comprehension
    #which for each sample in x calculates x^d, x^(d-1), ..., x^0.

    return X


#Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
#Input: X as a list of features for each sample, and y as a list of target variable samples.
#Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y)
    X = np.array(X)
    y = np.array(y)

    #fill in
    #Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.

    return B

if __name__ == '__main__':
    datapath = 'poly.txt'
    degrees = [2, 4]

    paramFits = main(datapath, degrees)
    print(paramFits)
    
    # Code for Problem 1: Part 3 - Graphing Degree Polynomials
    ######## Fake Data - Need to Replace with Real Data ########
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([0, 1000, 2000, 3000, 4000])
    
    # Plotting Original Data
    plt.scatter(x, y, color='black', label='data')

    # Plotting Polynomial d = 1
    coeffList_d_1 = [1,0] ######## Need to Replace with paramFits ########
    y = coeffList_d_1[0]*(x) + coeffList_d_1[1]
    plt.plot(x,y, color='red', label='d = 1')

    # Plotting Polynomial d = 2
    coeffList_d_2 = [1,1,0]  ######## Need to Replace with paramFits ########
    y = coeffList_d_2[0]*(x**2) + coeffList_d_2[1]*x + coeffList_d_2[2]
    plt.plot(x,y, color='orange', label='d = 2')

    # Plotting Polynomial d = 3
    coeffList_d_3 = [1,1,1,0]  ######## Need to Replace with paramFits ########
    y = coeffList_d_3[0]*(x**3) + coeffList_d_3[1]*(x**2) + coeffList_d_3[2]*x + coeffList_d_3[3]
    plt.plot(x,y, color='blue', label='d = 3')

    # Plotting Polynomial d = 4
    coeffList_d_4 = [1,1,1,1,0]  ######## Need to Replace with paramFits ########
    y = coeffList_d_4[0]*(x**4) + coeffList_d_4[1]*(x**3) + coeffList_d_4[2]*(x**2) + coeffList_d_4[3]*x + coeffList_d_4[4]
    plt.plot(x,y, color='green', label='d = 4')

    # Plotting Polynomial d = 5
    coeffList_d_5 = [1,1,1,1,1,0]  ######## Need to Replace with paramFits ########
    y = coeffList_d_5[0]*(x**5) + coeffList_d_5[1]*(x**4) + coeffList_d_5[2]*(x**3) + coeffList_d_5[3]*(x**2) + coeffList_d_5[4]*x + coeffList_d_5[5]
    plt.plot(x,y, color='purple', label='d = 5')

    # Labeling Data
    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.legend(fontsize=10, loc='upper left')
    plt.show()
    
