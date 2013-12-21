Sampling-techniques
===================

Initially developed for Kaggle's Expedia contest

It uses the idea of 1st breaking the "train" sample into cv, test & train, but with an additional twist - all "rows" for a particular search query results - meaning ONE travel should go in one file (train, test or cv) - with this I havce tried to write a *near* optimal code, since I will need to scan & base the groupings by search_id for the hotel booking/travel query. 



The file sample_expedia.py creates train, test and cross validation datasets in sklearn (python 2.7) with a grouping constraints . To understand what this module does, see also my post in stackoverflow - http://stackoverflow.com/questions/18864754/creating-train-test-and-cross-validation-datasets-in-sklearn-python-2-7-with

Solved what I was looking for with a custom module, though it would be helpful to others looking at similar use-case
Also note that code was not written for very large data in mind(rather just as a quick, yet neat prototype), so it's not very efficient. Should you FORK this code - please point out how can I improve the run-time.

