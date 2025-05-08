def add(n1,n2):
    """
    Add two integers and return the sum
    """
    return n1 + n2
def sub(n1,n2):
    """
    Subtract two integers and return the difference
    """
    return n1 - n2
def div(n1,n2):
    """
    Divide two numbers and return the quotient
    """
    if n2 == 0:
        print("\nDivision with 0 error!")
        return
    return n1 / n2
def mul(n1,n2):
    """
    Multiply two numbers and return the product
    """
    return n1 * n2

def display_result(result,operation,n1,n2):
    """
    Take the result, operation, n1, n2 then display combined results
    """
    print(f"The result of {n1} {operation} {n2} = {result}")

def expand(result):
    """
    To continue operation on the result
    """
    choice = input("\nWould you like to perform operation on the result ? y/n:").lower()
    if choice == 'y':
        main(result)
    else:
        return

def start(operation,result):
    #dictionary with key as operators and value as function
    operation_dict = {'+':add,'-':sub,'/':div,'x':mul}
    """
    Take operation:str,result:int as input and perform operations
    """
    if result != 0:
        n2 = int(input(f"Enter a number to {operation} :"))
        #perform operations each mapped to dictionary
        to_do = operation_dict[operation](result,n2) 
        #display result of the operation
        display_result(to_do,operation,result,n2)
        #continue expanding the result
        expand(to_do)
    else:
        n1 = int(input("Enter the first number :"))
        n2 = int(input("Enter the second number :"))
        #perform operations each mapped to dictionary
        to_do = operation_dict[operation](n1,n2)
        #display result of the operation
        display_result(to_do,operation,n1,n2)
        #continue expanding the result
        expand(to_do)

def main(result):
    """
    Main function
    """
    from logo import art
    print(f"\n{art}\n\nC A L C U L A T O R")
    print("""+\n-\n/\nx""")
    operation = input("Input the operation you want to perform :")
    start(operation,result)

main(0) #result set to 0 by default