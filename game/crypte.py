"""
Created on Fri Jun 18 13:58:34 2021

@author: Iudhael ADIKPETO
"""

"""
cryptage
"""
"""
pour affecter un nombre hexadeecimal a une variable on procède comme suit
variable = 0xFAD5 commencer par 0x
pour affecter un nombre octale a une variable on procède comme suit
variable = 074 commencer par 0
"""
caractere = [
    " ", "!", "«", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",

    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?",

    "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",

    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "]", "^", "_",

    "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",

    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "□"

]

octal = [
    int(oct(0o40).replace("0o", "")), int(oct(0o41).replace("0o", "")), int(oct(0o42).replace("0o", "")),
    int(oct(0o43).replace("0o", "")), int(oct(0o44).replace("0o", "")), int(oct(0o45).replace("0o", "")),
    int(oct(0o46).replace("0o", "")), int(oct(0o47).replace("0o", "")), int(oct(0o50).replace("0o", "")),
    int(oct(0o51).replace("0o", "")), int(oct(0o52).replace("0o", "")), int(oct(0o53).replace("0o", "")),
    int(oct(0o54).replace("0o", "")), int(oct(0o55).replace("0o", "")), int(oct(0o56).replace("0o", "")),
    int(oct(0o57).replace("0o", "")), int(oct(0o60).replace("0o", "")),
    int(oct(0o61).replace("0o", "")), int(oct(0o62).replace("0o", "")),
    int(oct(0o63).replace("0o", "")), int(oct(0o64).replace("0o", "")), int(oct(0o65).replace("0o", "")),
    int(oct(0o66).replace("0o", "")), int(oct(0o67).replace("0o", "")), int(oct(0o70).replace("0o", "")),
    int(oct(0o71).replace("0o", "")), int(oct(0o72).replace("0o", "")),
    int(oct(0o73).replace("0o", "")), int(oct(0o74).replace("0o", "")), int(oct(0o75).replace("0o", "")),
    int(oct(0o76).replace("0o", "")), int(oct(0o77).replace("0o", "")), int(oct(0o100).replace("0o", "")),
    int(oct(0o101).replace("0o", "")), int(oct(0o102).replace("0o", "")),
    int(oct(0o103).replace("0o", "")), int(oct(0o104).replace("0o", "")), int(oct(0o105).replace("0o", "")),
    int(oct(0o106).replace("0o", "")), int(oct(0o107).replace("0o", "")), int(oct(0o110).replace("0o", "")),
    int(oct(0o111).replace("0o", "")), int(oct(0o112).replace("0o", "")),
    int(oct(0o113).replace("0o", "")), int(oct(0o114).replace("0o", "")), int(oct(0o115).replace("0o", "")),
    int(oct(0o116).replace("0o", "")), int(oct(0o117).replace("0o", "")), int(oct(0o120).replace("0o", "")),
    int(oct(0o121).replace("0o", "")), int(oct(0o122).replace("0o", "")),
    int(oct(0o123).replace("0o", "")), int(oct(0o124).replace("0o", "")), int(oct(0o125).replace("0o", "")),
    int(oct(0o126).replace("0o", "")), int(oct(0o127).replace("0o", "")), int(oct(0o130).replace("0o", "")),
    int(oct(0o131).replace("0o", "")), int(oct(0o132).replace("0o", "")),
    int(oct(0o133).replace("0o", "")), int(oct(0o135).replace("0o", "")), int(oct(0o136).replace("0o", "")),
    int(oct(0o137).replace("0o", "")), int(oct(0o140).replace("0o", "")),
    int(oct(0o141).replace("0o", "")), int(oct(0o142).replace("0o", "")),
    int(oct(0o143).replace("0o", "")), int(oct(0o144).replace("0o", "")), int(oct(0o145).replace("0o", "")),
    int(oct(0o146).replace("0o", "")), int(oct(0o147).replace("0o", "")), int(oct(0o150).replace("0o", "")),
    int(oct(0o151).replace("0o", "")), int(oct(0o152).replace("0o", "")),
    int(oct(0o153).replace("0o", "")), int(oct(0o154).replace("0o", "")), int(oct(0o155).replace("0o", "")),
    int(oct(0o156).replace("0o", "")), int(oct(0o157).replace("0o", "")), int(oct(0o160).replace("0o", "")),
    int(oct(0o161).replace("0o", "")), int(oct(0o162).replace("0o", "")),
    int(oct(0o163).replace("0o", "")), int(oct(0o164).replace("0o", "")), int(oct(0o165).replace("0o", "")),
    int(oct(0o166).replace("0o", "")), int(oct(0o167).replace("0o", "")), int(oct(0o170).replace("0o", "")),
    int(oct(0o171).replace("0o", "")), int(oct(0o172).replace("0o", "")),
    int(oct(0o173).replace("0o", "")), int(oct(0o174).replace("0o", "")), int(oct(0o175).replace("0o", "")),
    int(oct(0o176).replace("0o", "")), int(oct(0o177).replace("0o", ""))
]

