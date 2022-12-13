#Кодирование сообщения в битовый поток UTF-8
def msg_to_bin(text):
   encoding='utf-8'
   errors='surrogatepass'
   bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
   return " ".join(bits.zfill(8 * ((len(bits) + 7) // 8)))
 
