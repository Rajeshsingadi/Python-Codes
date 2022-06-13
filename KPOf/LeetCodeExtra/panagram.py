import string
def checkIfPangram(sentence: str) -> str:
    alphabet = string.ascii_lowercase
    return "".join(sorted(set(alphabet) - set(sentence)))
sentence = "The quic brown for jumps over the lazy dog"
print(checkIfPangram(sentence))

'''
https://leetcode.com/discuss/interview-question/2066940/Goldman-Sachs-or-Check-if-the-Sentence-Is-Pangram-and-return-the-missing-letters
'''