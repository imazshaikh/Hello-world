product = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(product)
sorted_product = sorted(product, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_product)