class SVM_classifier():
    

    #initiating the hyperparameters.
    def __init__(self, learning_rate, no_of_iterations, lambda_parameter):
        self.learning_rate = learning_rate
        self.no_of_iterations = no_of_iterations
        self.lambda_parameter = lambda_parameter

        #lambda parameter is the regularization parameter that builds some misclassified data points. it value ranges from 0.1, 0.001, 0.001 etc


#==--------------------------Step One Ends Here------------------------------------------#
    #fitting the data to the model
    def fit(self, X, Y ):

        #m = number of rows
        #n = number of feature columns
        self.m, self.n = X

        #initiating the weight and bias value
        self.w = np.zeros(self.n)
        self.b = 0
        #weight is and array and b is a single number

        self.X = X
        
        self.Y = Y

        #implementing Gradient Descent for optimization
        for i in range(self.no_of_iterations):
            self.update_weights()  #the weight updates each time the for loop is running so we can get accurate prediction from our model 



#==--------------------------Step Two Ends Here------------------------------------------#

    #updating the weight and the bias  
    def update_weights(self, ):
        
        #label encoding
        y_label = np.where(self.Y <= 0, -1, 1)

        #Gradient(dw, db function for updating  the weight and bias value     
        for index, x_i in enumerate(self.X):
        #enumerate = how many times an account is carried out in a list. to print the index ad values of the list
                
            condition = y_label[index] * (np.dot(x_i, self.w) - self.b)>= 1  #Gradient for SVM classifier

            if (condition == True):
                dw = 2 * self.lambda_parameter * self.w
                db = 0
                
            else:
                
                dw = 2 * self.lambda_parameter * self.w - np.dot(x_i, y_label[index])
                db = y[label[index]]


            self.w = self.w - self.Learning_rate * dw 

            self.b = self.b - self.Learning_rate * db
            

#==--------------------------Step Three Ends Here------------------------------------------#
    #predicting the label for a given input value

    def predict (self, X):

        output = np.dot(X, x.self) -self.b
        
        predicted_labels  =  np.sign(output)   #to conver all -ve values to a classification and all +ve to another classification

        y_cap = np.where(predicted_labels <= -1, 0, 1)

        return_ycap

#model = SVM_classifier and instace its usually represented with 'self'
#the sytax self take the position of the SVM_classifier i.e model