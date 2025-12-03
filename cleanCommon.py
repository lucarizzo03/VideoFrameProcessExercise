import re 
import collections


def cleanCount(input):
    
    if not input:
        print("No message")
        return None
    
    # remove punctuation
    cleanedInput = re.sub(r'[^\w\s]', '', input)
    
    if not cleanedInput:
        print("no message 2")
        return None
    
    lowerCleanedInput = cleanedInput.lower()
    
    splitLCI = lowerCleanedInput.split()
    
    wordTotal = collections.Counter(splitLCI)
    
    print(wordTotal)
    
    mostCommon = wordTotal.most_common(4)
    
    if mostCommon:
        return mostCommon[0][0]
    
    return "No Common Word"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    input_text = "Data is messy. Data is fun! data... IS useful."
    # Expected Output: 'data' (It appears 3 times: "Data", "Data", "data")

    # Tricky Case: Empty string or just symbols
    tricky_input = "!!! ??? ..."
    # Expected Output: "" (Empty string, no words found)
    
    result = cleanCount(tricky_input)
    print(result)
    
    


