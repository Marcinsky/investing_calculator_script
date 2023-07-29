class Projects:

    def calculating(self):
        current_wealth = int(input("Type your current savings: "))
        rate_of_return = int(input("Type your yearly rate of return: "))
        monthly_savings = int(input("Type your monthly savings: "))
        years = int(input("Type your period of time: "))
        total_savings = current_wealth
        for year in range(1, years + 1):
            interest = total_savings * (rate_of_return / 100)
            total_savings += interest + (monthly_savings*12)
            print(f"Year {year}: Total wealth = {total_savings:.2f}")
        return "Your future wealth would be: " and total_savings

    print(calculating(self=5))
#result should be 100 * 5
#1: 100 * 10% = 110
#2: 110 * 10% = 121
#3: 121 * 10% = 132.1
#4: 132.1 * 10% = 145.31
#5: 145.31 * 10% = 159,841a