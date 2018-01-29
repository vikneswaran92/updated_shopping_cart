import os

shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    clear_screen()
    print("""
Enter 'DONE' to stop adding items into list
Enter 'SHOW' to show items in cart
Enter 'HELP' for options
Enter 'REMOVE' for remove items in list
What we shoul add in our cart
""")



def list_arrange(item):
    added_to_list()
    if len(shopping_list):
        position = input("Where should we add the {} item?\n"
                         "Press ENTER to add to the end of the list\n"
                         "-> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))

    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)
        
    added_to_list()

def added_to_list():
    clear_screen()

    print("Here is your list:")

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

    print("-" * 10)

def remove_list():
    print("Please enter the name of the item that you would like to remove")
    delete = input("-> ")
    shopping_list.remove(delete)
    added_to_list()
show_help()

while True:
      new_item = input("-> ")

      if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
          break
      elif new_item.upper() == 'HELP':
          show_help()
          continue
      elif new_item.upper() == 'SHOW':
          added_to_list()
          continue
      elif new_item.upper() == 'REMOVE':
          remove_list()
          continue
      else:
          list_arrange(new_item)
          
added_to_list()
