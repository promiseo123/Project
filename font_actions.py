"""This is a Python program that comprises of functions for displaying valid HTML font styles to a user and setting the
font style chosen by the user. Author: Promise Omiponle"""

import turtle

def see_fonts(show_fonts):
    """
    see_fonts takes the users input for displaying the fonts and opens a turtle window
    to write out the different font styles in their respective fonts if the user input yes
    or hit the enter key, otherwise if no is entered, nothing is done, but if anything other
    than these is input, the user is recursively prompted again until either of them is entered.

    pre-conditions: show_fonts=yes, no or the empty string.
    """
    if (show_fonts == "yes") or (show_fonts==""):
        print("Close the window when you have made your choice.")
        turtle.title("Font Options")
        turtle.up()
        turtle.goto(-375, 300)
        turtle.down()
        turtle.write("Arial", False, "left", ("Arial", 14, "normal"))
        turtle.up()
        turtle.right(90)
        turtle.fd(28)
        turtle.left(90)
        turtle.write("Comic Sans MS", False, "left", ("Comic Sans MS", 14, "normal"))
        turtle.up()
        turtle.right(90)
        turtle.fd(28)
        turtle.left(90)
        turtle.write("Lucida Grande", False, "left", ("Lucida Grande", 14, "normal"))
        turtle.up()
        turtle.right(90)
        turtle.fd(28)
        turtle.left(90)
        turtle.write("Tahoma", False, "left", ("Tahoma", 14, "normal"))
        turtle.up()
        turtle.right(90)
        turtle.fd(28)
        turtle.left(90)
        turtle.write("Verdana", False, "left", ("Verdana", 14, "normal"))
        turtle.right(90)
        turtle.fd(28)
        turtle.left(90)
        turtle.write("Helvetica", False, "left", ("Helvetica", 14, "normal"))
        turtle.up()
        turtle.right(90)
        turtle.fd(28)
        turtle.left(90)
        turtle.write("Times New Roman", False, "left", ("Times New Roman", 14, "normal"))
    elif show_fonts != "no":
        print("Invalid response.")
        show_fonts = input("Do you want to see what the fonts look like? [yes]")
        see_fonts(show_fonts)

def set_font(font):
    """set_font checks the font integer input by the user from a displayed list and sets the font
    variable according to the list. If the input is invalid, the user is recursively prompted
    until a valid integer is selected.

    pre-conditions: font in range(7)
    """
    if font == 0:
        font = "Arial"
        return font
    elif font == 1:
        font = "Comic Sans MS"
        return font
    elif font == 2:
        font = "Lucida Grande"
        return font
    elif font == 3:
        font = "Tahoma"
        return font
    elif font == 4:
        font = "Verdana"
        return font
    elif font == 5:
        font = "Helvetica"
        return font
    elif font == 6:
        font = "Times New Roman"
        return font
    else:
        print("Invalid font selection.")
        font = int(input("Choose a font by its number."
                         "0: Arial, size 14"
                         "1: Comic Sans MS, size 14"
                         "2: Lucida Grande, size 14"
                         "3: Tahoma, size 14"
                         "4: Verdana, size 14"
                         "5: Helvetica, size 14"
                         "6: Times New Roman, size 14"))
        return set_font(font)