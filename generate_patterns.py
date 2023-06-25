
from pattern_extractor_example.PatternExtract_IF import generate_IF
from pattern_extractor_example.PatternExtract_RE import generate_RE
from pattern_extractor_example.PatternExtract_TS import generate_TS

def generate_pattern_for_file(filename):
    inputFileDir = "./source_code/"
    
    #----- IF --------
    outputfeatureDir = "./pattern_feature/feature_zeropadding/loops/"
    outputfeatureFCDir = "./pattern_feature/feature_FNN/loops/"
    outputlabelDir = "./pattern_feature/label_by_extractor/loops/"

    generate_IF(filename, inputFileDir, outputfeatureDir, outputfeatureFCDir, outputlabelDir)
    
    #----- RE --------    
    outputfeatureDir = "./pattern_feature/feature_zeropadding/reentrancy/"
    outputfeatureFCDir = "./pattern_feature/feature_FNN/reentrancy/"
    outputlabelDir = "./pattern_feature/label_by_extractor/reentrancy/"

    generate_RE(filename, inputFileDir, outputfeatureDir, outputfeatureFCDir, outputlabelDir)

    #----- TS --------    
    outputfeatureDir = "./pattern_feature/feature_zeropadding/timestamp/"
    outputfeatureFCDir = "./pattern_feature/feature_FNN/timestamp/"
    outputlabelDir = "./pattern_feature/label_by_extractor/timestamp/"

    generate_TS(filename, inputFileDir, outputfeatureDir, outputfeatureFCDir, outputlabelDir)
    print(f"Pattern generation completed !!!")
    

'''
if __name__ == "__main__":
    filename = 'Crowdfunding.sol'
    generate_pattern_for_file(filename)
    print("Completed !!!")
'''