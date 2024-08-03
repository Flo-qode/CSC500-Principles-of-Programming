def cost_of_meal():
    try:
        # User to enter the amount spent on food
        Cost_of_food = float(input("Enter the cost of the food: $"))
        
        # 18% tip charged
        tip_charged = Cost_of_food * 0.18
        
        # 7% sales tax charged
        sales_tax = Cost_of_food * 0.07
        
        # Total amount for cost of meal
        Total_amount = Cost_of_food + tip_charged + sales_tax
        
        # Display each section
        print(f"Cost of food: ${Cost_of_food:.2f}")
        print(f"18% Tip charged: ${tip_charged:.2f}")
        print(f"7% Sales tax charged: ${sales_tax:.2f}")
        print(f"Total amount: ${Total_amount:.2f}")
    
    except ValueError:
        print("Erro Message: The cost of food should be in  numbers not words.")

# Run the program
cost_of_meal()