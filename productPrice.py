def priceCheck(products, productPrices, productSold, soldPrice):
    # product_dict ={}
    # for i in range(len(products)):
    #     product_dict.update({products[i]:productPrices[i]})

    # creating a dictionary with products as keys and productPrices as values
    product_dict = dict(zip(products, productPrices))
    print((product_dict))
    
    # error counter
    errors = 0
    
    # Looping through the sold products list and checking if it was the right price
    # if not increase the error counter by onef
    for i in range(len(productSold)):
        if product_dict[productSold[i]] != soldPrice[i]:
            errors += 1
    return errors


print(priceCheck(['eggs', 'milk', 'cheese'], [2.45, 3.14, 5.79], ['eggs', 'eggs', 'cheese', 'milk'], [2.89, 2.99, 5.79, 3.14]))
# Output: 2
print(priceCheck(['rice', 'sugar', 'wheat', 'cheese'], [16.89, 56.92, 20.89, 345.99], ['rice', 'cheese'], [16.89, 345.99]))
# Output: 0
