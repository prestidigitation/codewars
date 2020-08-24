# Write a function that takes an array and counts the number of each unique element present.
# count(['james', 'james', 'john'])
# #=> { 'james' => 2, 'john' => 1}


# naive solution
def count(array):
    hash = {}
    for item in array:
        if item in hash:
            hash[item] = hash[item] + 1
        else:
            hash[item] = 1
    return hash
