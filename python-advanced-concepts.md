################## Notes for each topic ##################
## Topic-1 : EasyDict

reference : https://github.com/makinacorpus/easydict

* when using dictionary it becomes difficult to use keys and values with brackets
* To make it simplified , lets access each key or value with attributes (like a variable)
* ```  
  >>> from easydict import EasyDict as edict
  >>> d = edict({'foo':3, 'bar':{'x':1, 'y':2}})
  >>> d.foo
  3
  >>> d.bar.x
  1

  >>> d = edict(foo=3)
  >>> d.foo
  3

* Now access easily like -> d.foo  or d.bar.x

Real worl usage : https://github.com/SimonVandenhende/Multi-Task-Learning-PyTorch/blob/e2bcb2ebb72c29ea424b8b251d733a8cddef2214/utils/config.py#L16


## Topic-2 : List Comprehensions

### Doing all processing inside the brackets 
* Basic for loop
* ```  
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
  newlist = []

  for x in fruits:
    if "a" in x:
      newlist.append(x)

  print(newlist) # ['apple', 'banana', 'mango']
  
* ```  
  >>> l = [2, 4, 6, 8, 10, 12]
  >>> [int(i / 2) for i in l]
  [1, 2, 3, 4, 5, 6]
* process logic inside block



