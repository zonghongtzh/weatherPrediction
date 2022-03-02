# retrospective euclidean distance

from utils import * 

def eucl_dist(arr_1, arr_2):
    # function calculates euclidean distance between 2 matrices
    # uses d2 from https://math.stackexchange.com/questions/507742/distance-similarity-between-two-matrices
    
    diff_matrix = arr_1 - arr_2
    dist = sum(sum(diff_matrix ** 2)) ** 0.5
    
    return dist

def RED_calculation(predictor_df, historical_df, post = False):
    # retrospective euclidean distance calculation (RED)
    # takes a given target dataframe and retrospectively calculates eucl. dist from all prior data
    
    # parameters
    # all dataframe must have numbered index, the indexes are used to map predictors to predicted results
    # post: if True, calculates beyond predictor_df's index, else if False, calculates only up to predictor_df's index, filling the rest of the data with NaN
    
    n = len(predictor_df)
    predictor_values = predictor_df.values
    predictor_index = predictor_df.index[0]
    
    result = {} # map bounds of dataframe with eucl dist
    for i in range(len(historical_df)):

        # if post == False, all results post predictor_df's index = np.NaN (No forward looking)
        if (i >= predictor_index) & (post == False):
            result[(i, i + n)] = np.NaN
            continue

        hist_values = historical_df.iloc[i:i+n].values
        dist = eucl_dist(predictor_values, hist_values)
        result[(i, i + n)] = dist
        
    return result
        
