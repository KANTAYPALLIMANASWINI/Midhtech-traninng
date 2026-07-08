word="python programming"  
word1="java"  
print("Basic example index:",word[0]);  #indexing
print("Basic example index:",word[3]);
print("concatenation:",word+word1) #concatenation
print("repetition:",word*4)   #repitition
print(word[1:3]); #slicing
print(len(word1)); #length;
print("Membership:","py" in word) #Membershhip
print("uppercase:" ,word.upper())  #upper case
print("Lowercase: " ,word.lower()) #lower case
 

 #replace 
new_name=word.replace("py","PY")
print("Replace result: ",new_name)

print("original string still:",word)

print(word.strip())
splitword="manaswini,teju";
print(splitword.split("*"));
print(word.count("a"));
print(word.find("py"));
print(word.startswith("python"));
print(word.endswith("programming"));





