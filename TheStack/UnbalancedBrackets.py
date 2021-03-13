from StackImportant import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):  # we assign the Stack method to the variable "s"
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced: # we itterate over paren_string index and push if we have an opening bracket
        paren = paren_string[index]       # we assign the current index to the variable paren
        if paren in "([{":
            s.push(paren)              # we push the open bracket in the stack
        else:
            if s.is_empty():                        # If no opening brackets are found we break out of the loop 
                is_balanced = False
                break
            else: 
                top = s.pop()                            # we assign the last item popped to variable TOP
                if not is_match(top, paren):              # we compare the last item Popped to the current item in our index and set balance to false if it matches then break out of the program
                    is_balanced = False                  
                    break
        index += 1                        # increment the index
 
  # we check if our condition are true in order to return TRUE / FALSE
    if s.is_empty() and is_balanced:         
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))