# Allya Putri Ditya - 2309116078 

class Boneka :
    def __init__(self):
        self.order = [] #untuk simpan orderan

    def create_order(self, order_code, user_name, doll_name, color, size, quantity): #function untuk menambah orderan
        order = {"Item Code": order_code, "User Name": user_name, "Doll Name": doll_name, "Color": color,"Size": size, "Quantity": quantity}
        self.order.append(order)
        print("\nSuccessfully ordered.\nsend to our email (allya09ditya@gmail.com) to do your payment immediately!")

    def read_order(self,order_code): #function untuk membaca orderan
        for order in self.order: #mengecek apakah orderan ada dalam self.order
            if order["Item Code"] == order_code : #mengecek apakah code ada dalam orderan
                print ("================================================")
                print ("                  The Order                     ")
                print ("================================================")
                print("Item Code    : ", order["Item Code"])
                print("User Name    : ", order["User Name"])
                print("Doll Name    : ", order["Doll Name"])
                print("Color        : ", order["Color"])
                print("Size         : ", order["Size"])
                print("Quantity     : ", order["Quantity"])
                print("Total Price  :  IDR", order["Quantity"]*80000 )
                print ("================================================")
                return
        print("\nOrder not found!\n")

    def update_order(self, order_code, user_name, doll_name, color, size, quantity): #function untuk update orderan
        for order in self.order: #mengecek apakah orderan ada dalam self.order
            if order["Item Code"] == order_code : #mengecek apakah code ada dalam orderan
                if user_name:
                    order["User Name"] = user_name
                if doll_name:
                    order["Doll Name"] = doll_name
                if color:
                    order["Color"] = color
                if size :
                    order["Size"] = size 
                if quantity :
                    order["Quantity"] = quantity
                print("\nOrder successfully updated!\n")
                return
            print("\nOrder not found!\n")

    def delete_order(self, order_code): #function untuk menghapus orderan
        for order in self.order: #mengecek apakah orderan ada dalam self.order
            if order["Item Code"] == order_code:#mengecek apakah code ada dalam orderan
                ask = (input("are you sure? (y/n) : "))
                if ask == "y":
                    self.order.remove(order)
                    print("\nOrder successfully deleted!\n")
                    return
                elif ask == "n" :
                    return
                else :
                    print ("Invalid choice, try again!")
            else :
                print ("\nOrder not found!\n")

# Main program
if __name__ == "__main__":
    boneka = Boneka() #memberi variabel objek dari class

    while True :
        print ("\n================================================")
        print ("                Berryliz Shop                   ")
        print ("================================================\n")
        print("Welcome to the best doll store in this town!\n")
        print("1. Create Custom Order")
        print("2. Read Order")
        print("3. Update Order")
        print("4. Delete Order")
        print("5. Exit")
        pilihan = input("enter the number : ")

        if pilihan == "1":
            order_code = input("Enter your Order Code : ")
            user_name = input("Enter your name : ")
            doll_name = input("Enter the Doll Name : ")
            color = input("Enter the Color : ")
            size = int(input("Enter the size (xx.cm) : "))
            quantity = int(input("Enter the quantity : "))
            boneka.create_order(order_code, user_name, doll_name, color, size, quantity) #diarahkan ke function create_order

        elif pilihan == "2":
            order_code = input("Enter the order code : ")
            boneka.read_order(order_code) #diarahkan ke function read_order

        elif pilihan == "3":
            order_code = input("Enter your Order Code to Update : ")
            user_name = input("Enter your name to Update : ")
            doll_name = input("Enter the Doll Name to Update : ")
            color = input("Enter the Color to Update : ")
            size = int(input("Enter the size to Update (xx.cm) : "))
            quantity = int(input("Enter the quantity to Update : "))
            boneka.update_order(order_code, user_name, doll_name, color, size, quantity) #diarahkan ke function update_order

        elif pilihan == "4":
            order_code = input("Enter your Order Code to delete : ")
            boneka.delete_order(order_code) #diarahkan ke function delete_order

        elif pilihan == "5":
            break

        else :
            print("Please enter the correct number!\n")


