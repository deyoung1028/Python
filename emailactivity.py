with open("emails.txt") as file_object:
    emails = file_object.read()

duplicate_emails = emails.split(',')
print(duplicate_emails)

duplicate_free_emails = []

for email in duplicate_emails:
    if email not in duplicate_free_emails:
        duplicate_free_emails.append(email)

print(duplicate_free_emails)

with open("duplicate-free-email.txt", "w") as file:
    for email in duplicate_free_emails:
        file.write(email)
        file.write("\n")

