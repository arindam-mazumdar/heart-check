# HeartCheck
### Predicting heart-diesease risk from life style

## Motivation
Medical practioner calculate the the possibility of developing heart disease from the clinical and pathological investigations like different blood works, measurements of blood pressure etc. Then those informations are used in some linear and non-linear regression formula established by Gross et.al.( DOI: 10.1161/01.cir.0000437741.48606.98). However, most of the time the high blood pressure and hyperglycemia (High Cholesterol) remians undetected. In this project we try to predict the probability that an user has already developed heart disease from a set of life style questions. If the probability is sufficiently high, the user can visit doctor and get the clinical assessments done. Our app also shows which factor of lifestyle is contributing most in developing heart-disease. 

## Data
The project uses the BRFSS data which is collected by CDC annually. The data contains the answers to different behaviour question like smoking, drinking, physical acitivity history of different persons collected over different states in USA. Along with that the data also contains the some medical history of the patients. The source of the data is : CDC - 2020 BRFSS Survey Data and Documentation (https://www.cdc.gov/brfss/annual_data/annual_2020.html). The original ASCII data converted to csv following cdc codebook. Please refer to "**asc_to_csv**" notebook or  "ASCII_to_CSV_coversion.py" file. This takes several hours on a single processor.

### Data Cleaning
Data cleaing in performed in the "**data_cleaning.ipynb**" notebook. These cleaing typically takes care of filtering missing values and an-answered question. Even after that there remains some bad data, which are rejected in the model building process. For example the sleeping hours histogram shows:

![Bad Sleeping-hours data](https://github.com/arindam-mazumdar/heart-check/blob/main/sleeping_bad.png)

That there are some sleeping hours which are above 70 hrs. These data points are eventually rejected. 

## Data Analysis
The analysis and visualizations of data are in "**analysis_and_visualization.ipynb**" notebook. The data shows clear trend of varying probablility of heart-disease with different features. For instance, in the following bar-plot we see the consistent increase in heart-disease probability with age:

![Age -vs- Heart Disease proability](https://github.com/arindam-mazumdar/heart-check/blob/main/age.png)

( age : 18-99 years are divided in 13 groups. To see exact groups follow the flask app: https://heart-check-cdc.herokuapp.com/)

## Model
We use a Naive Bayes classifier to predict probability for developing heart-disease. Other classification method fails to predict the probability realistically since the data is highly imbalanced. DecisionTree, K-NN, Logistic Regression these kind of classifiers predicts the outcome with 91-92% accuracy. However, if we look at the F1-score and the confussion matrix we find that they fail misearably to predict even a single positive case. The reason is the data is originally highly imbalanced, i.e. the positive case 'MICHD'=1 is only 8% of data. There are many method to overcome the problem of imbalanced class. However, we do not use those since our aim is not to target a prticular user and predict if he or she is going to get heart-attack. Rather, we would like to find the probability of developing heart-disease and how much greater or less that is compared to the other healthy individuals. Therefore we choose Naive-Bayes classifer. 

For the purpose of finding out most important factor we use the conditional independence assumption and selects out that factor with highest conditional probability of occurring heart disease. We build a flask app which takes 2 general information (age and gender) and 6 different life-style questions and predict the probability of that you have already developed a heart disease. For example, an individual of 18-24 years of age, Male, with "Current smoker - now smokes some days", 'No physical activity or exercise in last 30 days', "Heavy Drinking" and sleeping 5 hours a day the contributing factor to his risk of developing heart disease looks like:


![Contribution of different factors](https://github.com/arindam-mazumdar/heart-check/blob/main/pie.png)


## Heart-Check App:
The falsk_app folder contains necessary files for creating the app. The NaiveBayes model and the factor's conditional probability is calculated in "**model.py**" file within the folder. 

Please refer to app webpage: https://heart-check-cdc.herokuapp.com/
Calculate your own risk.
