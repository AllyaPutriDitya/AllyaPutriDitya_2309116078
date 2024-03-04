# Allya Putri Ditya - 2309116078 
class Node :
    def __init__(self, data):
        self.data = data
        self.nect = None

class Boneka :
    def __init__(self):
        self.head = None

    def __len__(self): #untuk menghitung panjang orderan
        current = self.head #mulai mencari dari self.head
        count = 0 # 0 untuk mendefinisikan dari count 
        while current:
            count += 1 #penambahan nilai ketika orderan bertambah
            current = current.next 
        return count

    def create_order(self, order_code, user_name, doll_name, color, size, quantity, position): #function untuk menambah orderan
        new_order = Node({"Item Code": order_code, "User Name": user_name, "Doll Name": doll_name, "Color": color,"Size": size, "Quantity": quantity, "Position": position})
        if position == "first":
            if self.head is None: #jika self.head belum ada
                self.head = new_order 
            else:
                new_order.next = self.head 
                self.head.prev = new_order
                self.head = new_order
        elif position == "last":
            if self.head is None: #jika self.head belum ada
                self.head = new_order
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_order
        elif position == "between":
            if len(self) < 2:  # Periksa jika struktur data hanya memiliki satu atau tidak ada node
                print("Sorry, we can't insert that Order to between, not enough orders.")
                return
            else:
                if len(self) % 2 == 0:  # Jika jumlah order genap
                    index = len(self) // 2  # Tentukan indeks tengah
                else:
                    index = (len(self) + 1) // 2  # Tentukan indeks tengah jika jumlah ganjil

                current = self.head
                for _ in range(index - 1):  #menyisipkan orderan
                    current = current.next

                new_order.next = current.next
                current.next = new_order
        else:
            print("Invalid position!")
        print("\nSuccessfully ordered.\nsend to our email (allya09ditya@gmail.com) to do your payment immediately!")

    def read_order(self,order_code): #function untuk membaca orderan
        current = self.head
        while current:
            if current.data == order_code : #mengecek apakah code ada dalam orderan
                print ("================================================")
                print ("                  The Order                     ")
                print ("================================================")
                print("Item Code    : ", current.data["Item Code"])
                print("User Name    : ", current.data["User Name"])
                print("Doll Name    : ", current.data["Doll Name"])
                print("Color        : ", current.data["Color"])
                print("Size         : ", current.data["Size"])
                print("Quantity     : ", current.data["Quantity"])
                print("Total Price  :  IDR", current.data["Quantity"]*80000 )
                print ("================================================")
                return
            current = current.next
        print("\nOrder not found!\n")

    def update_order(self, order_code, user_name, doll_name, color, size, quantity): #function untuk update orderan
        current = self.head
        while current:
            if current.data["Item Code"] == order_code : #mengecek apakah code ada dalam orderan
                if user_name:
                    current.data["User Name"] = user_name
                if doll_name:
                    current.data["Doll Name"] = doll_name
                if color:
                    current.data["Color"] = color
                if size :
                    current.data["Size"] = size 
                if quantity :
                    current.data["Quantity"] = quantity
                print("\nOrder successfully updated!\n")
                return
            current = current.next #current akan berubah dan didefinisikan current.next
            print("\nOrder not found!\n")

    def delete_order(self, order_code): #function untuk menghapus orderan
        current = self.head
        prev = None
        while current:
            if current.data["Item Code"] == order_code:#mengecek apakah code ada dalam orderan
                ask = (input("are you sure? (y/n) : "))
                if ask == "y":
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                    print("\nOrder successfully deleted!\n")
                    return
                elif ask == "n" :
                    return
                else :
                    print ("Invalid choice, try again!")
            prev = current
            current = current.next
        print ("\nOrder not found!\n")

    def display_orders(self): #function untuk menampilkan urutan orderan yang sudah diinput
        current = self.head
        if current is None: #jika orderan yang dicari tidak ada
            print("\nNo orders available.")
            return
        
        print("\n================================================")
        print("------------------------------------------------")
        print("              Berryliz Order Lists              ")
        print("------------------------------------------------")
        print("================================================\n")
        while current:
            print ("================================================")
            print ("                  The Order                     ")
            print ("================================================")
            print("Item Code    : ", current.data["Item Code"])
            print("User Name    : ", current.data["User Name"])
            print("Doll Name    : ", current.data["Doll Name"])
            print("Color        : ", current.data["Color"])
            print("Size         : ", current.data["Size"])
            print("Quantity     : ", current.data["Quantity"])
            print("Total Price  :  IDR", current.data["Quantity"]*80000 )
            print ("================================================")
            current = current.next
        print("\n================================================")

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
        print("5. Display Order")
        print("6. Exit")
        pilihan = input("enter the number : ")

        if pilihan == "1":
            order_code = input("Enter your Order Code : ")
            user_name = input("Enter your name : ")
            doll_name = input("Enter the Doll Name : ")
            color = input("Enter the Color : ")
            size = int(input("Enter the size (xx.cm) : "))
            quantity = int(input("Enter the quantity : "))
            position = (input("Enter the position (first/between/last) : "))
            boneka.create_order(order_code, user_name, doll_name, color, size, quantity,position) #diarahkan ke function create_order

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
            boneka.display_orders()

        elif pilihan == "6":
            break

        else :
            print("Please enter the correct number!\n")