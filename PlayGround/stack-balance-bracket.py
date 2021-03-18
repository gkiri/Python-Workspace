
class Stack: 
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
        return data 
    
    def pop(self): 
        return self.elements.pop() 
        
    def peek(self): 
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0

def BracketMatcher(strParam):
  stack = Stack()
  #print("init empty ? =",stack.is_empty())
  #if len(strParam)==1 and (strParam == "(" or strParam == ")"):
  #  return 0

  for ch in strParam:
    if ch == '(':
      #print("if case")
      stack.push(ch)
    elif stack.is_empty()==False and ch ==')':
      #print("else case ")
      stack.pop()
    elif ch==')':
      #print("default")

      stack.push(ch)


  if stack.is_empty():
    return 1
  else:
    return 0



# keep this function call here 
print(BracketMatcher(input()))
