Sampling-techniques
===================

Initially developed for Kaggle's Expedia contest

It uses the idea of 1st breaking the "train" sample into cv, test & train, but with an additional twist - all "rows" for a particular search query results - meaning ONE travel should go in one file (train, test or cv) - with this I havce tried to write a *near* optimal code, since I will need to scan & base the groupings by search_id for the hotel booking/travel query. 

