# Mobile Service Provider
numbers = []

n = int(input("Enter number of mobile numbers: "))

for i in range(n):
    num = input("Enter number: ")
    numbers.append(num)

provider_dict = {}

for num in numbers:
    if num.startswith(("98", "99")):
        provider = "Airtel"
    elif num.startswith("97"):
        provider = "Jio"
    elif num.startswith("96"):
        provider = "VI"
    else:
        provider = "Other"

    provider_dict[num] = provider

print("Dictionary:", provider_dict)

airtel_numbers = []

for num, prov in provider_dict.items():
    if prov == "Airtel":
        airtel_numbers.append(num)

print("Airtel numbers:", tuple(airtel_numbers))

count = {}

for prov in provider_dict.values():
    count[prov] = count.get(prov, 0) + 1

print("Provider count:", count)

print("Sorted numbers:", sorted(numbers))