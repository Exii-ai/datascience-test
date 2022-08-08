from datascience_test.generator import Generator

generator = Generator()

# Question 1 
generator.question_1()

# Question 2
generator.question_2(fulfillment_status='fulfilled')

# Question 3
generator.question_3()

# Question 4
generator.question_4(fulfillment_status='fulfilled')

# Question 5
generator.question_5()

# Question 6
generator.question_6(fulfillment_status='fulfilled')

# Question 7
generator.question_7(fulfillment_status='fulfilled', date_from='2019-12-01', date_to='2020-03-31')

# Question 8
generator.question_8(fulfillment_status='fulfilled')

# Question 9
generator.question_9(fulfillment_status='fulfilled', date_interval_1=['2019-12-01','2019-12-30'], date_interval_2=['2020-01-01','2020-01-31'])

# Question 10
product_ids,product_ranks = generator.question_10()