decimale = [
    32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
    89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
    115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127
]

hexadecimal = [
    int(hex(0x20).replace("0x", "")), int(hex(0x21).replace("0x", "")), int(hex(0x22).replace("0x", "")),
    int(hex(0x23).replace("0x", "")), int(hex(0x24).replace("0x", "")), int(hex(0x25).replace("0x", "")),
    int(hex(0x26).replace("0x", "")), int(hex(0x27).replace("0x", "")), int(hex(0x28).replace("0x", "")),
    int(hex(0x29).replace("0x", "")), int(hex(0x2A), 16), int(hex(0x2B), 16), int(hex(0x2C), 16), int(hex(0x2D), 16),
    int(hex(0x2E), 16), int(hex(0x2F), 16), int(hex(0x30).replace("0x", "")), int(hex(0x31).replace("0x", "")),
    int(hex(0x32).replace("0x", "")), int(hex(0x33).replace("0x", "")), int(hex(0x34).replace("0x", "")),
    int(hex(0x35).replace("0x", "")), int(hex(0x36).replace("0x", "")), int(hex(0x37).replace("0x", "")),
    int(hex(0x38).replace("0x", "")), int(hex(0x39).replace("0x", "")), int(hex(0x3A), 16), int(hex(0x3B), 16),
    int(hex(0x3C), 16), int(hex(0x3D), 16), int(hex(0x3E), 16), int(hex(0x3F), 16), int(hex(0x40).replace("0x", "")),
    int(hex(0x41).replace("0x", "")), int(hex(0x42).replace("0x", "")), int(hex(0x43).replace("0x", "")),
    int(hex(0x44).replace("0x", "")), int(hex(0x45).replace("0x", "")), int(hex(0x46).replace("0x", "")),
    int(hex(0x47).replace("0x", "")), int(hex(0x48).replace("0x", "")), int(hex(0x49).replace("0x", "")),
    int(hex(0x4A), 16), int(hex(0x4B), 16), int(hex(0x4C), 16), int(hex(0x4D), 16), int(hex(0x4E), 16),
    int(hex(0x4F), 16), int(hex(0x50).replace("0x", "")), int(hex(0x51).replace("0x", "")),
    int(hex(0x52).replace("0x", "")), int(hex(0x53).replace("0x", "")), int(hex(0x54).replace("0x", "")),
    int(hex(0x55).replace("0x", "")), int(hex(0x56).replace("0x", "")), int(hex(0x57).replace("0x", "")),
    int(hex(0x58).replace("0x", "")), int(hex(0x59).replace("0x", "")), int(hex(0x5A), 16), int(hex(0xB), 16),
    int(hex(0x5D), 16), int(hex(0x5E), 16), int(hex(0x5F), 16), int(hex(0x60).replace("0x", "")),
    int(hex(0x61).replace("0x", "")), int(hex(0x62).replace("0x", "")), int(hex(0x63).replace("0x", "")),
    int(hex(0x64).replace("0x", "")), int(hex(0x65).replace("0x", "")), int(hex(0x66).replace("0x", "")),
    int(hex(0x67).replace("0x", "")), int(hex(0x68).replace("0x", "")), int(hex(0x69).replace("0x", "")),
    int(hex(0x6A), 16), int(hex(0x6B), 16), int(hex(0x6C), 16), int(hex(0x6D), 16), int(hex(0x6E), 16),
    int(hex(0x6F), 16), int(hex(0x70).replace("0x", "")), int(hex(0x71).replace("0x", "")),
    int(hex(0x72).replace("0x", "")), int(hex(0x73).replace("0x", "")), int(hex(0x74).replace("0x", "")),
    int(hex(0x75).replace("0x", "")), int(hex(0x76).replace("0x", "")),
    int(hex(0x77).replace("0x", "")), int(hex(0x78).replace("0x", "")), int(hex(0x79).replace("0x", "")),
    int(hex(0x7A), 16), int(hex(0x7B), 16), int(hex(0x7C), 16),
    int(hex(0x7D), 16), int(hex(0x7E), 16), int(hex(0x7F), 16)

]

