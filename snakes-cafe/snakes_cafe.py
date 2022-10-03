Appetizers = ["Wings","Cookies","Spring Rolls"]
Entrees =["Salmon","Steak","Meat Tornado","A Literal Garden"]
Desserts = ["Ice Cream","Cake","Pie"]
Drinks =["Coffee","Tea","Unicorn Tears"]
menu =["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears" ]
print("**************************************")

print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**                                  **")
print("** To quit ay any time, type \"quit\" **")

print("**************************************")
print("Appetizers\n---------")
for x in Appetizers:
  print(x)
print("\n")
print("Entrees\n-------")
for x in Entrees:
  print(x)
print("\n")
print("Desserts\n-------")
for x in Desserts:
  print(x)
print("\n")
print("------")
for x in Drinks:
  print(x)
print("\n")
print("***********************************")
print("** What would you like to order? **")
print("***********************************")
keyword= "quit"
num=0
yourorder=[]
while True :
 
 order = input("> ")
 
 if order == keyword :
    break
 if order in menu : 
    num+=1
    yourorder.append(order)
    print(f"** {num} order of {order} have been added to your meal **")
 else : 
    print("**           item is not on the menu           **")

print(f"your order is {yourorder}")
 

    
     