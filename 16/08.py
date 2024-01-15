message_list = list()


def print_only_new(message):
    global message_list
    if message not in message_list:
        print(message)
        message_list.append(message)
