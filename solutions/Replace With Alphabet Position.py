def alphabet_position(text):
    new_string = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    space = ' '
    for i in range(len(text)):
        if i+1 == len(text)-1:
            space = ''
        if text[i] == "'" or text[i] == ' ' or text[i] == '.':
            i += 1
        else:
            for x in range(len(alphabet)):
                
                if text[i].lower() == alphabet[x]:
                    new_string += str(x+1)+space
                else:
                    x += 1
    return new_string
                
