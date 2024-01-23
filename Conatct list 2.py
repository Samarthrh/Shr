import pandas as pd

def add_contact_to_excel(file_path):
    try:
        
        try:
            existing_contacts = pd.read_excel(file_path)
        except FileNotFoundError:
            existing_contacts = pd.DataFrame(columns=['Name', 'Email', 'Phone'])

        
        name = input('Enter Name: ')
        email = input('Enter Email: ')
        phone = input('Enter Phone: ')

       
        new_contact = pd.DataFrame([[name, email, phone]], columns=['Name', 'Email', 'Phone'])
        updated_contacts = pd.concat([existing_contacts, new_contact], ignore_index=True)

        
        updated_contacts.to_excel(file_path, index=False)

        print(f'Contact added to {file_path}')

    except Exception as e:
        print(f'Error adding contact: {e}')

def delete_contact_from_excel(file_path):
    try:
       
        try:
            existing_contacts = pd.read_excel(file_path)
        except FileNotFoundError:
            print(f'File {file_path} not found.')
            return

       
        delete_name = input('Enter the name of the contact to delete: ')

        updated_contacts = existing_contacts[existing_contacts['Name'] != delete_name]

        
        updated_contacts.to_excel(file_path, index=False)

        print(f'Contact deleted from {file_path}')

    except Exception as e:
        print(f'Error deleting contact: {e}')

def search_contact_in_excel(file_path):
    try:
       
        try:
            existing_contacts = pd.read_excel(file_path)
        except FileNotFoundError:
            print(f'File {file_path} not found.')
            return

        
        search_name = input('Enter the name of the contact to search: ')

        found_contact = existing_contacts[existing_contacts['Name'] == search_name]

        
        if not found_contact.empty:
            print(f'Contact found:')
            print(found_contact.iloc[0])  
        else:
            print(f'Contact with name {search_name} not found.')

    except Exception as e:
        print(f'Error searching contact: {e}')

def list_all_contacts_in_excel(file_path):
    try:
       
        try:
            existing_contacts = pd.read_excel(file_path)
        except FileNotFoundError:
            print(f'File {file_path} not found.')
            return

       
        print('All Contacts:')
        print(existing_contacts)

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
        add_contact_to_excel(file_path)
    elif choice == '2':
        delete_contact_from_excel(file_path)
    elif choice == '3':
        search_contact_in_excel(file_path)
    elif choice == '4':
        list_all_contacts_in_excel(file_path)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
