This is where info on how to use this is gonna go.

## Installation
1. You will need python.
2. https://github.com/artemisticc/Terminal-App


## Dependencies
simple_term_menu
term_color
tabulate
art
pandas
colorama

## System/Hardware requirements

## User guide/Features:

This application was made with the intention of using it as an inventory handler (or catalogue) for a 
The features of this app include:
1. **Selectable menus** - you can navigate to what you would like to do by using the up & down arrows on your keyboard. Pressing enter confirms your selection. You can exit menus (or the program, if in the main menu) by either pressing escape or selecting Exit.
2. **Display books in catalogue** - selecting the catalogue list displays all the entries within the catalogue in a neat table. An empty table will be displayed if there are no entries.
3. **Search for entry** - selecting to search the catalogue gives you the option to search by Title or Author. You can type in the title or author of an entry and the app will search for it within the catalogue and display any matching results if they are found. Please note: the search function is case sensitive. 
4. **Add books to catalogue** - selecting "Create entry" allows you to add books into the catalogue. You can define how many books you would like to create and then type in the information. The price and the stock count must be numbers, but only the price may include decimal points. Blank entries are not accepted.
5. **Remove books from catalogue** - selecting "Remove entry" displays the catalogue and allows you to remove an entry from the catalogue by typing in its corresponding number. Selecting a number that does not exist will result in an error and the app will ask again. Leaving the entry selection input blank will return you to the main menu.
6. **Modify entries in catalogue** - selecting to modify the entries displays the catalogue and allows you to modify an entry of your choice. After typing in the corresponding number of the entry you would like to modify, you may select what information to edit. These modifcations follow the same rules as creating an entry. Leaving the entry selection input blank will return you to the main menu.

## Implementation plan

I decideed to use Trello for keeping track of the development of my app. Due to reasons outlined in my support plan, I was unable to adhere to most deadlines, but my features were still created and implemented according to this implementation plan.

All testing for this program was done manually, by copying thee chunks of code I was testing to another file and testing it from there. When it was working in the test file, I would move it to the main file