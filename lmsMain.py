from lms import library

def main():
    while True:
        lib = library()
        print("\n╔═══════╣ LMS MENU ╠═══════╗")
        print("║    » 1- List Books       ║")
        print("║    » 2- Add Book         ║")
        print("║    » 3- Remove Book      ║")
        print("║    » q- Exit             ║")
        print("╚══════════════════════════╝\n")
        choice = input("» Enter your choice (1/2/3/q): ")
        
        if choice == '1':
            lib.listBooks()
        elif choice == '2':
            lib.addBook()
        elif choice == '3':
            lib.removeBook()
        elif choice == 'q':
            print("Exiting...")
            break
        else:
            print("» Invalid choice. Please enter a valid option.\n")


if __name__ == "__main__":
    main()