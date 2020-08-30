# Variabel global untuk menyimpan data bunga
bunga = [["Sepatu", 10000], ["Mawar", 13000], ["Melati", 5000]]

# fungsi untuk menampilkan semua data
def list_bunga():
    #if len(bunga) <= 0:
        #print("Belum Ada, Silahkan Input Dulu")
    #else:
        i = 0
        for item in bunga:
            print("# " + str(i) + " | " +"Bunga "+ item[0] + " | " + "Harga "+ str(item[1]) + " #")
            i += 1

#input bunga baru
def input_bunga():
    x,y  = input("Nama dan Harga Bunga: ").split()
    #print(x)
    #print(y)
    bunga.append([x,y])

#edit data
def edit_data():
    list_bunga()
    i = int(input("Inputkan ID bunga: "))
    if(i > len(bunga)):
        print("ID salah")
    else:
        a,b  = input("Nama dan Harga Bunga: ").split()
        #nama = input("Nama dan Harga Bunga Baru: ")
        bunga[i] = [a,b]

#delete_data()
def delete_data():
    list_bunga()
    i = int(input("Inputkan ID bunga: "))
    if(i > len(bunga)):
        print("ID salah")
    else:
        bunga.remove(bunga[i])

#menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[1] List Bunga")
    print ("[2] Input Bunga")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    
    menu = int(input("PILIH MENU> "))
    print ("\n")
    
    if menu == 1:
        list_bunga()
    elif menu == 2:
        input_bunga()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Salah pilih!")


if __name__ == "__main__":

    while(True):
        show_menu()