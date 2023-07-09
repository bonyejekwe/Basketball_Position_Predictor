# Basketball_Position_Predictor
A series of models to predict NBA basketball positions based on player data.

## Files:
**-data/:** Collection of csv files, each representing a regular season player data for a specific season (from 2002-03 onward). Data loaded from Basketball-Reference.com.

**-get_stats.py:** Clean data and concatenate data into a single dataframe. Filter out unwanted data (based on games played, games started, or minutes played) and return either with 3 position categories ("G", "F", "C") or 5 position categories ("PG", "SG", "SF", "PF", "C")

## Results:

### KNN_Model.ipynb: k-Nearest Neighbor model

*3POS Val Accuracy: **0.79285** | 3POS Test Accuracy: **0.80910***

*5POS Val Accuracy: **0.63003** | 5POS Test Accuracy: **0.64598***

### RF_Model.ipynb: random forest model

*3POS Val Accuracy: **0.81516** | 3POS Test Accuracy: **0.81974***

*5POS Val Accuracy: **0.67376** | 5POS Test Accuracy: **0.69799***

### SVM_Model.ipynb: support vector classsifier model

*3POS Val Accuracy: **0.81634** | 3POS Test Accuracy: **0.82979***

*5POS Val Accuracy: **0.68041** | 5POS Test Accuracy: **0.70331***


## Timeline

**16 Nov 2021:** Initial project created (originally was the final group project for DS 3000: Foundations of Data Science)

**26 June 2023:** Develop pipeline for each model 