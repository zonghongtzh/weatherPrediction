# data management 
from utils import * 

def data_cleaning(weatherHistory):
    '''
    If timestamp to next is uncommonly long, the data should not be selected by algorithm
    e.g. 
    |Loud Cover | Pressure (millibars)| Daily Summary| Timestamp | Timestamp diff to next|
    |L1         | P1                  | DS1          | T1        | 3600                  |
    
    should not match with 
    e.g. 
    |Loud Cover | Pressure (millibars)| Daily Summary| Timestamp | Timestamp diff to next|
    |L2         | P2                  | DS2          | T2        | 120272400             |
    
    bcos of timestamp difference
    
    '''
    
    # Add timestamp difference
    weatherHistory['Timestamp'] = weatherHistory['Formatted Date'].apply(lambda x: datetime.datetime.strptime(x[:-10],'%Y-%m-%d %H:%M:%S').timestamp())
    weatherHistory['Timestamp diff to next'] = weatherHistory['Timestamp'].diff().shift(-1)
    
    # remove non-factors
    non_factor_cols = [
        'Formatted Date',
        'Daily Summary'
    ]
    factor_cols = [col for col in weatherHistory.columns if col not in non_factor_cols]
    weatherHistory = weatherHistory[factor_cols]
    
    return weatherHistory


def convert_object_to_int(weatherHistory):
    # find columns containing non-floats
    data_types = weatherHistory.dtypes
    non_float_cols = data_types[data_types != float].index.tolist() 
    
    # convert object to numbers
    # e.g. Partly Cloudy -> 0.0, 'Mostly Cloudy': 1.0, ...
    for non_float_col in non_float_cols:
        items = weatherHistory[non_float_col].unique()
        mapping = {
            items[i]:float(i)
            for i in range(len(items))
        }
        weatherHistory[non_float_col] = weatherHistory[non_float_col].apply(lambda x: mapping[x])
    
    return weatherHistory
    

if __name__ == "__main__":
    # data
    weatherHistory_path = os.path.join(utils.mypath, 'Storage', 'weatherHistory.csv')
    weatherHistory = pd.read_csv(weatherHistory_path)
    
    weatherHistory = data_cleaning(weatherHistory)
    weatherHistory = convert_object_to_int(weatherHistory)
    
    save_path = os.path.join(utils.mypath, 'Storage', 'weatherHistory_cleaned.csv')
    weatherHistory.to_csv(save_path)