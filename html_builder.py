"""This is a Python program that builds a very simple web page from text input by a user.
Author: Promise Omiponle"""

from cs_queue import *
import sys
from font_actions import *
from color_actions import *
from dataclasses import dataclass

@dataclass
class Paragraph:
    """
    A Paragraph structure is used to represent a paragraph
    to be included in the HTML file. A paragraph comprises a
    title, content as in the body of the paragraph, and images
    to be included.
    """
    title: str
    content: str
    images: Queue

def images_add(add_images, image_queue=make_empty_queue()):
    """
    images_add takes the users response for adding images and prompts the user
    for image file names and whether to add more images, prompting for file names
    each time the user chooses to add more, adding each image file name to an image_queue.

    If the user inputs anything other than yes, no or the empty string, the user is
    prompted again until either of those is input.

    pre-conditions: add_images=yes, no, or the empty string.
    post-conditions: image_queue is returned
    """
    if (add_images == "yes") or (add_images==""):
        image_filename = input("Image file name: ")
        enqueue(image_queue, image_filename)
        add_other_image = input("Do you want to add another image? [yes]")
        if (add_other_image=="yes") or (add_other_image==""):
            images_add(add_other_image, image_queue)
        elif add_other_image!="no":
            print("Invalid answer.")
            add_other_image = input("Do you want to add images? [yes]")
            images_add(add_other_image, image_queue)
    elif add_images!="no":
        print("Invalid answer.")
        add_images=input("Do you want to add images? [yes]")
        images_add(add_images)
    return image_queue

def paragraphs_add(add_paragraph, paragraph_queue=make_empty_queue()):
    """
    paragraphs_add recursively takes the users response for adding a paragraph and
    prompts the user for the title, content, whether to add images or not, adding
    each image file name to an image_queue and adding all these to a paragraph
    instance. The user is also prompted to add images or not, calling images_add,
    and whether to add more paragraphs, adding each paragraph instance to.

    If the user inputs anything other than yes, no or the empty string, the user is
    prompted again until either of those is input.

    pre-conditions: add_paragraph=yes, no, or the empty string.
    post-conditions: paragraph_queue is returned
    """
    if (add_paragraph=="yes") or (add_paragraph==""):
        title=input("Title of your paragraph: ")
        content=input("Content of your paragraph: ")
        add_images=input("Do you want to add images? [yes] ")
        paragraph=Paragraph(title, content, images_add(add_images))
        enqueue(paragraph_queue, paragraph)
        add_another=input("Do you want to add another paragraph to your website? [yes] ")
        if (add_another=="yes") or (add_another==""):
            paragraphs_add(add_another, paragraph_queue)
        elif add_another=="no":
            return None
        else:
            print("Invalid response.")
            add_another = input("Do you want to add another paragraph to your website? [yes] ")
            return paragraphs_add(add_another, paragraph_queue)
        return paragraph_queue
    elif add_paragraph=="no":
        return None
    else:
        print("Invalid response.")
        add_paragraph=input("Do you want to add another paragraph to your website? [yes] ")
        return paragraphs_add(add_paragraph, paragraph_queue)

def insert_style(w):
    """
    insert_style reads each line in the file style_template.txt in the same
    directory as this program and prints them into the file w while replacing
    certain string instances with their corresponding user input.
    """
    with open("style_template.txt", "r") as s:
        for line in s:
            content = str(line.strip())
            if "@BACKCOLOR" in content:
                print(content.replace("@BACKCOLOR", background_color), file=w)
            elif "@HEADCOLOR" in content:
                print(content.replace("@HEADCOLOR", heading_color), file=w)
            elif "@FONTCOLOR" in content:
                print(content.replace("@FONTCOLOR", paragraph_color), file=w)
            elif "@FONTSTYLE" in content:
                print(content.replace("@FONTSTYLE", font), file=w)
            else:
                print(content, file=w)

