## Evangelos Tsiamalos
## Temp71
##
## Please read instruction in "assignment5_report.pdf"


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import math



def TrainRF(X, Y, n_trees, min_samples_leaf):
    '''
    – X: The sample data (samples along rows, features along columns).
    – Y: The label vector. Y is the class variable you want to predict.
    – n trees: the number of trees to grow
    – min samples leaf: minimum number of leaf node observations
    
    – model: This model should contain everything required in order to classify
        new samples. It is up to you to decide the structure of the variable. The only
        requirement is that it is compatible with your next function.

    '''
    
    
    model = {}  ## The model that we are going to return. Its keys are the integers 1,..., n_trees and its values are the trained decision trees
    for i in range(n_trees):
        
        ## Step 1: Create a bootstraped dataset of equal size with the original
        bootstrap_rows = np.random.randint(X.shape[0], size=X.shape[0])    ## Select wchich rows we are going to pick with replacement
        
        X_boots = X[bootstrap_rows]     ## The bootstrap datasets
        Y_boots = Y[bootstrap_rows]
        
        
        ## Step 2: Train a tree only taking some of the variables into account
        numberOfVariables = np.floor(np.sqrt(X_boots.shape[1]))
        tree = DecisionTreeClassifier(criterion= "entropy",min_samples_leaf=min_samples_leaf,max_features="sqrt")
        tree.fit(X,Y)       ## Train the tree
        #model[i] = {"tree":tree, "bootstrap_rows": bootstrap_rows}
        model[i] = {"tree":tree}
    return model

def PredictRF(model, X):
    '''
    – model: A model previously trained using TrainRF.
    – X: A matrix of data to be classified (samples along rows, features along
    columns).    
    
    predictions: The vector of predicted classes for each of the input samples
    '''
    
    result = np.empty(X.shape[0]) ## An array with the classification for ach sample

    votes0 = np.zeros(X.shape[0])  ## Array containing the votes for 0 for each sample
    votes1 = np.zeros(X.shape[0])   ## Array containing the votes for 1 for each sample
    for j in model.keys():  ## For each tree count the votes 
        treeClassification = model[j]["tree"].predict(X)  ## Classification of the tree
        votes0[treeClassification == 0] += 1    
        votes1[treeClassification == 1] += 1
    result[(votes0 - votes1 > 0)] = 0
    result[(votes1 - votes0 >= 0)] = 1
    #return result, votes0/len(model.keys()), votes1/len(model.keys())
    return result
    
def differenceOfAccuracy():
    ########################## NOT REQUIRED ##############################
    '''
    A function that performs tasks to evaluate the general case of the difference of forest accuracy and average tree accuracy of Part B
    '''
    
    n1 = 100  ## For 100 trees
    min1 = 1   ## min_sample_leaf
    min2 = 10
    cases = 200   ## Check k-cases
    history1 = np.empty(cases)  ## Record the differneces
    history2 = np.empty(cases)
    for i in range(cases):
        model1 = TrainRF(X_train,Y_train,n1,min1) ## Train and test the model for min_sample_leaf = 1
        predictions1 = PredictRF(model1,X_test)
        
        ## Accuracy for the forest
        forestAccuracy1 = (predictions1 == Y_test).sum()/Y_test.size
        
        ## Accuracy of each tree
        treeAccuracy1 = np.array([(model1[k]["tree"].predict(X_test) == Y_test).sum()/Y_test.size for k in model1.keys()])
        averageTreeAccuracy1 = treeAccuracy1.mean()


        model2 = TrainRF(X_train,Y_train,n1,min2) ## Train and test the model for min_sample_leaf = 10
        predictions2 = PredictRF(model2,X_test)
        
        ## Accuracy for the forest
        forestAccuracy2 = (predictions2 == Y_test).sum()/Y_test.size
        
        ## Accuracy of each tree
        
        treeAccuracy2 = np.array([(model2[k]["tree"].predict(X_test) == Y_test).sum()/Y_test.size for k in model2.keys()])
        averageTreeAccuracy2 = treeAccuracy2.mean()


        history1[i] = abs(forestAccuracy1 - averageTreeAccuracy1) ## record the differences for ach case
        history2[i] = abs(forestAccuracy2 - averageTreeAccuracy2) 
    
    m1 = history1.mean() ## the mean values and the stds
    m2 = history2.mean()
    s1 = history1.std()
    s2 = history2.std()

    plt.figure()  ### MAke histograms for the differences
    plt.hist(history1, bins= 10, alpha=0.5, label = "min_sample_leaf = 1")
    plt.hist(history2, bins = 10,alpha=0.5, label = "min_sample_leaf = 10")
    plt.axvline(x=m1, ymin=0, ymax=1, color='purple',ls = '--', label='Mean Value for min_sample_leaf = 1')
    plt.axvline(x=m2, ymin=0, ymax=1, color='red',ls = '--', label='Mean Value for min_sample_leaf = 10')
    plt.legend()
    plt.xlabel("Values of the differnece Forest Accuracy - Average Tree Accuracy")
    plt.title("Difference Forest Accuracy - Average Tree Accuracy for values of min_sample_leaf")
    print()
    print("Evaluation of Differnece")
    print("Average for min_sample_leaf = 1: {:0.6f}".format(m1))
    print("Average for min_sample_leaf = 10: {:0.6f}".format(m2))
    print("Variance for min_sample_leaf = 1: {:0.6f}".format(s1))
    print("Variance for min_sample_leaf = 10: {:0.6f}".format(s2))
    plt.show()
    ####################################################################
  





