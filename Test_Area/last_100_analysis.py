# analysis on last 100
# check for predicted vs outcome eucl dist
from utils import * 
from RED import * 

last_100_path = os.path.join(utils.mypath, 'Result', 'last_100.json')
last_100 = utils.open_json(last_100_path)

weatherHistory_path = os.path.join(utils.mypath, 'Storage', 'weatherHistory_cleaned.csv')
weatherHistory = pd.read_csv(weatherHistory_path, index_col = [0])

result = {}
for k,v in last_100.items():
    outcome_idx = eval(k)[-1]
    predict_idx = eval(list(v.items())[0][0])[-1]
    
    if outcome_idx > weatherHistory.index[-1]:
        continue

    outcome = weatherHistory.loc[[outcome_idx]].values
    prediction = weatherHistory.loc[[predict_idx]].values
    error = eucl_dist(outcome, prediction) # prediction error
    
    result[k] = error
    
result = dict(sorted(result.items(), key=lambda item: item[1]))

mean_error = np.mean(list(result.values()))
std_error = np.std(list(result.values()))

print(mean_error, std_error)