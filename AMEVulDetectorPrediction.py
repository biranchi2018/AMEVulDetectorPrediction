
from generate_patterns import generate_pattern_for_file
from preprocessing2 import get_pattern_feature_for_prediction

from models.FNNModel import FNNModel
import tensorflow as tf
import numpy as np

# args = parameter_parser()


def main():
#     filename = 'SimpleDAO.sol'	# source_code folder should be present
    filename = 'Crowdfunding.sol'
    #generate_pattern_for_file(filename)
    pattern_test, label_by_extractor_valid = get_pattern_feature_for_prediction(filename)
    #print("-" * 50)
    #print(f"pattern_test.shape : {np.array(pattern_test).shape}")
    #print(f"pattern_test[:2] : {pattern_test[:2]}")

    # pattern_train.shape : (1338, 3, 250)
    # pattern_test.shape : (333, 3, 250)

    # The testing set of patterns' feature
    pattern1test = []
    pattern2test = []
    pattern3test = []
    for i in range(len(pattern_test)):
        pattern1test.append([pattern_test[i][0]])
        pattern2test.append([pattern_test[i][1]])
        pattern3test.append([pattern_test[i][2]])

    y_test_pattern = []
    for i in range(len(label_by_extractor_valid)):
        y_test_pattern.append(int(label_by_extractor_valid[i]))
    y_test_pattern = np.array(y_test_pattern)
    
    
    #-------- Save the model ----------------------------
    model_path = f"./logs/AMEVulDetector_FNNModel.h5"
    print(f'Load Model from path : {model_path}')
    
    model = tf.keras.models.load_model(model_path)    
    #print(model.summary())
    
    try:
    	print()
    	pattern_test = np.array(pattern_test)
    	#print(f"pattern_test.shape before : {pattern_test.shape}")
    	pattern_test = np.array(pattern_test).reshape(-1, 1, 250)
    	#print(f"pattern_test.shape after : {pattern_test.shape}")
    	
    	predictions = model.predict(pattern_test)
    	print(f"predictions : {predictions}")
    	argmax = np.argmax(predictions)
    	print(f"argmax : {argmax}")
    	
    except Exception as e:
    	print(f"Exception in model.predict : {str(e)}")


if __name__ == "__main__":
    main()

