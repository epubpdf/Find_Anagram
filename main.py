# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    list1 = len(word)
    list2 = len(anagram)
    count = 0

    if list1 == list2:
        for i in word:
            for j in anagram:
                if i == j:
                    count += 1
                    word.replace(i,'',1)
                    anagram.replace(j,'',1)
                    break
    if count == list1:
        return True
    return False

print(find_anagram("word", "anagram"))
