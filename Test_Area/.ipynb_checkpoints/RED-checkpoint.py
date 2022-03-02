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
        
def RED(target_df, reference_df, stepwise, top = 10):
    '''
    target_df = dataframe of predictors (e.g. data from 2016-09-05 to 2016-09-09)
    reference_df = dataframe of training data (e.g. data from 2006-04-01 to 2016-09-09)
    stepwise = how many rows of data to consider in calculating euclidean distance
    top = how many results to store (top n, ascending data)
    
    The function is simply a loop that breaks down target_df into each stepwise and then runs RED_calculation against reference data 
    '''
    
    result = {}
    for i in range(len(target_df) - stepwise + 1):
        predictor_df = target_df.iloc[i: i + stepwise]

        RED_result = RED_calculation(predictor_df, reference_df)
        top_n = dict(sorted(RED_result.items(), key=lambda item: item[1])[:top])
        top_n = {str(k):v for k,v in top_n.items()}

        store_key = tuple(predictor_df.index[0], predictor_df.index[1] + 1) # e.g. a df with an index of [5, 6] would need .iloc[5:7] to bound the dataframes
        result[str(tuple(predictor_df.index[0], predictor_df.index[1] + 1))] = top_n

    return result