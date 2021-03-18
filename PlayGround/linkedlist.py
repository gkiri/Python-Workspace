# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class List :

    def __init__(self):
        self.head=None
        print(" constructor")
        
    def append(self,val):
        if self.head==None:
            temp=Node(val)
            self.head=temp
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            
            temp.next=Node(val)
                
       
    def delete(self,val):
        temp=self.head
        prev=None
        if self.head.val == val:
             self.head=self.head.next

        while temp.next!=None :
            if temp.val==val:
                if prev!=None:
                    prev.next=temp.next  
                    return 1
                else:
                    self.head=temp.next
                    return 1
            #inc loop
            temp=temp.next
        
        return -1
    
    def print_list(self):
        temp=self.head
        while temp!=None:
            print(temp.val)
            temp=temp.next
            print("\n")

if __name__== "__main__":
    print("inside main")
    obj = List()
    obj.append(5)
    obj.append(8)

    obj.print_list()
    ret=obj.delete(5)
    print("new list")
    obj.print_list()
    print("del= ",obj.delete(8))
    print("new list")
    obj.print_list()   
    
    obj.append(10)
    print("new list")
    obj.print_list()   
    
    

