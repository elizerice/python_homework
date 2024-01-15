item_list = []
receipt_number = 0
def add_item(item_name, item_cost):
    global item_list
    item_list.append((item_name, item_cost))

def print_receipt():
    global receipt_number
    if len(item_list) > 0:
        receipt_number += 1

        print('Чек', receipt_number, '. Всего предметов: ', len(item_list))
        for item, cost in item_list:
            print(item, ' - ', cost)

        result_sum = sum(item[1] for item in item_list)
        print('Итого:', result_sum)
        print('-----')
        item_list.clear()
