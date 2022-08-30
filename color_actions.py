"""This is a Python program that defines a set of valid HTML colors and comprises functions for setting correct color
inputs to be used in html_builder. Author: Promise Omiponle"""

colornames={'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen', 'lawngreen',
        'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen', 'chocolate',
        'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat', 'mediumvioletred', 'bisque',
        'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred ', 'antiquewhite', 'royalblue', 'yellow', 'indigo ',
        'lightcoral', 'darkslategrey', 'sienna', 'lightslategray', 'mediumblue', 'red', 'khaki', 'darkviolet',
        'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise', 'lightyellow', 'grey', 'whitesmoke', 'blueviolet',
        'orchid', 'mediumslateblue', 'darkturquoise', 'coral', 'forestgreen', 'gainsboro', 'darkorange',
        'cornflowerblue', 'lightsteelblue', 'plum', 'lavender', 'palegreen', 'darkred', 'dimgray', 'floralwhite',
        'orangered', 'oldlace', 'darksalmon', 'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver', 'tomato',
        'darkkhaki', 'slategray', 'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson', 'mistyrose', 'lime',
        'saddlebrown', 'blanchedalmond', 'black', 'snow', 'seashell', 'darkcyan', 'gold', 'midnightblue',
        'darkgoldenrod', 'palevioletred', 'fuchsia', 'teal', 'lightpink', 'darkgrey', 'mediumspringgreen', 'aquamarine',
        'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood', 'rosybrown', 'springgreen', 'purple', 'olivedrab',
        'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine', 'navy', 'salmon', 'rebeccapurple', 'darkmagenta',
        'limegreen', 'deepskyblue', 'pink', 'mediumpurple', 'skyblue', 'aqua', 'blue', 'slategrey', 'darkslateblue',
        'honeydew', 'darkseagreen', 'paleturquoise', 'brown', 'thistle', 'lemonchiffon', 'peru', 'cornsilk',
        'papayawhip', 'green', 'lightgoldenrodyellow', 'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey',
        'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite', 'dodgerblue', 'greenyellow', 'dimgrey',
        'darkorchid'}

def set_background_color(background_color):
    """
    set_background_color recursively checks if the user input background_color is valid.
    If it isn't, the user is continuously prompted until a valid color is input.

    return: background_color
    """
    if ((background_color[0]=="#") and ((i==("a" or "b" or "c" or "d" or "e" or "f")) or
                        (int(i)==(n for n in range(10))) for i in background_color)) or \
            (background_color in colornames):
        return background_color
    else:
        print("Invalid color choice.")
        background_color=input("Choose the name of a color, or in format 'XXXXXX': ")
        set_background_color(background_color)

def set_paragraph_color(paragraph_color):
    """
    set_paragraph_color recursively checks if the user input paragraph_color is valid.
    If it isn't, the user is continuously prompted until a valid color is input.

    return: paragraph_color
    """
    if ((paragraph_color[0]=="#") and ((chr(i)==("a" or "b" or "c" or "d" or "e" or "f")) or
                        (int(i)==(n for n in range(10))) for i in paragraph_color)) or \
            (paragraph_color in colornames):
        return paragraph_color
    else:
        print("Invalid color choice.")
        paragraph_color=input("Choose the name of a color, or in format 'XXXXXX': ")
        set_paragraph_color(paragraph_color)

def set_heading_color(heading_color):
    """
    set_heading_color recursively checks if the user input heading_color is valid.
    If it isn't, the user is continuously prompted until a valid color is input.

    return: heading_color
    """
    if ((heading_color[0]=="#") and ((chr(i)==("a" or "b" or "c" or "d" or "e" or "f")) or
                        (int(i)==(n for n in range(10))) for i in heading_color)) or \
            (heading_color in colornames):
        return heading_color
    else:
        print("Invalid color choice.")
        heading_color=input("Choose the name of a color, or in format 'XXXXXX': ")
        set_heading_color(heading_color)