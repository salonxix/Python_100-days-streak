def removeDigit(number: str, digit: str) -> str:
    max_result = ""
    
    for i in range(len(number)):
        if number[i] == digit:
            new_number = number[:i] + number[i+1:]
            if new_number > max_result:
                max_result = new_number
                
    return max_result

# 🔍 Test Cases
print(removeDigit("123", "3"))     # Output: "12"
print(removeDigit("1231", "1"))    # Output: "231"
print(removeDigit("551", "5"))     # Output: "51"
