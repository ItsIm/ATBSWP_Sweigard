dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(items):
    print('Инвентарь:')
    itemTotals = 0
    for i, j in items.items():
        print(f'{i} - {j}')
        itemTotals += j
    print(f'Всего предметов в инвентаре: {itemTotals}')

def add_to_inventory(inventory, addItems):
    for i in addItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

inv = add_to_inventory(inventory, dragonLoot)
display_inventory(inv)
