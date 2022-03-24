"""
(       )(  ___  )(  ____ )(  ____ \(  ____ \
| () () || (   ) || (    )|| (    \/| (    \/
| || || || |   | || (____)|| (_____ | (__
| |(_)| || |   | ||     __)(_____  )|  __)
| |   | || |   | || (\ (         ) || (
| )   ( || (___) || ) \ \__/\____) || (____/\
|/     \|(_______)|/   \__/\_______)(_______/



                            _______  _______  ______   _______
                            (  ____ \(  ___  )(  __  \ (  ____ \/
                            | (    \/| (   ) || (  \  )| (    \/
                            | |      | |   | || |   ) || (__
                            | |      | |   | || |   | ||  __)
                            | |      | |   | || |   ) || (
                            | (____/\| (___) || (__/  )| (____/\/
                            (_______/(_______)(______/ (_______/


                                             _______  _______  _                 _______  _______ _________ _______  _______
                                            (  ____ \(  ___  )( (    /||\     /|(  ____ \(  ____ )\__   __/(  ____ \(  ____ )
                                            | (    \/| (   ) ||  \  ( || )   ( || (    \/| (    )|   ) (   | (    \/| (    )|
                                            | |      | |   | ||   \ | || |   | || (__    | (____)|   | |   | (__    | (____)|
                                            | |      | |   | || (\ \) |( (   ) )|  __)   |     __)   | |   |  __)   |     __)
                                            | |      | |   | || | \   | \ \_/ / | (      | (\ (      | |   | (      | (\ (
                                            | (____/\| (___) || )  \  |  \   /  | (____/\| ) \ \__   | |   | (____/\| ) \ \__
                                            (_______/(_______)|/    )_)   \_/   (_______/|/   \__/   )_(   (_______/|/   \__/  """

Morse_Dictionary = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

Entry_section=input("Type your entry as either morse or word,number,punctuation format:").upper()

def morse_to_letter():
    # This function translates morse code into letters
    result = Entry_section.split()
    output=[]

    for i in result:
         for k,v in Morse_Dictionary.items():
             if i == v:
                 output.append(k)
             else:
                 pass

    print("".join(output))

def letter_to_morse():
    # This function translates words into morse codes
    result1 = list(Entry_section)
    output1=[]

    for i in result1:
         for k,v in Morse_Dictionary.items():
             if i == k:
                 output1.append(v)
             else:
                 pass

    print("".join(output1))

# Below code detects the entry whether it is morse code or not
control = list(Entry_section)
if control.count("-") > 4:
    morse_to_letter()
else:
    letter_to_morse()

