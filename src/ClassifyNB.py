def classify(features_train, labels_train):

    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB();
    fit = clf.fit(features_train, labels_train);
    return(fit);

    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!

