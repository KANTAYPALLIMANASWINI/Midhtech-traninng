# for loop with numbers
# print("for loop with in range");
# for i in range(1, 6):
   # print(i);

 #for loop with list
# students=["manaswini","sai","sindhu", "sowmya"];
# for name in students:
#     print("\n" + name); # sepeerator ichinapudu + vundalii

#while loop

#seconds=6;
# while seconds>0: higher to lower
#     print(seconds);
#     seconds=seconds-1;



# # break and continue
# for  i in range(1,9):
#     if(i==3):
#         break;
#     print(i);

#and continue
# fi



####while loop food items
# count = 1

# while True:
#     food = input("Enter food or (q to quit): ")

#     if food == "q":
#         break

#     print(count, food)
#     count += 1

food = input("Enter your food item (Press 'q' to quit): ")

while food != "q":
    print(f"You like {food}")
    food = input("Enter another food item (Press 'q' to quit): ")

print("Thank you!")

num = int(input("Rate the food between 1 and 10: "))

while num < 1 or num > 10:
    print("Invalid rating")
    num = int(input("Please enter a rating between 1 and 10: "))

print("Your rating is:", num)