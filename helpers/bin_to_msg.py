#Декодирование сообщения из битового потока в символы UTF-8
def bin_to_msg(text):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(text)]*8))