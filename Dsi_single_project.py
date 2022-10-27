class Product:
    available_balance = 0

    def add_product(self, prod):
        list1 = []
        a = int(input("Enter Product id:"))
        prod[a] = {}
        # list1.append(a)
        nam = input("Enter product Name:")
        # list1.append(nam)
        prod[a]['p_name'] = nam
        price = float(input("Enter product Price:"))
        prod[a]["price"] = price
        # list1.append(price)
        sell_price = float(input("Enter sell_price of product:"))
        prod[a]["sell_price"] = sell_price
        # list1.append(sell_price)
        no_prod = int(input("Enter No_of_product:"))
        prod[a]["quantity"] = no_prod
        # list1.append(no_prod)
        # profit = sell_price - price
        prod[a]["profit"] =0

        # list1.append(profit)
        # prod[a]=list1
        # print(prod)

    def list_of_products(self, prod):

        print("Product Name           No_of_product             Profit")
        for p_id, p_info in prod.items():
            print(p_info["p_name"], end="                    ")
            # print("         ")
            print(p_info["quantity"], end="                  ")
            # print("         ")
            # print(p_info["profit"])

    def delete_product(self, prod):
        prod_num = int(input("Which product do you want to delete:"))
        del (prod[prod_num])


    def sell_product(self,prod):
        # name=input("Enter the product Name:")
        # name=name.lower()
        id=int(input("Enter Product id:"))
        quantity_no=int(input("Enter the total no of product you need:"))
        if(prod[id]['quantity']>=quantity_no):
            profit=quantity_no*(prod[id]['sell_price']-prod[id]['price'])
            new_quantity = (prod[id]['quantity']-quantity_no)
            prod[id]['quantity']=new_quantity
            prod[id]['profit']=profit
            self.available_balance = self.available_balance+(prod[id]['sell_price']*quantity_no)
            print(self.available_balance)
        else:
            print("Insufficient no of product")


    def buy_product(self, prod):
        p_no=int(input("Enter the product no:"))
        no_of_prod=int(input("How many product you want to bought:"))
        prod_price=prod[p_no]['price']
        if(self.available_balance>=(prod_price*no_of_prod)):
            self.available_balance= self.available_balance-(prod_price*no_of_prod)
            prod[p_no]['quantity']=no_of_prod+prod[p_no]['quantity']
        else:
            print("Insufficient balance")






if __name__ == '__main__':
        p1=Product()
        prod = {}

        while(1):
                print("\t\t-----Welcome to the Shop-----")
                print("\t\t\t1.Add any Elements")
                print("\t\t\t2.Delete a product")
                print("\t\t\t3.Buy a Product")
                print("\t\t\t4.Sell a Product")
                print("\t\t\t5.See list of product")
                print("\t\t\t6.See the available balance")
                print("\t\t\t7.Exit the system")
                print("----------------------------------------------------")
                a = int(input("\t\tChoose an Option:"))

                if (a == 1):
                    p1.add_product(prod)
                elif (a == 2):
                    p1.delete_product(prod)
                elif (a == 3):
                    p1.buy_product(prod)
                elif (a == 4):
                    p1.sell_product(prod)
                elif (a == 5):
                    p1.list_of_products(prod)
                elif (a == 6):
                    print(p1.available_balance)
                elif (a == 7):
                    break


