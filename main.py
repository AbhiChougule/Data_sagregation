def email_extraction(data):
    emails = []
    for line in data:
        for word in line.split(','):
            if '@' in word and word.endswith('.com'):
                emails.append(word)
    return emails

def number_extraction(data):
    numbers = []
    for line in data:
        for word in line.split(','):
            if word.isdigit() and len(word) in [9, 10]:
                numbers.append(word)
    return numbers

def special_char(data):
    special_characters = []
    for line in data:
        for word in line.split(','):
            word = word.strip()  # Remove spaces
            if any(not char.isalnum() for char in word):
                special_characters.append(word)
    return special_characters



def main():
    filename = 'test1.txt'
    with open(filename, 'r') as fp:
        data = fp.readlines()
    emails = email_extraction(data)
    print(emails)
    with open('email.txt', 'w') as fp:
        fp.write(str(emails))
    ph_no = number_extraction(data)
    print(ph_no)
    with open('ph_no.txt', 'w') as fp:
        fp.write(str(ph_no))
    spcl_char = special_char(data)
    print(spcl_char)
    with open('special_char.txt', 'w') as fp:
        fp.write(str(spcl_char))

if __name__ == '__main__':
    main()
