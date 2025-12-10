import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

__locations = None
__d_col = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    global a
    try:
        location_index = __d_col.index(location.lower())
    except:
        location_index = -1

    a = np.zeros(len(__d_col))
    a[0] = sqft
    a[1] = bath
    a[2] = bhk
    if location_index >= 0:
        a[location_index] = 1
    return round(__model.predict([a])[0],2) # this will be a float number so it will be till 2 decimal places

# This function will read the column.json and returns the list of all the location starting from 4th column
def get_loc_name():
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts ... start')
    global __d_col # global variables
    global __locations

    with open('./artifacts/columns.json','r') as f:
        __d_col = json.load(f)['d_col'] # whatever object is loaded it will be converted into a dictionary
        __locations = __d_col[3:] # by using python index slicing

    with open('./artifacts/house_price_model.pickle','rb') as f:
        global __model
        __model = pickle.load(f)
    print('loading the artifacts is dont.')

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_loc_name())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('5th block hbr layout', 1000, 2, 2))
    print(get_estimated_price('benson town', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))