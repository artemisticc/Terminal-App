import sys
from termcolor import colored, cprint


# question = colored('Input here: ', 'magenta', attrs=['bold'])
# # print(text)
# cprint('This is an error', 'red', attrs=['bold'])

# # print_red_on_cyan = lambda x: cprint(x, 'red', attrs=['bold'])
# # print_red_on_cyan('Hello, World!')
# # print_red_on_cyan('Hello, Universe!')

# # for i in range(10):
# #     cprint(i, 'magenta', end=' ')

# # cprint("Attention!", 'blue', attrs=['bold', 'blink'], file=sys.stderr)

# # error_message = lambda x: cprint(x, 'red', attrs=['bold'])
# # error_message("This is an error")

# input(text)

# def remove_entry():
#     question = colored("What is the title of the book you want to remove? ", 'blue')
#     print(question)

# def _give_color(user_input, color):
#     colored_message = colored(user_input, color)
#     input(colored_message)

# cprint('This is an error', 'red', attrs=['bold'])
def edit_entry(operation1, operation2):
    n = _search_title()
        if n > 1:
            input("Using the numbers on the left, which book would you like to " + operation1 + "from the system? ")
        elif n == 1:
            input("Do you want to permanently remove this book from the system?")
        else:
            print("Nothing to remove.")

edit_entry()