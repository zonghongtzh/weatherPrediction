# retrospective euclidean distance

from utils import * 
from RED import * 

df_path = os.path.join(utils.mypath, 'Storage', 'weatherHistory_cleaned.csv')
df = pd.read_csv(df_path, index_col = [0])

# testing last 100 datasets in 2 step-wise
# data is from 2016-09-05 to 2016-09-09
test_dataset = df.iloc[-100:]
historical_df = df.copy(deep = True)
n = 2

result = {}
for i in range(len(test_dataset) - n + 1):
    predictor_df = test_dataset.iloc[i: i + n]
    
    RED_result = RED_calculation(predictor_df, historical_df)
    top_10 = dict(sorted(RED_result.items(), key=lambda item: item[1])[:10])
    top_to = {str(k):v for k,v in top_10.items()}
    
    result[str(tuple(predictor_df.index))] = top_10
    
    if i%10 == 0:
        print(i)
        

save_path = os.path.join(utils.mypath, 'Result', 'last_100.json')
utils.save_json(result_str, save_path)