Ascii7bits = [
    100000, 100001, 100010, 100011, 100100, 100101, 100110, 100111, 101000, 101001, 101010, 101011, 101100, 101101,
    101110, 101111, 110000, 110001, 110010, 110011, 110100, 110101, 110110, 110111, 111000, 111001, 111010, 111011,
    111100, 111101, 111110, 111111, 1000000, 1000001, 1000010, 1000011, 1000100, 1000101, 1000110, 1000111, 1001000,
    1001001, 1001010, 1001011, 1001100, 1001101, 1001110, 1001111, 1010000, 1010001, 1010010, 1010011, 1010100,
    1010101, 1010110, 1010111, 1011000, 1011001, 1011010, 1011011, 1011101, 1011110, 1011111, 1100000, 1100001,
    1100010, 1100011, 1100100, 1100101, 1100110, 1100111, 1101000, 1101001, 1101010, 1101011, 1101100, 1101101,
    1101110, 1101111, 1110000, 1110001, 1110010, 1110011, 1110100, 1110101, 1110110, 1110111, 1111000, 1111001,
    1111010, 1111011, 1111100, 1111101, 1111110, 1111111

]

print(len(hexadecimal))

print("--------------------Convertion alphanumerique--------------------")

print("1-> Convertion de caractere en décimale,hexadecimale,octal,ASCII 7 bits")
print("2-> Convertion du décimale en caractere")
print("3-> Convertion de l'hexadecimal en caractere")
print("4-> Convertion de l'octal en caractere")
print("5-> Convertion de l'ASCII 7 bits en caractere")

val = int(input("Choisissez une valeur : "))

while val >= 6 or val < 0:
    val = int(input("Essaiyez une autre valeur : "))

ch1 = "anb"
num = 1111111

if val == 1:
    print("\t1-> Convertion de caractere en décimal,hexadecimal,octal,ASCII 7 bits")
    print("\t1-> Convertion de '{}' en decimal".format(ch1))
    for i in range(0, len(ch1)):
        for j in range(len(caractere)):
            if ch1[i] == caractere[j]:
                # print(j)
                print(decimale[j], end=',')

    print("\n")
    print("\t2-> Convertion de '{}' en hexadecimal".format(ch1))
    for i in range(0, len(ch1)):
        for j in range(len(caractere)):
            if ch1[i] == caractere[j]:
                # print(j)
                print(hex(decimale[j]).replace("0x", ""), end=',')

    print("\n")
    print("\t3-> Convertion de '{}'en octal".format(ch1))
    for i in range(0, len(ch1)):
        for j in range(len(caractere)):
            if ch1[i] == caractere[j]:
                # print(j)
                print(oct(decimale[j]).replace("0o", ""), end=',')

    print("\n")
    print("\t3-> Convertion de '{}' en ASCII 7 bits".format(ch1))
    for i in range(0, len(ch1)):
        for j in range(len(caractere)):
            if ch1[i] == caractere[j]:
                # print(j)
                print(Ascii7bits[j], end=',')

if val == 2:
    print("\t2-> Convertion du décimal en caractere")
    for i in range(0, len(decimale)):
        if num == decimale[i]:
            print(caractere[i], end=' ')

print("\n")

if val == 3:
    print("3-> Convertion de l'hexadecimal en caractere")
    try:
        i = hexadecimal.index(num)
    except ValueError:
        print("Valeur non trouver")
    else:
        print(caractere[i], end=' ')

if val == 4:
    print("4-> Convertion de l'octal en caractere")
    try:
        i = octal.index(num)
    except ValueError:
        print("Valeur non trouver")
    else:
        print(caractere[i], end=' ')

if val == 5:
    print("5-> Convertion de l'ASCII 7 bits en caractere")
    for i in range(0, len(Ascii7bits)):
        if num == Ascii7bits[i]:
            print(caractere[i], end=' ')
