def reverse(nums):
    data = list(nums)
    start = 0;
    end = len(data) - 1;
    newarr = [];


    while end > start :
        data[start], data[end] = data[end], data[start];
        start = start + 1;
        end = end - 1;
    return ''.join(data);
    
def palindrome(s):
    
    reverse_string = reverse(s)
    
    if reverse_string == s:
        return True
    else:
        return False;


if __name__ == "__main__":
    string = "radar";
    print(palindrome(string));
    
    # print()
    
    # reverse(n)
    # print(n);