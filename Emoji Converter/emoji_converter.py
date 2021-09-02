message = input(">")
msg = message.split(" ")
emojis = {
    ":)" : "😄",
    ":(" : "🙁"
}

output = ""
for word in msg:
    output += emojis.get(word, word) + " "
print(output)