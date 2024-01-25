import connect
from models import Authors, Quotes


def find_name(*args):
    if len(args) == 0:
        return f"Name is empty"
    quotes = []
    author_name = f"{' '.join(args)}"
    try:
        auth_id = Authors.objects.get(fullname=author_name).id
        for doc in Quotes.objects:
            if doc.author.id == auth_id:
                quotes.append(doc.quote)

        return f"All quotes of {author_name} : {quotes}"
    except:
        return f"Author does not exists"


def find_tag(*args):
    if len(args) == 0:
        return f"No tags..."

    quotes = []

    for doc in Quotes.objects:
        tags_list = doc.tags
        for tag in tags_list:
            if tag == args[0]:
                quotes.append(doc.quote)
    if quotes:
        return f'Quotes for tag "{args[0]}": {quotes}'
    else:
        return f"Tag not found"


def find_tags(*args):
    if len(args) == 0:
        return f"No tags..."

    quotes = []
    tags = args[0].split(",")

    for inputed_tag in tags:
        for doc in Quotes.objects:
            tags_list = doc.tags
            for tag in tags_list:
                if tag == inputed_tag:
                    if doc.quote not in quotes:
                        quotes.append(doc.quote)

    if quotes:
        return f'Quotes for tags "{tags}": {quotes}'
    else:
        return f"Tag not found"


CMD = {"name:": find_name, "tag:": find_tag, "tags:": find_tags}


def check_input(income_data):
    user_input = income_data.split()
    if user_input[0] in CMD.keys():
        cmd = user_input[0]
        func = CMD[cmd]
        value = user_input[1:]
        return func, value
    else:
        return None, f"Command not found"


while True:
    users_input = input(">>>").strip()
    if not users_input:
        continue
    if users_input == "exit":
        print("Good Bye!")
        break

    func, value = check_input(users_input)
    if not func:
        print(value)
    else:
        exe = func(*value)
        print(exe)
