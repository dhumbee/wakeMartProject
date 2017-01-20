from customer import Customer

def main():
    print("Welcome to Wake-Mart.  Please register.")
    name = input("Enter your name: ")
    obj = Customer(name)
    obj.inputCardInfo()
    print("Registration completed.Rick")
    total_items_ordered = scanPrices()
    total_coupons = scanCoupons()
    amount_due = total_items_ordered - total_coupons
    print("\nTotal amount due: ", amount_due)
    makePayment(obj, amount_due)

# opens txt file with all item prices and stores keys and values in dictionary
def readPriceList():
    price_list = open("price_list.txt", "r")
    price_dict = {}
    for line in price_list:
        price = line.split()
        price_dict[price[0]] = price[1]
    return price_dict

# opens txt file with all coupon values and stores keys and values in dictionary
def readCouponList():
    coupon_list = open("coupon_list.txt", "r")
    coupon_dict = {}
    for line in coupon_list:
        coupon = line.split()
        coupon_dict[coupon[0]] = coupon[1]
    return coupon_dict

# user enters item codes, then searched for in dictionary of prices, if found, price is appended to list and summed
def scanPrices():
    prices = readPriceList()
    price_tuples = prices.items()
    print("\nPrice List:")
    for item in price_tuples:
        print(item)
    item_code = input("\nEnter a 4 digit product code [or 9999 to stop]: ")
    items_cost = []
    while item_code != "9999":
        if item_code in prices:
            print("Item found! Price is $", prices[item_code])
            items_cost.append(float(prices[item_code]))
        else:
            print("Item not found.")
        item_code = input("Enter a 4 digit product code [or 9999 to stop]: ")
    total_item_cost = sum(items_cost)
    print("Total cost of all items: ", total_item_cost)
    return total_item_cost

# user enters coupon codes, then searched for in dictionary of coupons, if found, coupon value is appended to list and summed
def scanCoupons():
    coupons = readCouponList()
    coupon_tuples = coupons.items()
    print("\nCoupons:")
    for item in coupon_tuples:
        print(item)
    coupon_code = input("\nEnter a 4 digit coupon code [or 9999 to stop]: ")
    coupon_values = []
    while coupon_code != "9999":
        if coupon_code in coupons:
            print("Coupon found! Value is $", coupons[coupon_code])
            coupon_values.append(float(coupons[coupon_code]))
        else:
            print("Coupon not found.")
        coupon_code = input("Enter a 4 digit coupon code [or 9999 to stop]: ")
    total_coupon_value = sum(coupon_values)
    print("Total coupon value: ", total_coupon_value)
    return total_coupon_value

def makePayment(object1, amount_due):
    choice = False
    while not choice:
        payment_method = input("\nChoose a payment method:\nPlease enter 1 for credit and 2 for debit: ")
        if payment_method == "1":
            security_code = input("Please enter credit card security code: ")
            verification = object1.verifyCreditCard(security_code)
            if verification == False:
                print("Security code incorrect, payment rejected.")
                choice = False
            else:
                print("The amount of ", amount_due, "will be charge to the card ending in ", object1.creditCardLastFour())
                choice = True
        elif payment_method == "2":
            pin = input("\nPlease enter debit card pin: ")
            verification = object1.verifyDebitCard(pin)
            if verification == False:
                print("Pin incorrect. Payment rejected.")
                choice = False
            else:
                print("The amount of ", amount_due, "will be charge to the card ending in ", object1.debitCardLastFour())
                choice = True

main()
