#Camryn Hurley

hashtag = '#'
def hash_spam(lines, hashtag):
    count = 0
    index = 0
    while index < len(lines):
        if lines[index:index+len(hashtag)] == hashtag <= 4:
            count += 1
            index += len(hashtag)
            print("this tweet will be considered spam")
        else:
            index += 1
            print("none")
