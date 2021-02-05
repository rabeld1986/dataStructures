"""A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on."""

class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S+" "
        sentence = []
        word = ""
        
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        
        for ch in S:
            if ch.isalpha():
                word += ch
            elif ch == " ":
                sentence.append(word)
                word = ""
                
        ind = 0        
        for i in range(len(sentence)):
            ind +=1
            if sentence[i][0] in vowels:
                extra = ind*"a"
                sentence[i] = sentence[i] +"ma"+extra
            elif sentence[i][0] in consonants:
                extra = ind*"a"
                ch = sentence[i][0]
                sentence[i] = sentence[i][1:len(sentence[i])]
                sentence[i] = sentence[i]+ch +"ma"+extra
        return " ".join(sentence)
