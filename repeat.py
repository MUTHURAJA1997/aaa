chars = "abcdefghijklmnopqrstuvwxyz"
string = str(input("enter the sentence or word:"))

for cha in chars:
  count = string.count(cha)
  if (count > 1):
    print (cha,("is repeated") ,count ,("times"))
