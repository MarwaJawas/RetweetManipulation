
import sys
import scipy
import numpy as np
import pandas
import sklearn
import pandas as pd
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
#from sklearn.datasets import load_iris
#dataset = pd.read_csv("new4_final_temp_feat.csv")
dataset = pd.read_csv("extracted_all_feat.csv")
#dataset.columns

#print(len(dataset.columns))
dataset.fillna(0.999, inplace=True)
x = dataset.iloc[:, 1:33].values
y = dataset.iloc[:, 33].values
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.20, random_state=1)
#dataset = pd.read_csv("new4_final_temp_feat.csv")
dataset = pd.read_csv("extracted_all_feat.csv")
#dataset.columns
#print(len(dataset.columns))
dataset.fillna(0.999, inplace=True)
x = dataset.iloc[:, np.r_[1,4,5,8,13,19,22,24,25,27]].values

y = dataset.iloc[:, 33].values
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.20, random_state=1)


import pandas as pd
#a = pd.read_csv("final_graph_feat.csv")
#b = pd.read_csv("final_temp_feat.csv")

a = pd.read_csv("new4_final_graph_feat.csv")
b = pd.read_csv("new4_final_temp_feat.csv")

merged = pd.merge(b, a, how='left', on=['groupID','label'])
merged.fillna(0.999, inplace=True)
x = merged.iloc[:,  np.r_[ 1:8, 10:11]].values
y = merged.iloc[:, 9].values 
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.20, random_state=1)
# Spot Check Algorithms
models = []
models.append(('Decision Tree', DecisionTreeClassifier()))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200,class_weight="balanced")))
#models.append(('Random Forest',RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0)))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear',class_weight="balanced")))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))

	
# Spot Check Algorithms
models = []
models.append(('Decision Tree', DecisionTreeClassifier()))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200,class_weight="balanced")))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear',class_weight="balanced")))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='roc_auc')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))

	
# Spot Check Algorithms
models = []
models.append(('Decision Tree', DecisionTreeClassifier()))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200, class_weight="balanced")))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear',class_weight="balanced")))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='precision')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))

	
# Spot Check Algorithms
models = []
models.append(('Decision Tree', DecisionTreeClassifier(class_weight="balanced")))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200,class_weight="balanced")))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear',class_weight="balanced")))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='recall')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))

	
# Spot Check Algorithms
models = []
models.append(('Decision Tree', DecisionTreeClassifier()))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200,class_weight="balanced")))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear',class_weight="balanced")))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='f1')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))

	
# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

# Make predictions on validation dataset
model =RandomForestClassifier(n_estimators=200)
#model = LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear')
#model = GradientBoostingClassifier()
#model= DecisionTreeClassifier()
#model= LinearDiscriminantAnalysis()
#model=LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear')
#model = SVC(gamma='auto')
model.fit(X_train, Y_train)
#m=np.where(np.isnan(X_test))
predictions = model.predict(X_test)
# Evaluate predictions
print(confusion_matrix(Y_test, predictions))
print(accuracy_score(Y_test, predictions))
print(classification_report(Y_test, predictions))


#add rows to DataFrame
import pandas as pd
dataset = pd.read_csv("final_graph_feat.csv")
dataset2 = pd.read_csv("extracted_graph_features_aletihad_alhilal.csv")
out = dataset.append(dataset2)
with open('new4_final_graph_feat.csv', 'w', encoding='utf-8') as f:
    out.to_csv(f, index=False)
    
#add columns to dataframe
import pandas as pd
#a = pd.read_csv("final_rt_feat.csv")
a = pd.read_csv("final_graph_feat.csv")
b = pd.read_csv("final_temp_feat.csv")

merged = pd.merge(b, a, how='left', on=['groupID','label'])
    
merged.head()


print(len(merged.columns))

# Feature Selection with Univariate Statistical Tests
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
# load data

