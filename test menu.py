from simple_term_menu import TerminalMenu

def option_menu():
    options = ["Name", "Author", "Genre"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"Searching for books using '{options[menu_entry_index]}'")

if __name__ == "__main__":
    option_menu()