############## MAIN PROGRAM ##################

if __name__ == "__main__":
    dataset = pd.read_csv("Dataset6.1_XY.csv") ## read the data
    


    ## Part A and B
    ## Suffle and  Split the data
    suffled = dataset.sample(frac = 1)
    percentage = 0.7
    point = int(np.floor(percentage*len(suffled)))
    X_train = suffled.iloc[:point,:-1].to_numpy()
    Y_train = suffled.iloc[:point,-1].to_numpy()
    X_test = suffled.iloc[point:,:-1].to_numpy()
    Y_test = suffled.iloc[point:,-1].to_numpy()
    #n_trees = 1000
    n_trees = int(input("n_trees: "))
    #min_samples_leaf = 10
    min_samples_leaf = int(input("min_samples_leaf: "))
    model = TrainRF(X_train,Y_train,n_trees,min_samples_leaf)
    #predictions, vote0, vote1 = PredictRF(model,X_test)
    predictions = PredictRF(model,X_test)
    
    ## Accuracy for the forest
    forestAccuracy = (predictions == Y_test).sum()/Y_test.size
    
    ## Accuracy of each tree
    
    treeAccuracy = np.array([(model[k]["tree"].predict(X_test) == Y_test).sum()/Y_test.size for k in model.keys()])
    averageTreeAccuracy = treeAccuracy.mean()



  
    print()
    print("PART B")
    print("Forest Accuracy: {:0.6f}".format(forestAccuracy))
    print("Tree Average Accuracy: {:0.6f}".format(averageTreeAccuracy))
    #print("Average frequency of vote 1 by the trees: {:0.3f}".format(vote1[Y_test == 1].mean()))
    #print("Average frequency of vote 0 by the trees: {:0.3f}".format(vote0[Y_test == 0].mean()))

    plt.figure()
    plt.hist(treeAccuracy,bins = 10)
    plt.axvline(x=averageTreeAccuracy, ymin=0, ymax=1, color='purple',ls = '--', label='Mean Value of tree Accuraces')
    plt.axvline(x=forestAccuracy, ymin=0, ymax=1, color='red',ls = '--', label='Forest Accuracy')
    plt.legend()
    plt.xlabel("Accuracy")
    plt.ylabel("Freequency for the accuracy of the trees")
    plt.title("Accuracy comparison")
    plt.show()
    
    ##BONUS
    casesBonus = 1000
    treeStandard =  DecisionTreeClassifier(criterion= "entropy",max_features=None) ## Create a standard tree
    DTaccuracy = np.empty(casesBonus)
    for i in range(casesBonus):
        treeStandard.fit(X_train, Y_train)
        DTaccuracy[i] = (treeStandard.predict(X_test) == Y_test).sum() / Y_test.size
    dtmean = DTaccuracy.mean()
    
    prob = (DTaccuracy >= forestAccuracy).sum()/casesBonus
    print()
    print("Bonus")
    print("The probability that a single tree would obtain similar or better accuracy than the forest: {:0.6f}".format(prob)) 
    plt.figure()
    plt.hist(DTaccuracy,bins = 100)
    
    plt.axvline(x=dtmean, ymin=0, ymax=1, color='purple',ls = '--', label='Mean Value of tree Accuraces')
    plt.axvline(x=forestAccuracy, ymin=0, ymax=1, color='red',ls = '--', label='Forest Accuracy')
    plt.xlabel("Accuracy")
    plt.ylabel("Freequency for the accuracy of the trees")
    plt.title("BONUS: Forest vs Standard tree")
    plt.show()
######### UNCOMENT THE FUNCTION IF YOU WANT TO TRY IT ####################
    #differenceOfAccuracy()