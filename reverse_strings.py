# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"


# *** your code here ***

def string_reverse(sentence):
    my_arr = sentence.split(" ")
    for i in range(0, len(my_arr)):
        word_len = len(my_arr[i])
        my_arr[i] = my_arr[i][word_len: 0: -1] + my_arr[i][0]
    new_sentence = " "
    return new_sentence.join(my_arr)

print(string_reverse("flip this shit"))