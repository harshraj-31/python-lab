# Email Processing
emails = []

n = int(input("Enter number of emails: "))

for i in range(n):
    e = input("Enter email: ")
    emails.append(e)

domain_dict = {}

for e in emails:
    domain = e.split("@")[1]
    domain_dict[e] = domain

print("Dictionary:", domain_dict)

gmail = []

for e in emails:
    if "gmail.com" in e:
        gmail.append(e)

print("Gmail emails:", tuple(gmail))

count = {}

for e in emails:
    domain = e.split("@")[1]
    count[domain] = count.get(domain, 0) + 1

print("Domain count:", count)

unique_emails = set(emails)

print("Unique emails:", unique_emails)

print("Sorted emails:", sorted(unique_emails))