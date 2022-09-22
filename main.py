"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""
def oneEditAway(str1, str2):
    if (len(str1) == len(str2)):
        return (checkReplace(str1,str2))
    elif (len(str1) - len(str2) == 1 ):
        return (checkDelete(str1, str2))
    elif (len(str2) - len(str1) == 1 ):
        return (checkDelete(str2, str1))
    else:
        return False

def checkReplace(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            continue
        else:
            count += 1

        if count > 1:
            return False
            
    return True

def checkDelete(str1, str2):
    count = 0
    i = 0
    j = 0

    while (j < len(str2)):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            count += 1
            if count > 1:
                return False
            i += 1
            if (str1[i] != str2[j]):
                return False
    return True
        
        

print(oneEditAway("sales", "saes"))
