import os

print("Choose mode:")
print("1. User Mode")
print("2. Admin Mode")
choice = input("Enter choice (1/2): ")

if choice == '1':
    os.system("streamlit run termpaperuser.py")
elif choice == '2':
    os.system("streamlit run termpaper.py")
else:
    print("Invalid choice.")
