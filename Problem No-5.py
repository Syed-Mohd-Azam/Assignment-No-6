# Write a python script to print two given words in dictionary order.
print("Enter two words: ")
a,b= input(),input()
print("the dictionary order of given words are: ")
print(b,a,sep="\n") if a>b else print(a,b,sep='\n')
print()