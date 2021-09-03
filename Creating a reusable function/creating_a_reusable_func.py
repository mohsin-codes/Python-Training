def emoji_converter(msg):
    msg = message.split(" ")
    emojis = {
        ":)" : "😄",
        ":(" : "🙁"
    }

    output = ""
    for word in msg:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
output = emoji_converter(message)
print(output)