def email_extraction(data):
    words=[]
    for line in data:
        for word in line.split(','):
            if '@' in word:
                if word.endswith('.com'):
                    words.append(word)
    return words

def number_extraction(data):
    no=[]
    for line in data:
        for word in line.split(','):
            if word.isdigit() and len(word) in [9, 10]:
                no.append(word)
    return no

def special_char(data):
    char=[]
    for line in data:
        for word in line.split(','):
            if not word.isalpha() and word.isdigit():
                char.append(word)
    return word




def main():
    filename="test1.txt"
    fp = open(filename, "r")
    data = fp.readlines()
    emails=email_extraction(data)
    print(emails)
    fp = open('email', 'w')
    fp.write(str(emails))
    ph_no=number_extraction(data)

    print(ph_no)
    fp = open('ph_no', 'w')
    fp.write(str(ph_no))

    spcl_char=special_char(data)
    print(spcl_char)
    fp=open('special_char','w')
    fp.write(str(spcl_char))

if __name__=='__main__':
    main()