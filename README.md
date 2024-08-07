# Predictive Maintenance

## Table of Contents
[Overview](#overview)

[EDA](#eda)

[Hypothesis Test](#hypothesis-test)

[Regression Model](#regression-model)

## Overview
This dataset contains telemetry data recorded from 100 machines every hour for a year.
This comes out to 100 * 24 * 365 or 876000 rows with 9 features each. 
## EDA
For the purposes of this project I decided to use the machines failures as the dependent variable and therefore had to manipulate my data in specific ways to accommodate that. 
Firstly, I created a new column called 'future-fail'. This column checks the 'failureID' column using the .rolling method, to see if there has been a failure of any kind in the last 24 hours for a given machine. If there has been the columns value is True, otherwise it is False. Additionally, I elected not to use the maintenance data because it had multiples entries per machine per hour which caused a serious headache while indexing. Lastly I used pd.dummies to make my categorical data of errors and models into binary values that can be used for my regression model later.
## Hypothesis Test

### Null Hypothesis 
The distribution of a qualitative feature ('volt', 'rotate', 'pressure', 'vibration') with a False value for 'future_fail' is the same as that feature with a True value.
### Alternate Hypothesis
The distribution of a qualitative feature with a False value in 'future_fail' is not the same as that features distribution with a True value.
### Testing Method
I chose a Welch's T-test because the qualitative features fall in a normal distribution. 

The binary values found in the 'future_fail' column do not have a variance therefore Welch's T-test was chosen over the students T-test.
### Conclusion
The test concluded that all 4 qualitative features had seperate distributions for both True and False values therefore the Null hypothesis was rejected.

## Predictive Model

### Goal
My goal is to make a model using some number of features that can most effectively predict wheteher or not a machine will encounter an error in the next 24 hours.
### Model Type
I used a logistic regression model because it was the model most appropriate for predicting binary like the ones found in 'future_fail'. 

The model uses a standard train to test ratio of 0.8 to 0.2 and has a maximum number of iterations of 1000 to accomadate the large amount of data.

### Features 
voltage

rotation 

pressure 

vibration 

age

errorID (onehot encoded using pd.dummies)

modelID (onehot encoded using pd.dummies)

### Quality

The model is able to predict failures with a roughly 50% precision, this is very valuable because it means 50% of True predictions were in fact True.
