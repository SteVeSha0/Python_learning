inv = {
    'gold coin': 42, 'rope': 1
    }

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        total += value
    print('Total number of items :' + str(total))

def addToInventory(inventory, addedItems):
    for items in addedItems:
        if items in inventory.keys():
            inventory[items] += 1
        else:
            inventory[items] = 1
    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
