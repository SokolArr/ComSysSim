def msg_to_bin(message):
   temp_str = ' '.join("".join(f"{ord(i):08b}" for i in message))
   return temp_str

# print (msg_to_bin("Hello"))

