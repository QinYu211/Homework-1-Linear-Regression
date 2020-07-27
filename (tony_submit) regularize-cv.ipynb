{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1811976.5702684515\n",
      "[3928.07687554]\n",
      "[-1.15372087 -1.22213684 -1.1017549  -1.54042767 -2.43581425 -2.21169544\n",
      "  0.67493254  0.43644429  0.23566017]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.linear_model import Ridge\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import linear_model\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.metrics import mean_squared_error\n",
    "\n",
    "\n",
    "def normalize_train(X_train):\n",
    "    mean = np.mean(X_train, axis = 0)\n",
    "    std = np.std(X_train, axis = 0)\n",
    "    X = (X_train - mean) /std\n",
    "    return X, mean, std\n",
    "\n",
    "def normalize_test(X_test, trn_mean, trn_std):\n",
    "    X = (X_test - trn_mean) /trn_std\n",
    "    return X\n",
    "\n",
    "diamonds = pd.read_csv('diamonds.csv')\n",
    "\n",
    "X = diamonds[['carat', 'depth', 'table', 'x', 'y', 'z', 'clarity', 'cut', 'color']]\n",
    "y = diamonds[['price']]\n",
    "\n",
    "#Training and testing split, with 25% of the data reserved as the test set\n",
    "X = X.to_numpy()\n",
    "y = y.to_numpy()\n",
    "[X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)\n",
    "\n",
    "[X_train, trn_mean, trn_std] = normalize_train(X_train)\n",
    "X_test = normalize_test(X_test, trn_mean, trn_std)\n",
    "\n",
    "lmbda = np.logspace(-1, 2, num=101) # Lambda Values Needed for Submission\n",
    "MODEL = []\n",
    "MSE = []\n",
    "\n",
    "for l in lmbda:\n",
    "    ridge = Ridge(alpha=l,fit_intercept=True)\n",
    "    ridge.fit(X_train,y_train)\n",
    "    mse = mean_squared_error(y_test,ridge.predict(X_test))\n",
    "    MODEL.append(ridge)\n",
    "    MSE.append(mse)\n",
    "\n",
    "\n",
    "# plot MSE with lmbda\n",
    "plt.figure(figsize=(6,4))\n",
    "plt.plot(lmbda,MSE)\n",
    "plt.xlabel('Lambda')\n",
    "plt.ylabel('MSE')\n",
    "plt.title('MSE vs. Lambda (Tony Qin-20200727)')\n",
    "plt.show()\n",
    "    \n",
    "best_lmbda = lmbda[MSE.index(min(MSE))]\n",
    "print(min(MSE))\n",
    "# mse = mean_squared_error(y_test, ridge.predict(X_test))\n",
    "# print(mse)\n",
    "\n",
    "# print(\"Training set score:{:.2f}\".format(ridge.score(X_train,y_train)))\n",
    "# print(\"Test set score:{:.2f}\".format(ridge.score(X_test,y_test)))\n",
    "# a = ridge.score(X_train,y_train)\n",
    "# b = ridge.coef_\n",
    "# c = ridge.intercept_\n",
    "# print(c)\n",
    "\n",
    "\n",
    "ridge = Ridge(alpha=13.489628825916533,fit_intercept=True)\n",
    "ridge.fit(X_train,y_train)\n",
    "b = ridge.coef_\n",
    "c = ridge.intercept_\n",
    "print(c)\n",
    "\n",
    "x_predict = [0.25,60,55,4,3,2,5,3,3]\n",
    "x_predict_nor = normalize_test(X_predict, trn_mean, trn_std)\n",
    "print(x_predict_nor)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
