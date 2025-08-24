import string


hashtag="#"
nothing=""

user_input="Should, I. subscribe?!".title()
vse_gotovo_bez_znakiv = ''.join(ch for ch in user_input if ch not in string.punctuation)

print(hashtag+nothing.join(vse_gotovo_bez_znakiv.split())[:140])