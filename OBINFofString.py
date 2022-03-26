#help url     ---->    https://docs.python.org/3/library/stdtypes.html



#bytearray.isalnum()¶
#Return true if all bytes in the sequence are alphabetical ASCII characters or ASCII decimal digits and the sequence is not empty, false otherwise.
#Alphabetic ASCII characters are those byte values in the sequence b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.
#ASCII decimal digits are those byte values in the sequence b'0123456789'.

print('ABCabc1'.isalnum())#True
print('ABC abc1'.isalnum())#False
print("Durga768 is alpha numaric",'Durga768'.isalnum()) # True
print("Durga is alpha numbaric",'Durga'.isalnum())#True

#bytes.isalpha()¶
#bytearray.isalpha()
#Return true if all bytes in the sequence are alphabetic ASCII characters and the sequence is not empty, false otherwise.
#Alphabetic ASCII characters are those byte values in the sequence b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.
print("durga has only alphabetic characters ",'durga'.isalpha())#True
print("durga1 has only alphabetic characters ",'durga1'.isalpha())#False
print("'' has only alphabetic characters ",''.isalpha())#False
print("' ' has only alphabetic characters ",' '.isalpha())#False



#str.isdigit()¶
#Return true if all characters in the string are digits and there is at least one character, false otherwise.
#Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits.
#This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formally,
#a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.
print("all characters in the string '897845' are digits characters",'897845'.isdigit()) # True 
print("all characters in the string '897.845' are digits characters",'897.845'.isdigit()) # False
print("all characters in the string 'durga' are digits characters",'durga'.isdigit())#False

#str.islower()¶
#Return true if all cased characters [4] in the string are lowercase and there is at least one cased character, false otherwise.
print("abc is in lower case",'abc'.islower())#True
print("Abc is in lower case",'Abc'.islower())#False
print("abc232 is in lower case",'abc123'.islower())#True

#bytes.isupper()¶
#bytearray.isupper()
#Return true if there is at least one uppercase alphabetic ASCII character in the sequence and no lowercase ASCII characters, false otherwise.
print("ABCDEF is in upper case",'ABCDEF'.isupper())#True
print("AbcdeF is in upper case",'AbcdeF'.isupper())#False
print("ABCDEF123 is in upper case",'ABCDEF123'.isupper())#True

#bytes.istitle()¶
#bytearray.istitle()
#Return true if the sequence is ASCII titlecase and the sequence is not empty, false otherwise.
#See bytes.title() for more details on the definition of “titlecase”.
print("'Learning Python' is a title",'Learning Python'.istitle()) #True
print("'Learning python' is a title",'Learning python'.istitle())#False
print("lLearning python' is a title",'learning python'.istitle())#False
print("'Learning Python 124' is a title",'Learning Python 124'.istitle())#True
print("'123earning Python' is a title",'123earning Python'.istitle())#False
print("'L1234earning Python' is a title",'L1234earning Python'.istitle())#False
print("'L1234earning Python9090' title",'L1234earning Python9090'.istitle())#False
print("'Learning Python9090' title",'Learning Python9090'.istitle()) #True
print("'Learning Python @' title",'Learning Python @'.istitle())#True
print("'@Learning Python' is a title",'@Learning Python'.istitle())#True
print("'Learning Python @#$' is a title",'Learning Python @#$'.istitle())#True

#bytes.isspace()¶
#bytearray.isspace()
#Return true if all bytes in the sequence are ASCII whitespace and the sequence is not empty, false otherwise.
#ASCII whitespace characters are those byte values in the sequence b' \t\n\r\x0b\f' (space, tab, newline, carriage return, vertical tab, form feed).
print("'       ' is whitespace string",'       '.isspace()) #True
print("'DurgaSoft' is whitespace string",'DurgaSoft'.isspace())#False
print("'   DurgaSoft    ' is whitespace string",'   DurgaSoft    '.isspace()) #False
print("'Durga Soft' is whitespace string",'   Durga Soft    '.isspace())#False
print("'' is whitespace string",''.isspace()) #False
print("'\\t' is whitespace string",'\t'.isspace())#True
print("'\\r' is whitespace string",'\r'.isspace())#True
print("'\\r\\t\\n' is whitespace string",'\r\t\n'.isspace())#True
print("'\\x0b' is whitespace string",'\x0b'.isspace()) #True
print("'\\f' is whitespace string",'\f'.isspace()) #True

#\\f












