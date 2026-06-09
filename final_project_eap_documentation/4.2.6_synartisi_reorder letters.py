def reverseWord(word):
    return word[::-1]

myList = ['ishoJ keetarP yb nohtyP htiw ecnegilletnI laicifitrA' ]

newList = [reverseWord(word) for word in myList]

print(newList)