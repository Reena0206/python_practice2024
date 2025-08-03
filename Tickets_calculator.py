# Function to calculate price based on age
def get_ticket_price(age):
    if age < 12:
        return 100
    elif age < 60:
        return 200
    else:
        return 150

# Function to take input of group members' ages
def get_ages():
    ages = []
    count = int(input("Enter number of people in the group: "))
    for i in range(count):
        age = int(input(f"Enter age of person {i+1}: "))
        ages.append(age)
    return ages

# Function to calculate total price
def calculate_total(ages):
    total = 0
    prices = []
    for age in ages:
        price = get_ticket_price(age)
        prices.append(price)
        total += price
    return total, prices

# Function to display receipt
def print_receipt(ages, prices, total):
    print("\n🎟️ Movie Ticket Receipt 🎟️")
    print("---------------------------")
    for i in range(len(ages)):
        print(f"Person {i+1} (Age: {ages[i]}) - ₹{prices[i]}")
    print("---------------------------")
    print(f"Total Amount to Pay: ₹{total}")
    print("Enjoy your movie! 🍿")

# Main function
def main():
    ages = get_ages()
    total, prices = calculate_total(ages)
    print_receipt(ages, prices, total)

# Run the program
main()
