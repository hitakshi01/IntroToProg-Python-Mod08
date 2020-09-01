# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Hitakshi,8.30.2020,Modified code to complete assignment 8
# Hitakshi,8.31.2020,Added error handling to code
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2020,Created Class
        Hitakshi,8.30.2020,Modified code to complete assignment 8
    """

    # getter
    @property
    def product_name(self):
        return self.__product_name

    @property
    def product_price(self):
        return self.__product_price

    # setter
    @product_name.setter  # setting value frequently
    def product_name(self, prodName:str):
        if str(prodName).isnumeric() == False:
            self.__product_name = prodName
        else:
            raise Exception("Product Names cannot be numbers")

    @product_price.setter
    def product_price(self, prodPrice:float):
        self.__product_price = prodPrice

    def __str__(self):
        productInfo = self.__product_name + "," + str(self.__product_price)  # Accessing attributes directly
        return productInfo
        pass

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #

class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2020,Created Class
        Hitakshi,08.30.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        try:
            objFile = open(file_name, "w")
            for object in list_of_product_objects:
                objFile.write(object.__str__() + "\n")
            objFile.close()
        except Exception as e:
            print("There is some problem in saving product details to file.")
            raise Exception(e)

    @staticmethod
    def read_data_from_file(file_name):
        try:
            objFile = open(file_name, "r")
            lstProdItems = []
            for row in objFile:
                name, price = row.strip().split(",")
                objProduct = Product()
                objProduct.product_name = name  # call setter
                objProduct.product_price = price  # call setter

                lstProdItems.append(objProduct)
            objFile.close()
            return lstProdItems
        except Exception as e:
            print("There is an error processing the file")
            raise Exception(e)

    pass


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # """Group of functions used to perform Input/Output operations from the user:
    #     methods:

    # print_menu_Tasks() - Show Current Products
    # input_menu_choice() - Takes user choice as input
    # print_current_product_items_in_list() -
    # input_new_task_and_priority() -
    #

    # changelog: (When,Who,What)
    # Hitakshi,08.30.2020,Created Class
    #     """
    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user
            :return: nothing
        """
        print('''
            Menu of Options
            1)Show Current Products
            2)Add a new Product
            3)Save Product to File and Exit 
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    pass

    @staticmethod
    def print_current_product_items_in_list(list_product_objects):
        """ Shows the current product and its price
        :param list_product_objects: (list) of product objects you want to display
        :return: nothing
        """
        print("******* The current Products are: *******")
        for prod_object in list_product_objects:
            print(prod_object)  # calls __str__ function in Product Class
        print("*******************************************")

        print()  # Add an extra line for looks

    @staticmethod
    def add_product():
        product_name = str(input("Enter Product Name: ")).strip()# Captures Product Name
        product_price = float(input("Enter Product Price: ")) # Captures Product Price
        return product_name, product_price  # packs as tuple
        pass

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program

try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
    while True:
        IO.print_menu_Tasks()
        userChoice = IO.input_menu_choice()
        if userChoice == "1":
            IO.print_current_product_items_in_list(lstOfProductObjects)
        elif userChoice == "2":
            added_ProductName, added_ProductPrice = IO.add_product()
            newProductObj = Product()
            newProductObj.product_name = added_ProductName
            newProductObj.product_price = added_ProductPrice
            lstOfProductObjects.append(newProductObj)
        elif userChoice == "3":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print("Product information is saved in the file. Exiting from the program! ")
            break
        else:
            print("Please select options from [1,2,3]")
except Exception as e:
    print("We ran into technical issue :)")
    raise Exception(e)
# Main Body of Script  ---------------------------------------------------- #
