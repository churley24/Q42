#Camryn Hurley

hashtag = '#'
def hash_spam(lines, hashtag):
    count = 0
    index = 0
    while index < len(lines):
        if lines[index:index+len(hashtag)] == hashtag:
            count += 1
            index += len(hashtag)
        else:
            index += 1
    if count >= 4:
        print("this tweet will be considered spam")
    else:
        print("none")
