# Function to determine points based on books purchased
def calculate_points(books_purchased):
    if books_purchased == 0:
        points = 0
    elif books_purchased == 2:
        points = 5
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 6:
        points = 30
    elif books_purchased >= 8:
        points = 60
    else:
        points = 0  # Assuming other numbers (like 1, 3, 5, 7) earn 0 points
    return points
# Ask the user for the number of books purchased
books_purchased = int(input("Enter the number of books purchased this month: "))
# Calculate the points based on the number of books
points_awarded = calculate_points(books_purchased)
# Display the points awarded
print(f"You have earned {points_awarded} points.")
