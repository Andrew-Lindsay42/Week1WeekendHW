# WRITE YOUR FUNCTIONS HERE

# PET SHOP FUNCTIONS

def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop, cash):
    pet_shop['admin']['total_cash'] += cash

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, sold):
    pet_shop['admin']['pets_sold'] += sold

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop, breed):
    pets_of_breed = []
    for pet in pet_shop['pets']:
        if breed == pet['breed']:
            pets_of_breed.append(pet)
    return pets_of_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if name == pet['name']:
            return pet
    return None

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if name == pet['name']:
            pet_shop['pets'].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)

# CUSTOMER FUNCTIONS

def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer, cash):
    customer['cash'] -= cash

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, pet):
    customer['pets'].append(pet)