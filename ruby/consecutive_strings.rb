# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# Example:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
# Note:
# consecutive strings : follow one after another without an interruption

# naive solution
def longest_consec(strarr, k)
  if strarr.length == 0 || k > strarr.length || k <= 0
    return ''
  end
  longest = ''
  strarr.each_cons(k) do |a|
    total_length = a.map { |string| string.length }.sum
    if total_length > longest.length
      longest = a.join('')
    end
  end
  longest
end
