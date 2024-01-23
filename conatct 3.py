import pandas as pcl

def add_c_to_excel(file_path):
    try:
        
        try:
            exist_c = pcl.read_excel(file_path)
        except FileNotFoundError:
            exist_c = pcl.DataFrame(columns=['Name', 'Email', 'Phone'])

        
        name = input('Enter Name: ')
        email = input('Enter Email: ')
        phone = input('Enter Phone: ')

       
        new_contact = pcl.DataFrame([[name, email, phone]], columns=['Name', 'Email', 'Phone'])
        upclated_contacts = pcl.concat([exist_c, new_contact], ignore_index=True)

        
        upclated_contacts.to_excel(file_path, index=False)

        print(f'Contact added to {file_path}')

    except Exception as e:
        print(f'Error adding contact: {e}')

def delete_c_from_excel(file_path):
    try:
       
        try:
            exist_c = pcl.read_excel(file_path)
        except FileNotFoundError:
            print(f'File {file_path} not found.')
            return

       
        delete_name = input('Enter the name of the contact to delete: ')

        upclated_contacts = exist_c[exist_c['Name'] != delete_name]

        
        upclated_contacts.to_excel(file_path, index=False)

        print(f'Contact deleted from {file_path}')

    except Exception as e:
        print(f'Error deleting contact: {e}')

def search_c_in_excel(file_path):
    try:
       
        try:
            exist_c = pcl.read_excel(file_path)
        except FileNotFoundError:
            print(f'File {file_path} not found.')
            return

        
        search_name = input('Enter the name of the contact to search: ')

        found_contact = exist_c[exist_c['Name'] == search_name]

        
        if not found_contact.empty:
            print(f'Contact found:')
            print(found_contact.iloc[0])  
        else:
            print(f'Contact with name {search_name} not found.')

    except Exception as e:
        print(f'Error searching contact: {e}')

def list_c_in_excel(file_path):
    try:
       
        try:
            exist_c = pcl.read_excel(file_path)
        except FileNotFoundError:
            print(f'File {file_path} not found.')
            return

       
        print('All Contacts:')
        print(exist_c)

    except Exception as e:
        print(f'Error listing contacts: {e}')

file_path = 'contacts.xlsx'

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. List All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    if choice == '1':
        add_c_to_excel(file_path)
    elif choice == '2':
        delete_c_from_excel(file_path)
    elif choice == '3':
        search_c_in_excel(file_path)
    elif choice == '4':
        list_c_in_excel(file_path)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


