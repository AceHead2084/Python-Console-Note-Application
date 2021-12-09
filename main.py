from replit import db

print("Type '/add' to add a note.")
print("Type '/notes' to see notes.")
print("Type '/remove' to remove a note.")

while True:
  userinput = input()
  option1 = "/add"
  option2 = "/notes"
  option3 = "/remove"



  if userinput == option1:
    userinput1 = input("Add note: ")
    db[userinput1] = userinput1

  if userinput == option2:
    keys = db.keys()
    separator = ", "

    if keys:
     print(separator.join(keys))

    if not keys:
      print("Notes are empty")

  if userinput == option3:
    userinput2 = input("Type note to delete: ")
    del db[userinput2]