# monte carlo simulation for last 100
# purpose: check whether last 100's mean error is statistically small enough 

from utils import * 
from RED import * 
import random

weatherHistory_path = os.path.join(utils.mypath, 'Storage', 'weatherHistory_cleaned.csv')
weatherHistory = pd.read_csv(weatherHistory_path, index_col = [0])

# 1000 sets of simulated predictions
simulations = 1000
result = []
for j in range(simulations):
    rand_result = {
        'Summary': random.choice(weatherHistory['Summary'].unique()),
        'Precip Type': random.choice(weatherHistory['Precip Type'].unique()),
        'Temperature (C)': random.uniform(0,1), 
        'Apparent Temperature (C)': random.uniform(0,1),
        'Humidity': random.uniform(0,1),
        'Wind Speed (km/h)': random.uniform(0,1),
        'Wind Bearing (degrees)': random.uniform(0,1),
        'Visibility (km)': random.uniform(0,1),
        'Loud Cover': random.choice(weatherHistory['Loud Cover'].unique()),
        'Pressure (millibars)': random.uniform(0,1),
        'Timestamp diff to next': random.choice(weatherHistory['Timestamp diff to next'].unique())
    }
    
    arr_1 = pd.DataFrame({'index':rand_result}).T[weatherHistory.columns].values
    
    # randomized outcome 
    rand_outcome = random.choice(range(len(weatherHistory)))
    arr_2 = weatherHistory.iloc[[rand_outcome]].values
    
    error = eucl_dist(arr_1, arr_2)
    result.append(error)

# save monte carlo simulation results
save_path = os.path.join(utils.mypath, 'Result', 'monte_carlo_result.json')
utils.save_json(result, save_path)