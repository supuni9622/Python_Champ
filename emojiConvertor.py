emojis = {
    ':(': '😥',
    ':)': '😀'
}

user_message = input('< ')
words = user_message.split(' ')

output = ''

for word in words:
    output += emojis.get(word, word) + ' '
print(output)
