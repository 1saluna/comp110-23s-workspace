"""Practice with lists."""

grocery_list: list[str] = list()
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("break")
grocery_list.append("bananas")
grocery_list[1] = "ceral"
grocery_list.pop(2)
print(grocery_list)