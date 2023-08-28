# Implement a function to find the longest common prefix string amongst list of strings, return an empty string "" if not found.

def lcp(string):

    string.sort()

    first_string = string[0]

    last_string = string[-1]

    common_prefix = ""

    for i in range(min(len(first_string), len(last_string))):

        if first_string[i] == last_string[i]:

            common_prefix += first_string[i]

        else:

            break

    return common_prefix

string_list = ["light","live","liver"]   #["light","racecar","car"]

result = lcp(string_list)

print("The longest common prefix is :", result)