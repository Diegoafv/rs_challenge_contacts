def new_contact(contacts):
  name = input("\nName: ")
  phone = input("Phone number: ")
  email = input("Email: ")
  contact = {"name": name, "phone_number": phone, "email": email, "favorite": False}
  contacts.append(contact)
  print("\nNew contact added successfully!")
  return

def show_contacts(contacts):
  index = 1
  for contact in contacts:
    print(f"\n{index} - {contact['name']}")
    print(f"Phone: {contact['phone_number']}")
    print(f"Email: {contact['email']}")
    index+=1

  if index == 1:
    print("Your contacts list is empty.")
  return

def edit_contact(contacts):
  if len(contacts):
    index = int(input("\nWhich contact do you want to edit? "))
    change = input("\nEdit the name? (y/n) ")

    if change == "y":
      contacts[index-1]["name"] = input("Type the new name: ")

    change = input("\nEdit the phone number? (y/n) ")

    if change == "y":
      contacts[index-1]["phone_number"] = input("Type the new phone number: ")

    change = input("\nEdit the email? (y/n) ")

    if change == "y":
      contacts[index-1]["email"] = input("Type the new email: ")

    print("\nThe contact was successfully updated!")
  else:
    print("Try adding a new contact before editing.")
  return

def add_to_favorites(contacts):
  if len(contacts):
    index = int(input("\nWhich contact will be added to favorites? "))
    contacts[index-1]["favorite"] = True

    print("The contact was successfully added to your favorites list!")
  else:
    print("Try adding a new contact before using the favorites function.")

  return

def show_favorites(contacts):
  empty = True
  for contact in contacts:
    if contact["favorite"]:
      print(f"\n{contact['name']}")
      print(f"Phone: {contact['phone_number']}")
      print(f"Email: {contact['email']}")
      empty = False

  if empty:
    print("Your favorites list is empty.")
  return

def delete_contact(contacts):
  if len(contacts):
    index = int(input("\nWhich contact do you want to delete? "))
    contacts.pop(index-1)
    print("The contact was successfully deleted!")
  else:
    print("Try adding a new contact before using the delete function.")
  return

contacts = []

choice = 0
while choice != "7":
  print("\nMenu:")
  print("1. Add new contact")
  print("2. Show contacts list")
  print("3. Edit contact")
  print("4. Add contact to favorites")
  print("5. Show favorite contacts")
  print("6. Delete a contact")
  print("7. Exit")

  choice = input("Choose an option: ")

  if choice == "1":
    new_contact(contacts)
  elif choice == "2":
    show_contacts(contacts)
  elif choice == "3":
    show_contacts(contacts)
    edit_contact(contacts)
  elif choice == "4":
    show_contacts(contacts)
    add_to_favorites(contacts)
  elif choice == "5":
    show_favorites(contacts)
  elif choice == "6":
    show_contacts(contacts)
    delete_contact(contacts)
