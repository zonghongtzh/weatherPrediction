# retrospective euclidean distance

from utils import * 
from RED import * 

if __name__ == "__main__":

    df_path = os.path.join(utils.mypath, 'Storage', 'weatherHistory_cleaned.csv')
    df = pd.read_csv(df_path, index_col = [0])

    # testing last 100 datasets in 2 step-wise
    # data is from 2016-09-05 to 2016-09-09
    test_dataset = df.iloc[-100:]
    historical_df = df.copy(deep = True)
    stepwise = 2
    top = 10

    # run analysis
    result = RED(test_dataset, historical_df, stepwise, top)

    save_path = os.path.join(utils.mypath, 'Result', 'last_1.json')
    utils.save_json(result, save_path)