if __name__ == '__main__':
    """
    main prompts the user for input for all elements to be used in building a website 
    if the command line is empty, otherwise it prompts for the background color, heading color,
    paragraph color, and font style only. It then builds the website either from all the input 
    or from just these four inputs plus the script that is a text file on the command line.
    post-conditions: website(s) built.
    """
    if len(sys.argv)==1:
        website_title = input("What is the title of your website? ")
    print("Background Color")
    background_color = input("Choose the name of a color, or in format 'XXXXXX': ").lower()
    set_background_color(background_color)
    print("You will now choose a font.")
    show_fonts = input("Do you want to see what the fonts look like? [yes]")
    see_fonts(show_fonts)
    print("Choose a font by its number.")
    print("0: Arial, size 14")
    print("1: Comic Sans MS, size 14")
    print("2: Lucida Grande, size 14")
    print("3: Tahoma, size 14")
    print("4: Verdana, size 14")
    print("5: Helvetica, size 14")
    print("6: Times New Roman, size 14")
    font = int(input())
    font = set_font(font)
    print("Paragraph Text Color")
    paragraph_color = input("Choose the name of a color, or in format 'XXXXXX': ").lower()
    set_paragraph_color(paragraph_color)
    print("Heading Color")
    heading_color = input("Choose the name of a color, or in format 'XXXXXX': ").lower()
    set_heading_color(heading_color)
    if len(sys.argv) == 1:
        paragraph_title = input("Title of your paragraph: ")
        print("Content of your paragraph (single line)")
        paragraph_content = input()
        add_images = input("Do you want to add images? [yes]")
        add_paragraph = input("Do you want to add another paragraph to your website? [yes] ")
        with open("index.html", "w") as w:
            print("<!DOCTYPE html>", file=w)
            print("<html>", file=w)
            print("<head>", file=w)
            print("<title>"+website_title+"</title>", file=w)
            insert_style(w)
            print("</head>", file=w)
            print("<body>", file=w)
            print("<h1>"+website_title+"</h1>", file=w)
            print("", file=w)
            print("<hr/>", file=w)
            print("<h2>"+paragraph_title+"</h2>", file=w)
            print("<p>"+paragraph_content+"</p>", file=w)
            images=images_add(add_images)
            while images.size!=0:
                print('<img ' + 'src="' + front(images)+'" class="center">', file=w)
                dequeue(images)
            paragraphs = paragraphs_add(add_paragraph)
            while paragraphs.size!=0:
                print("<h2>"+front(paragraphs).title+"</h2>", file=w)
                print("<p>"+front(paragraphs).content+"</p>", file=w)
                images=front(paragraphs).images
                while images.size!=0:
                    print('<img '+'src="'+front(images)+'" class="center">', file=w)
                    dequeue(images)
                dequeue(paragraphs)
            print("</body>", file=w)
            print("</html>", file=w)
    else:
        for i in range(1,len(sys.argv)):
            with open("index"+str(i)+".html", "w") as w:
                print("<!DOCTYPE html>", file=w)
                print("<html>", file=w)
                print("<head>", file=w)
                file=open(sys.argv[i])
                for line in file:
                    content=line.strip().split()
                    if len(content)==0:
                        print("", file=w)
                    elif (len(content)==1) and (content[0][0]!="!"):
                        print("<title>"+content[0]+"</title>", file=w)
                        insert_style(w)
                        print("</head>", file=w)
                        print("<body>", file=w)
                        print("", file=w)
                        print("<h1>"+content[0]+"</h1>", file=w)
                        print("<hr/>", file=w)
                        if len(sys.argv)!=2:
                            print('<p align="center">', file=w)
                            for i in range(1,len(sys.argv)):
                                file=open(sys.argv[i])
                                for line in file:
                                    content=line.strip().split()
                                    if (len(content)==1) and (content[0][0]!="!"):
                                        w.write('<a href="index'+str(i)+'.html">'+content[0]+'</a>---')
                                    else:
                                        break
                                file.close()
                            print("</p>", file=w)
                    elif content[0]=="!new_paragraph":
                        continue
                    elif content[0]=="!title":
                        print("<h2>", file=w)
                        for word in content[1:]:
                            w.write(word+" ")
                        print("</h2>", file=w)
                        print("<p>", file=w)
                    elif content[0] == "!image":
                        print("</p>", file=w)
                        if (len(content)==3) and (content[2][-1] == "%"):
                            print('<img src="' + content[1] + '" width=' + str(content[2]) + ' class="center">', file=w)
                        else:
                            print('<img src="' + content[1] + '" class="center">', file=w)
                    elif (len(content)!=0) and(content[0][0]!="!"):
                        for word in content:
                            w.write(word+" ")
                    else:
                        print("", file=w)
                file.close()