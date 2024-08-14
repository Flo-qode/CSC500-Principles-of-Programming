# Function to collect rainfall data and calculate statistics
def calculate_rainfall():
    # Get the number of years from the user
    num_years = int(input("Enter the number of years: "))
    # Initialize total rainfall and total months
    total_rainfall = 0.0
    total_months = 0
    # Outer loop to iterate over each year
    for year in range(1, num_years + 1):
        print(f"\nYear {year}:")
        # Inner loop to iterate over each month
        for month in range(1, 13):
            # Get rainfall for the month
            monthly_rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            # Add the monthly rainfall to the total rainfall
            total_rainfall += monthly_rainfall
        # Increment total months by 12 (for each year)
        total_months += 12
    # Calculate the average rainfall per month
    average_rainfall = total_rainfall / total_months
    # Display the results
    print("\nTotal number of months:", total_months)
    print("Total inches of rainfall:", total_rainfall)
    print("Average rainfall per month:", average_rainfall)
# Run the function to collect data and calculate rainfall statistics
calculate_rainfall()