# feature extraction
test = SelectKBest(score_func=f_classif, k=4)
fit = test.fit(x, y)
# summarize scores
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(x)
# summarize selected features
#print(features[0:4,:])


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#data = pd.read_csv("D://Blogs//train.csv")
#X = data.iloc[:,0:20]  #independent columns
#y = data.iloc[:,-1]    #target column i.e price range
#apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(x,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(x.columns)
#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']  #naming the dataframe columns
print(featureScores.nlargest(10,'Score'))  #print 10 best features


AttributeError: 'numpy.ndarray' object has no attribute 'columns'
# Create and fit selector
selector = SelectKBest(f_classif, k=7)
selector.fit(X, Y)
# Get columns to keep and create new dataframe with those only
cols = selector.get_support(indices=True)
features_df_new = dataset.iloc[:,cols]
x = features_df_new.iloc[:, 1:6].values
 
X_train, X_test, Y_train, Y_test = train_test_split(x, Y, test_size=0.20, random_state=1)
# Spot Check Algorithms
models = []
models.append(('Extra Trees',ExtraTreesClassifier()))
models.append(('Decision Tree', DecisionTreeClassifier()))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0)))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear')))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))

# Feature Selection with Univariate Statistical Tests
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
# load data
dataset = pd.read_csv("final_rt_feat.csv")

X= dataset.iloc[:, 1:12].values
Y = dataset.iloc[:, 13].values
# feature extraction
test = SelectKBest(score_func=f_classif, k=5)
fit = test.fit(X, Y)
# summarize scores
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
# summarize selected features
print(features[0:4,:])

print(len(dataset.columns))
10
# Feature Extraction with RFE
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
# load data
dataset = pd.read_csv("final_temp_feat.csv")
#print(len(dataset.columns))
dataset.fillna(0.999, inplace=True)
X = dataset.iloc[:, 1:8].values
Y = dataset.iloc[:, 9].values
# feature extraction
#model = LogisticRegression(solver='lbfgs')
model =RandomForestClassifier(n_estimators=200)
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)


# Feature Importance with Extra Trees Classifier
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
# load data
# load data
dataset = pd.read_csv("final_temp_feat.csv")
#print(len(dataset.columns))
dataset.fillna(0.999, inplace=True)
X = dataset.iloc[:, 1:8].values
Y = dataset.iloc[:, 9].values
# feature extraction
#model = ExtraTreesClassifier(n_estimators=10)
model =RandomForestClassifier(n_estimators=100)
model.fit(X, Y)
print(model.feature_importances_)

#add rows to DataFrame
import pandas as pd
dataset = pd.read_csv("extracted_all_feat.csv")
dataset2 = pd.read_csv("extracted_Annual_bonus_feat.csv")
out = dataset.append(dataset2)
with open('8.csv', 'w', encoding='utf-8') as f:
    out.to_csv(f, index=False)
    
# Spot Check Algorithms
models = []
models.append(('Decision Tree', DecisionTreeClassifier(class_weight="balanced")))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0,class_weight="balanced")))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear',class_weight="balanced")))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='roc_auc')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))

# Spot Check Algorithms
models = []
models.append(('Decision Tree', DecisionTreeClassifier(class_weight="balanced")))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0,class_weight="balanced")))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear',class_weight="balanced")))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))

# Spot Check Algorithms
models = []
models.append(('Decision Tree', DecisionTreeClassifier(class_weight="balanced")))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0,class_weight="balanced")))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear',class_weight="balanced")))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='recall')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))

# Spot Check Algorithms
models = []
models.append(('Decision Tree', DecisionTreeClassifier(class_weight="balanced")))

#models.append(('Random Forest', RandomForestClassifier(n_estimators=100)))
models.append(('Random Forest',RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0,class_weight="balanced")))
#models.append(('Logistic Regression', LogisticRegression(solver='lbfgs')))
models.append(('Logistic Regression', LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear',class_weight="balanced")))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='f1')
    results.append(cv_results)
    names.append(name)
    print('%s: %f' % (name, cv_results.mean()))
