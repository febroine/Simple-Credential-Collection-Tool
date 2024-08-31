import os
import json

def collect_credentials(directory):
    credentials = []

    for root, dirs, files in os.walk(directory):
        if 'Passwords.txt' in files:
            file_path = os.path.join(root, 'Passwords.txt')
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                url = username = password = None
                for line in lines:
                    if 'URL' in line:
                        url = line.split(':', 1)[1].strip()
                    elif 'Username' in line:
                        username = line.split(':', 1)[1].strip()
                    elif 'Password' in line or 'Passw' in line:
                        password = line.split(':', 1)[1].strip()
                
                if url and username and password:
                    credentials.append({
                        'File_Name': os.path.relpath(root, directory),
                        'URL': url,
                        'Username': username,
                        'Password': password
                    })

    return credentials

def main():
    directory = input("Please enter the directory path: ")
    credentials = collect_credentials(directory)

    output_file = os.path.join(os.getcwd(), 'credentials.json')
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(credentials, json_file, indent=2, ensure_ascii=False)

    print(f"Information has been written to {output_file}.")

if __name__ == "__main__":
    main()
