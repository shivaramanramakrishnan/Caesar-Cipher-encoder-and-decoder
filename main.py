alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  new_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift
        
      elif direction =="decode":
        new_position = position - shift
      new_text += alphabet[new_position]

    else:
      new_text += letter
  print(f"The {direction}d text is {new_text}")

import art
print(art.logo)

flag=True
while flag:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  
  shift = (shift%26)
  caesar(text=text, shift=shift, direction=direction)
  choice = input("Type 'yes' if you want to go again. Otherwise type 'no'")
  if choice =="no":
    flag = False
    print("Goodbye")