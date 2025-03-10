word = input("enter a word")
ren= "_"*len(word)
print(ren)
chances=0
no_of_mist=9

for i in word:
    letter=input("enter a letter")
    if letter in word:
           result=ren[:i]+letter+ren[i+1:]
           print(result)





