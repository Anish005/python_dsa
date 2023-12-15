'''Two strings are called twins if they can be made equivalent by performing some number of operations on one or both strings. There are two possible operations:

• SwapEven: Swap a character at an even- numbered index with a character at another even-numbered index.
SwapOdd: Swap a character at an odd- numbered index with a character at another odd-numbered index.

There will be two string arrays. At each index of the two arrays, compare a string from each array, aligned by index, and store the result in a final string array. The return array should consist of strings either "Yes" or "No", based on whether the strings compared are twins or not.

Example

firstString = ["abcd", "abcd"]

secondString = ["cbad", "adbc"]'''


def are_twins(firstString, secondString):
    result = []
    
    for str1, str2 in zip(firstString, secondString):
        if len(str1) != len(str2):
            result.append("No")
            continue
        
        even_str1 = [str1[i] for i in range(len(str1)) if i % 2 == 0]
        odd_str1 = [str1[i] for i in range(len(str1)) if i % 2 != 0]
        
        even_str2 = [str2[i] for i in range(len(str2)) if i % 2 == 0]
        odd_str2 = [str2[i] for i in range(len(str2)) if i % 2 != 0]
        
        even_str1.sort()
        even_str2.sort()
        odd_str1.sort()
        odd_str2.sort()
        
        if even_str1 == even_str2 and odd_str1 == odd_str2:
            result.append("Yes")
        else:
            result.append("No")
    
    return result

# Example usage:
firstString = ["abcd", "abcd"]
secondString = ["cbad", "adbc"]

final_result = are_twins(firstString, secondString)
print(final_result)
