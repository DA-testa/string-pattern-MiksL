def read_input():    
    inputType = input()
    if(inputType[:1] == "F"):
        # Assume the only test file is 06 and it is in the tests/ directory
        fileName = "tests/06"
        try:
            with open(fileName) as readableFile:
                # The input - 2 strings, first is the pattern, second is the text, they're separated by a space
                pattern = readableFile.readline()
                text = readableFile.readline()
        except FileNotFoundError:
            print("Invalid file name or path")
            return
    elif(inputType[:1] == "I"):
        pattern = input()
        text = input()
    else:
        print("Invalid input character")
        return
    
    return pattern.rstrip(), text.rstrip()

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # Initialize a list of matched pattern positions
    matchedPatternPositions = []
    
    # Variables for the length of the pattern and the text
    patternLength = len(pattern)
    textLength = len(text)
    
    # Get the hash value of the pattern to compare to
    hashPattern = getHash(pattern)
    
    # Iterate through the text and compare the hash values of the pattern and the text, if they match, compare the strings
    for patternStartIndex in range(textLength - patternLength + 1):
        # text[patternStartIndex : patternStartIndex+patternLength] - Substring of the text, starting at the current index and ending at the current index + the length of the pattern
        if getHash(text[patternStartIndex : patternStartIndex+patternLength]) == hashPattern:
            if text[patternStartIndex : patternStartIndex+patternLength] == pattern:
                matchedPatternPositions.append(patternStartIndex)
    
    return matchedPatternPositions

# Function uses the DJB2 hashing algorithm because of its simplicity and speed
def getHash(stringToHash):
    hashNumber = 5381
    for(char) in stringToHash:
        hashNumber = ((hashNumber << 5) + hashNumber) + ord(char)
    return hashNumber

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

