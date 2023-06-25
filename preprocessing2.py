import numpy as np
import os

def get_pattern_feature():
    train_total_name_path = "./graph_feature/reentrancy/contract_name_train.txt"  	## Gets the .sol filename
    test_total_name_path = "./graph_feature/reentrancy/contract_name_valid.txt"		## Gets the .sol filename
    pattern_feature_path = "./pattern_feature/feature_FNN/reentrancy/"				## Get the pattern vector

    final_pattern_feature_train = []  # pattern feature train
    pattern_feature_train_label_path = "./pattern_feature/feature_zeropadding/reentrancy/label_by_extractor_train.txt"

    final_pattern_feature_test = []  # pattern feature test
    pattern_feature_test_label_path = "./pattern_feature/feature_zeropadding/reentrancy/label_by_extractor_valid.txt"

    f_train = open(train_total_name_path, 'r')
    lines = f_train.readlines()
    for line in lines:
        line = line.strip('\n').split('.')[0]
        tmp_feature = np.loadtxt(pattern_feature_path + line + '.txt')				## Reads the .sol code
        final_pattern_feature_train.append(tmp_feature)		

    f_test = open(test_total_name_path, 'r')
    lines = f_test.readlines()
    for line in lines:
        line = line.strip('\n').split('.')[0]
        tmp_feature = np.loadtxt(pattern_feature_path + line + '.txt')				## Reads the .sol code
        final_pattern_feature_test.append(tmp_feature)

    # labels of extractor (train)
    label_by_extractor_train = []
    f_train_label_extractor = open(pattern_feature_train_label_path, 'r')			## Reads the actual label
    labels = f_train_label_extractor.readlines()
    for label in labels:
        label_by_extractor_train.append(label.strip('\n'))

    # labels of extractor (valid)
    label_by_extractor_valid = []
    f_test_label_extractor = open(pattern_feature_test_label_path, 'r')				## Reads the actual label
    labels = f_test_label_extractor.readlines()
    for label in labels:
        label_by_extractor_valid.append(label.strip('\n'))
        
    #print(f"final_pattern_feature_train[:2] : {final_pattern_feature_train[:2]}")
    #print(f"label_by_extractor_train[:2] : {label_by_extractor_train[:2]}")

    for i in range(len(final_pattern_feature_train)):
        final_pattern_feature_train[i] = final_pattern_feature_train[i].tolist()

    for i in range(len(final_pattern_feature_test)):
        final_pattern_feature_test[i] = final_pattern_feature_test[i].tolist()

    return final_pattern_feature_train, final_pattern_feature_test, label_by_extractor_train, label_by_extractor_valid


def get_graph_feature():
#     graph_feature_train_data_path = "./graph_feature/reentrancy/reentrancy_final_train.txt"
#     graph_feature_train_label_path = "./graph_feature/reentrancy/label_by_experts_train.txt"

#     graph_feature_test_data_path = "./graph_feature/reentrancy/reentrancy_final_valid.txt"
#     graph_feature_test_label_path = "./graph_feature/reentrancy/label_by_experts_valid.txt"

    graph_feature_test_data_path = "./graph_feature/reentrancy/reentrancy_final_valid.txt"

    #  labels of experts definition
    label_by_experts_train = []
    f_train_label_expert = open(graph_feature_train_label_path, 'r')
    labels = f_train_label_expert.readlines()
    for label in labels:
        label_by_experts_train.append(label.strip('\n'))

    label_by_experts_valid = []
    f_test_label_expert = open(graph_feature_test_label_path, 'r')
    labels = f_test_label_expert.readlines()
    for label in labels:
        label_by_experts_valid.append(label.strip('\n'))

    graph_feature_train = np.loadtxt(graph_feature_train_data_path).tolist()  # graph feature train
    graph_feature_test = np.loadtxt(graph_feature_test_data_path, delimiter=", ").tolist()  # graph feature test

    for i in range(len(graph_feature_train)):
        graph_feature_train[i] = [graph_feature_train[i]]

    for i in range(len(graph_feature_test)):
        graph_feature_test[i] = [graph_feature_test[i]]

    return graph_feature_train, graph_feature_test, label_by_experts_train, label_by_experts_valid



def check_if_file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False
    

def get_pattern_feature_for_prediction(sol_file_name):
    base_file_with_ext = sol_file_name.split("/")[-1]
    base_file_name = base_file_with_ext.split(".")[0]
    
    print(f"base_file_with_ext : {base_file_with_ext}")
    print(f"base_file_name : {base_file_name}")
    
    # pattern feature test
    final_pattern_feature_test = []  
    
    # labels of extractor (valid)
    label_by_extractor_valid = []

    
    reentrancy_pattern_feature_path = f"./pattern_feature/feature_FNN/reentrancy/{base_file_name}.txt"				## Get the pattern vector
    #timestamp_pattern_feature_path = f"./pattern_feature/feature_FNN/timestamp/{base_file_name}.txt"

    tmp_feature = np.loadtxt(reentrancy_pattern_feature_path)									## Reads the .sol feature vector code
    final_pattern_feature_test.append(tmp_feature)
    print()
    print('*' * 50)
    print(f"1.final_pattern_feature_test.shape : {np.array(final_pattern_feature_test).shape}")
    print()

    #tmp_feature = np.loadtxt(timestamp_pattern_feature_path)									## Reads the .sol feature vector code
    #final_pattern_feature_test.append(tmp_feature)
    #print(f"2.final_pattern_feature_test.shape : {np.array(final_pattern_feature_test).shape}")
    print('*' * 50)
    print()


    reentrancy_pattern_feature_test_label_path = f"./pattern_feature/label_by_extractor/reentrancy/{base_file_with_ext}"
    #timestamp_pattern_feature_test_label_path = f"./pattern_feature/label_by_extractor/timestamp/{base_file_with_ext}"

    f_test_label_extractor = open(reentrancy_pattern_feature_test_label_path, 'r')				## Reads the actual label
    labels = f_test_label_extractor.readlines()
    for label in labels:
        label_by_extractor_valid.append(label.strip('\n'))

    #f_test_label_extractor = open(timestamp_pattern_feature_test_label_path, 'r')				## Reads the actual label
    #labels = f_test_label_extractor.readlines()
    #for label in labels:
        #label_by_extractor_valid.append(label.strip('\n'))

    #print()
    #print(50 * '-')
    #print(f"label_by_extractor_valid[:2] : {label_by_extractor_valid[:2]}")

    for i in range(len(final_pattern_feature_test)):
        final_pattern_feature_test[i] = final_pattern_feature_test[i].tolist()

    #print(f"final_pattern_feature_test[:2] : {final_pattern_feature_test[:2]}")
    #print(50 * '-')
    #print()

    return final_pattern_feature_test, label_by_extractor_valid
    

'''
if __name__ == "__main__":
    # pattern_train, pattern_test, pattern_experts_train, pattern_experts_test = get_pattern_feature()
#     graph_train, graph_test, graph_experts_train, graph_experts_test = get_graph_feature()
    sol_file_name = './source_code/Crowdfunding.sol'
#     sol_file_name = './source_code/Crowdfunding.sol'
    pattern_test, pattern_experts_test = get_pattern_feature_for_prediction(sol_file_name)
    
    #print(f"pattern_test.shape : {np.array(pattern_test).shape}")
    print(f"pattern_experts_test.shape : {np.array(pattern_experts_test).shape}")
    
    print()
    print('Done')
'''
