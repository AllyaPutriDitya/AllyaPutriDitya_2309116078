# Allya Putri Ditya - 2309116078 
import math

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def read_order(self,order_code): #function untuk membaca orderan
        current = self.head
        while current:
            if current.data["Item Code"]  == order_code : #mengecek apakah code ada dalam orderan
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

    def mergeSort(self, arr, key):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid] #mendefinisikan bagian kiri
            R = arr[mid:] #mendefinisikan bagian kanan

            self.mergeSort(L, key)
            self.mergeSort(R, key)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i][key].lower() <= R[j][key].lower(): #mengurutkan orderan tanpa membedakan huruf yang sama di bagian capslock dan tidak capslock
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def display_orders(self, key='Item Code'): #menampilkan order sesuai item code
        current = self.head
        if current is None: #jika orderan tidak ada
            print("\nOrders are still empty")
            return

        order_list = []
        while current:
            order_list.append(current.data)
            current = current.next

        if key == 'User Name': #jika parameter berisikan user name
            print("\nSorting orders by User Name")
        else:
            print("\nSorting orders by", key)

        self.mergeSort(order_list, key) # Memanggil metode mergeSort untuk mengurutkan sesuai opsi yang telah dipilih

        print("\n================================================")
        print("------------------------------------------------")
        print("              Berryliz Order Lists              ")
        print("------------------------------------------------")
        print("================================================\n")
        for order in order_list:
            print("\n\n================================================")
            print("                  The Order                     ")
            print("================================================")
            print("Item Code    : ", order["Item Code"])
            print("User Name    : ", order["User Name"])
            print("Doll Name    : ", order["Doll Name"])
            print("Color        : ", order["Color"])
            print("Size         : ", order["Size"])
            print("Quantity     : ", order["Quantity"])
            print("Total Price  :  IDR", order["Quantity"] * 80000)
            print("================================================")

    def display_node(self): #function untuk menampilkan urutan orderan yang sudah diinput
        current = self.head
        if current is None: #jika orderan yang dicari tidak ada
            print("\nOrders are still empty.")
            return
        
        print("\n================================================")
        print("------------------------------------------------")
        print("              Berryliz Order Lists              ")
        print("------------------------------------------------")
        print("================================================\n")
        while current:
            print ("\n\n================================================")
            print ("                  The Order                     ")
            print ("================================================")
            print("Item Code    : ", current.data["Item Code"])
            print("User Name    : ", current.data["User Name"])
            print("Doll Name    : ", current.data["Doll Name"])
            print("Color        : ", current.data["Color"])
            print("Size         : ", current.data["Size"])
            print("Quantity     : ", current.data["Quantity"])
            print("Total Price  :  IDR", current.data["Quantity"]*80000 )
            print ("================================================\n")
            current = current.next

    def search_order(self, key, value):
        if key not in ["Item Code", "User Name"]: #mengecek inputan yang diberikan valid atau tidak
            print("Invalid search key.")
            return

        current = self.head
        order_list = []
        index = 0

        while current:
            order_list.append(current.data)
            current = current.next
            index += 1

        if key == "1": #mencari berdasarkan Item Code
            order_list.sort(key=lambda x: x[key])
        else:   #mencari berdasarkan User Name
            order_list.sort(key=lambda x: x[key].lower())

        n = len(order_list)
        x = value
        step = math.floor(math.sqrt(n)) #mencari hasil akar dari panjang orderan
        prev = 0

        while order_list[int(min(step, n) - 1)][key] < x: #untuk menentukan rentang di mana nilai yang dicari mungkin berada
            prev = step 
            step += math.sqrt(n)
            if prev >= n: #jika melebihi atau sama dengan panjang order_list
                print("Order not found!")
                return -1

        while order_list[int(prev)][key] < x: #menemukan nilai yang dicari dalam rentang yang sudah ditentukan
            prev += 1
            if prev == min(step, n): #jika sama dengan nilai minimal dari step dan n
                print("Order not found!")
                return -1

        if order_list[int(prev)][key] == x: #menampilkan index dan detail orderan
            index = 0
            current = self.head
            while current:
                if current.data == order_list[int(prev)]:
                    print("\n\nOrder found at index:", index)
                    print("================================================")
                    print("Item Code    : ", current.data["Item Code"])
                    print("User Name    : ", current.data["User Name"])
                    print("Doll Name    : ", current.data["Doll Name"])
                    print("Color        : ", current.data["Color"])
                    print("Size         : ", current.data["Size"])
                    print("Quantity     : ", current.data["Quantity"])
                    print("Total Price  :  IDR", current.data["Quantity"] * 80000)
                    print("================================================\n")
                    return
                current = current.next
                index += 1
        else:
            print("Order not found!")

# Main program
if __name__ == "__main__":
    boneka = Boneka() #memberi variabel objek dari class

    # record data
    boneka.create_order("XZ1", "Chenle", "Dolphin", "Light Blue", 65, 7, "first")
    boneka.create_order("BB4", "Mark Lee", "Watermelon", "Red", 25, 3, "last")

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
        print("6. Search Order")
        print("7. Exit")
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
            print("\nnote : It's important to remember the letter size! ")
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
            print("\nnote : It's important to remember the letter size! ")
            order_code = input("Enter your Order Code to delete : ")
            boneka.delete_order(order_code) #diarahkan ke function delete_order

        elif pilihan == "5":
            print("\n1. Sort by Item Code")
            print("2. Sort by User Name")
            print("3. Sort by Node")
            option = input("Enter the sorting option: ")
            if option == "1":
                boneka.display_orders("Item Code")
            elif option == "2":
                boneka.display_orders("User Name")
            elif option == "3":
                boneka.display_node()
            else:
                print("Invalid sorting option.")

        elif pilihan == "6":
            print ("\n1. Search by Item Code")
            print ("2. Search by User Name")
            search_key = input("Enter Search by : ")
            if search_key == "1":
                print("\nnote : It's important to remember the letter size! ")
                search_value = input("Enter the Item Code to search : ")
                boneka.search_order("Item Code", search_value)
            elif search_key == "2":
                print("\nnote : It's important to remember the letter size! ")
                search_value = input("Enter the User Name to search : ")
                boneka.search_order("User Name", search_value)

        elif pilihan == "7":
            break

        else :
            print("Please enter the correct number!\n")