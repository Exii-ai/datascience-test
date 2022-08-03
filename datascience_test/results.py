from generator import Generator

generator = Generator()

# Example function
generator.example()

# Question One
print(
    "\nThe top 3 averagely highest priced product_id: ",
    ", ".join(generator.question_1(average=False).astype(str)),
)

print(
    "\nThe top 3 individually highest priced product_id: ",
    ", ".join(generator.question_1().astype(str)),
)

# Question Two
for criterion in ["order_revenue", "price", "quantity", "item_spend"]:
    print(
        f"\nThe top 3 best selling vendors based on {criterion}: ",
        ", ".join(generator.question_2(criterion=criterion)),
    )

# Question Three
print(f"\nThe product_id with most variants: {generator.question_3()}")

# Question Four
print(f"\nThe product_id sold to the most unqiue customer: {generator.question_4()}")

# Question Five
print(f"\nThe worst performing day in terms of revenue: {generator.question_5()}")

# Question Six
print(f"\nThe highest discount to revenue ratio: {generator.question_6()}")

# Question Seven
print(
    "\nThe top 3 best selling product_id in December 2019 regarding the revenue:",
    ", ".join(generator.question_7()[0].astype(str)),
)
print(
    "\nThe top 3 best selling product_id in March 2020 regarding the revenue:",
    ", ".join(generator.question_7()[1].astype(str)),
)
# Question Eight
print(f"\nThe ID of customer with the largest AOV: {generator.question_8()}")

# Question Nine
print(
    "\nThe top 3 growing products in terms of revenue from Dec 2019 to Jan 2020:",
    ", ".join(generator.question_9().astype(str)),
)

# Question Ten
print(
    "\nThe 3 most appealing products to new customer:",
    ", ".join(generator.question_10().head(3).index.astype(str)),
)
