from StackImportant import Stack

def convert_int_to_bin(dec_num):
    
    if dec_num == 0:
        return 0
    
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num


print(convert_int_to_bin(700))
print(int(convert_int_to_bin(56),2)==56) # Test the code