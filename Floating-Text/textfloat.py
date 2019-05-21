#import os
import time

width =70

text = input("Enter the text: ").upper()

printedtext = [ "","","","","" ]

characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "A" : [ "  *  ",
                       " * * ",
                       "*   *",
                       "*****",
                       "*   *" ],

               "B" : [ "**** ",
                       "*   *",
                       "**** ",
                       "*   *",
                       "**** " ],

               "C" : [ " ****",
                       "*    ",
                       "*    ",
                       "*    ",
                       " ****" ],

               "D" : [ "**** ",
                       "*   *",
                       "*   *",
                       "*   *",
                       "**** " ],

               "E" : [ "*****",
                       "*    ",
                       "*****",
                       "*    ",
                       "*****" ],

               "F" : [ "*****",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    " ],

               "G" : [ " ****",
                       "*    ",
                       "* ***",
                       "*   *",
                       " ****" ],

               "H" : [ "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *" ],

               "I" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "*****" ],

               "J" : [ "*****",
                       "   * ",
                       "   * ",
                       "*  * ",
                       "**** " ],

               "K" : [ "*   *",
                       "*  * ",
                       "***  ",
                       "*  * ",
                       "*   *"  ],

               "L" : [ "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "M" : [ "*   *",
                       "** **",
                       "* * *",
                       "*   *",
                       "*   *" ],

               "N" : [ "*   *",
                       "**  *",
                       "* * *",
                       "*  **",
                       "*   *" ],

               "O" : [ " *** ",
                       "*   *",
                       "*   *",
                       "*   *",
                       " *** " ],

               "P" : [ "**** ",
                       "*   *",
                       "**** ",
                       "*    ",
                       "*    " ],

               "Q" : [ " *** ",
                       "**  *",
                       "* * *",
                       " *** ",
                       "   * " ],

               "R" : [ "**** ",
                       "*   *",
                       "**** ",
                       "*  * ",
                       "*   *"  ],

               "S" : [ " ****",
                       "*    ",
                       " *** ",
                       "    *",
                       "**** " ],

               "T" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],

               "U" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       " *** " ],

               "V" : [ "*   *",
                       "*   *",
                       "*   *",
                       " * * ",
                       "  *  " ],

               "W" : [ "*   *",
                       "*   *",
                       "* * *",
                       "** **",
                       "*   *" ],

               "X" : [ "*   *",
                       " * * ",
                       "  *  ",
                       " * * ",
                       "*   *" ],

               "Y" : [ "*   *",
                       "*   *",
                       " * * ",
                       "  *  ",
                       "  *  " ],

               "Z" : [ "*****",
                       "   * ",
                       "  *  ",
                       " *   ",
                       "*****" ],

               "1" : [ " **  ",
                       "* *  ",
                       "  *  ",
                       "  *  ",
                       "*****" ],

               "2" : [ "*****",
                       "    *",
                       "*****",
                       "*    ",
                       "*****"  ],

               "3" : [ "*****",
                       "    *",
                       " ****",
                       "    *",
                       "*****" ],

               "4" : [ "*   *",
                       "*   *",
                       "*****",
                       "    *",
                       "    *" ],

               "5" : [ "*****",
                       "*    ",
                       "*****",
                       "    *",
                       "*****" ],

               "6" : [ "*****",
                       "*    ",
                       "*****",
                       "*   *",
                       "*****" ],

               "7" : [ "*****",
                       "   * ",
                       "  *  ",
                       " *   ",
                       "*    " ],

               "8" : [ "*****",
                       "*   *",
                       "*****",
                       "*   *",
                       "*****" ],

               "9" : [ "*****",
                       "*   *",
                       "*****",
                       "    *",
                       "*****" ],

               "0" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ]

               }


for row in range(5):
    for char in text:
        # print(characters[char][row],row,char)
        printedtext[row] += (str(characters[char][row]) + "  ")
# print(printedtext)
offset = width
while True:
   #os.system("cls") #clears the terminal to show the output.
    for row in range(5):
        print(" " * offset + printedtext[row][max(0,offset*-1):width - offset])
    offset -=1

    if offset <= (len(text)*5) * -1:
        offset = width
    time.sleep(0.1)
