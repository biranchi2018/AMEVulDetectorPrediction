import numpy as np


def get_pattern_feature():
    train_total_name_path = "./graph_feature/reentrancy/contract_name_train.txt"
    test_total_name_path = "./graph_feature/reentrancy/contract_name_valid.txt"
    pattern_feature_path = "./pattern_feature/feature_FNN/reentrancy/"

    final_pattern_feature_train = []  # pattern feature train
    pattern_feature_train_label_path = "./pattern_feature/feature_zeropadding/reentrancy/label_by_extractor_train.txt"

    final_pattern_feature_test = []  # pattern feature test
    pattern_feature_test_label_path = "./pattern_feature/feature_zeropadding/reentrancy/label_by_extractor_valid.txt"

    f_train = open(train_total_name_path, 'r')
    lines = f_train.readlines()
    for line in lines:
        line = line.strip('\n').split('.')[0]
        tmp_feature = np.loadtxt(pattern_feature_path + line + '.txt')
        final_pattern_feature_train.append(tmp_feature)

    f_test = open(test_total_name_path, 'r')
    lines = f_test.readlines()
    for line in lines:
        line = line.strip('\n').split('.')[0]
        tmp_feature = np.loadtxt(pattern_feature_path + line + '.txt')
        final_pattern_feature_test.append(tmp_feature)

    # labels of extractor (train)
    label_by_extractor_train = []
    f_train_label_extractor = open(pattern_feature_train_label_path, 'r')
    labels = f_train_label_extractor.readlines()
    for label in labels:
        label_by_extractor_train.append(label.strip('\n'))

    # labels of extractor (valid)
    label_by_extractor_valid = []
    f_test_label_extractor = open(pattern_feature_test_label_path, 'r')
    labels = f_test_label_extractor.readlines()
    for label in labels:
        label_by_extractor_valid.append(label.strip('\n'))

    for i in range(len(final_pattern_feature_train)):
        final_pattern_feature_train[i] = final_pattern_feature_train[i].tolist()

    for i in range(len(final_pattern_feature_test)):
        final_pattern_feature_test[i] = final_pattern_feature_test[i].tolist()

    return final_pattern_feature_train, final_pattern_feature_test, label_by_extractor_train, label_by_extractor_valid


def get_graph_feature():
    graph_feature_train_data_path = "./graph_feature/reentrancy/reentrancy_final_train.txt"
    graph_feature_train_label_path = "./graph_feature/reentrancy/label_by_experts_train.txt"

    graph_feature_test_data_path = "./graph_feature/reentrancy/reentrancy_final_valid.txt"
    graph_feature_test_label_path = "./graph_feature/reentrancy/label_by_experts_valid.txt"

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


if __name__ == "__main__":
    pattern_train, pattern_test, pattern_experts_train, pattern_experts_test = get_pattern_feature()
    graph_train, graph_test, graph_experts_train, graph_experts_test = get_graph_feature()
    print("-" * 50)
    print(f"pattern_train.shape : {np.array(pattern_train).shape}")
    print(f"pattern_test.shape : {np.array(pattern_test).shape}")

    # pattern_train.shape : (1338, 3, 250)
    # pattern_test.shape : (333, 3, 250)

    print(f"pattern_train[:2] : {pattern_train[:2]}")
    print(f"pattern_test[:2] : {pattern_test[:2]}")

    print("-" * 50)
    print(f"graph_train.shape : {np.array(graph_train).shape}")
    print(f"graph_test.shape : {np.array(graph_test).shape}")

    # graph_train.shape : (1338, 1, 250)
    # graph_test.shape : (333, 1, 250)

    print(f"graph_train[:2] : {graph_train[:2]}")
    print(f"graph_test[:2] : {graph_test[:2]}")
    
    print()

