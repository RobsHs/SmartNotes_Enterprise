import requests

BASE_URL = "http://127.0.0.1:8000"

def menu():
    while True:
        print("\n=== SmartNotes CLI ===")
        print("1. Add Note")
        print("2. List Notes")
        print("3. Delete Note")
        print("0. Exit")

        c = input("Select: ")

        if c == "1":
            title = input("Title: ")
            content = input("Content: ")
            tags = input("Tags: ").split(",")
            requests.post(f"{BASE_URL}/notes", json={
                "title": title,
                "content": content,
                "tags": tags
            })

        elif c == "2":
            res = requests.get(f"{BASE_URL}/notes")
            for n in res.json():
                print(n)

        elif c == "3":
            nid = input("ID: ")
            requests.delete(f"{BASE_URL}/notes/{nid}")

        elif c == "0":
            break

if __name__ == "__main__":
    menu()
