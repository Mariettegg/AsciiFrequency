#Written by Mario Gomez
#mariogomezmartin11@gmail.com

#### OBVSERVATIONS ####
# 1. This time did not get enough time to manage the interrupts
#    possible errors that may happen when introducing the wrong
#    commands in the console.
#
# 2. Also may want to install first the libraries listed below as
#    i got some problems trying to get them installed in my pycharm.
#
# 3. Please have the files of the texts you are going to analyse in
#    the same folder as this file, if not it wont work.

from matplotlib import pyplot as plt
import numpy as np


action = input("Action: (1) Input text, (2) Input file >> ")
option = input("Type of search: (1) All ascii values or (2) Alpha-numerical values only >> ")

if int(option) != 1 and int(option) != 2:
    print("Not an option.")

if int(action) == 2:
    file = input("File Name >> ")
    f = open(file, "r")
    text = f.readlines()

else:
    textInput = input("Text >> ")
    text = []
    text.append(textInput)

recordAlphaNum = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0')

# We have two different lists because if we want to see if they appear in the text, we need the actual value, but if we try to put that actual value in the axis, the value "written" wont appear
asciiList = (['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12',
          '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f',
          ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
          ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f'])
asciiListPlot = (['\\x00', '\\x01', '\\x02', '\\x03', '\\x04', '\\x05', '\\x06', '\\x07', '\\x08', '\\t', '\\n', '\\x0b', '\\x0c', '\\r', '\\x0e', '\\x0f', '\\x10', '\\x11', '\\x12',
          '\\x13', '\\x14', '\\x15', '\\x16', '\\x17', '\\x18', '\\x19', '\\x1a', '\\x1b', '\\x1c', '\\x1d', '\\x1e', '\\x1f',
          ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
          ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\\x7f'])
record = {}
freqTable = {}
totalCharacters = 0

if int(option) == 1:
    for line in text:
        for character in line:
            totalCharacters +=1
            if character in record.keys():
                record[character] += 1

            else:
                record[character] = 1

    dev_y = asciiList
    dev_x = []
    for character in asciiList:
        if character in record.keys():
            dev_x.append(int(record[character])/totalCharacters)
        else:
            dev_x.append(0)

    counter = 0
    for x in asciiListPlot:
        freqTable[x] = dev_x[counter]
        counter += 1
    print(freqTable)

    dev_y = np.arange(len(asciiListPlot))
    plt.xticks(dev_y, asciiListPlot)



else:
    for line in text:
        for character in line:

            if character in record.keys():
                record[character] += 1
                totalCharacters += 1

            elif character.lower() in record.keys():
                record[character.lower()] += 1
                totalCharacters += 1

            elif character.lower() in recordAlphaNum:
                record[character.lower()] = 1
                totalCharacters += 1

    dev_y = recordAlphaNum
    dev_x = []
    for character in recordAlphaNum:
        if character in record.keys():
            dev_x.append(int(record[character])/totalCharacters)
        else:
            dev_x.append(0)

    dev_y = np.arange(len(recordAlphaNum))
    plt.xticks(dev_y, recordAlphaNum)

    counter = 0
    for x in recordAlphaNum:
        freqTable[x] = dev_x[counter]
        counter += 1
    print(freqTable)


plt.bar(dev_y,dev_x)
plt.show()
