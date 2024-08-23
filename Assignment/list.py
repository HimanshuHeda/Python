def list_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def main():
    # Example list
    lst = [2, 3, 4, 3, 1]
    
    # Calculating the product
    result = list_product(lst)
    
    print(f"The product of the elements in the list {lst} is: {result}")

if __name__ == "__main__":
    main()
