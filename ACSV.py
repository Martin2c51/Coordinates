import pandas as pd

def a_csv(coords,nums, file_name):
    """Pass store and address in list format, coordinates as is returned by the function object
    Get Coordinate and file name in strings.
    Returns a dataframe with the store, address, latitude and longitude columns and generates its corresponding
    csv file """
        
    output = pd.DataFrame(coords, columns=['coords'])
    output['nums'] = nums


    
    output.to_csv(file_name, index = False)
    
    return output

