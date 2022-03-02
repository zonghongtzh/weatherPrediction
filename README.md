# weatherPrediction
Predicting weather using retrospective euclidean distance algorithm

## Concept
The simple concept of the project is as follows:
1. Take a current sequence of weather events (predictor)
![current_event](https://i.imgur.com/yLpaZmd.png)
2. Look back into the past data to find the most similar past sequence of weather event (measured by euclidean distance)
![past_event](https://i.imgur.com/UYoL29h.png)
3. Take most similar past weather event's outcome (prediction)
![prediction](https://i.imgur.com/MIJYj1u.png)
4. as the predicted outcome of the current sequence of weather events (outcome)
![outcome](https://i.imgur.com/XFpndtW.png)

## Analysis
p-value: 0.0005368 (statistically significantly non-random) 

The algorithm shows a remarkable ability to predict the subsequent weather patterns using past weather patterns. This is to be expected given the deterministic nature of weather. It is very likely that the algorithm will work even better given more granular data. 

Furthermore, the predicted outcomes can itself form a predictor of further future weather patterns
