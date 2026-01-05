import json
import os


def get_user_info():
   return {
  "Name":input("Enter your name: "), 
  "phone":input("Enter your phone: "),
  "email":input("Enter your email: "),
  "address":input("Enter your address: "),
  "category":input("Enter your category: ")
}



def append():
  with open("demofile.json", "r") as f:
       data_list =json.load(f)

  new_person= get_user_info()
  data_list.append(new_person)

  with open("demofile.json", "w") as f:
      f.write(json.dumps(data_list, indent=4))

  

def View_contects():
 with open("demofile.json", "r") as f:  
   print(f.read())

print("add contect: append()")
print("view contects: View_contects()")
print("search contect: search_contect()")
print("delete contect: delete_contect()")


def search_contect():
   name=input("Enter the name to search in your contect list: ")
   with open("demofile.json","r")as f:
       data_list =json.load(f)
       for person in data_list:
           if person["Name"]==name:
              print(person)
              break
       else:
        print("contect not found")


def delete_contect():
    name=input("Enter the name to search in your contect list: ")
    with open("demofile.json","r")as f:
       data_list =json.load(f)
    for person in data_list:
             if person["Name"]==name:
               data_list.remove(person)    
               break  
    with open("demofile.json","w")as f:
       f.write(json.dumps(data_list, indent=4))
       
       print("contect deleted successfully")
       return

    print("contect not found")        
