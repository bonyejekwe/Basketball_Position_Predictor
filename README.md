# Basketball_Position_Predictor
A series of models to predict NBA basketball positions based on player data.

**Files:**

-KNN_Model.ipynb: k-Nearest Neighbor model for 3 position (Guard, Forward, and Center) characterization, using data from [NBAstuffer](https://www.nbastuffer.com/2021-2022-nba-player-stats/) from 2018 to 2021. Incorporates feature scaling, grid search for optimal k value, feature selection, and cross validation.

-KNN_Model2.ipynb: k-Nearest Neighbor model for 5 position (Point Guard, Shooting Guard, Small Forward, Power Forward, and Center) characterization, using data from [Basketball Reference](https://www.basketball-reference.com/leagues/NBA_2022_advanced.html/).

-get_stats.py: retrieve and clean data from both websites, concatenating returning dataframes from across multiple seasons.

-Other_Models.ipynb: other models and techniques for player classification (Support Vector Machine, Random Forest, Decision Tree, Bagging, AdaBoost, Gradient Tree Boosting).
