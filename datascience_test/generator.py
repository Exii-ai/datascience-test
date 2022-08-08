from datascience_test.data import Data
import pandas as pd

class Generator:

    def __init__(self):

        self.data = Data()

        # Add another column to the orders data indicating the actual revenue of an order (=0 for unfulfilled orders)        
        self.data.orders['actual_revenue'] = self.data.orders['order_revenue']
        self.data.orders.loc[self.data.orders['fulfillment_status']!='fulfilled', 'actual_revenue'] *= 0

        # Add the customer id column to the orders data
        self.data.orders['customer_id'] = self.data.orders.order_id.map(self.data.customers.set_index('order_id')['customer_id'].to_dict())
        
    def question_1(self):
        '''
        This function returns the 3 products with highest price
        '''
        product_ids = self.data.orders.sort_values(by='price', ascending=False).iloc[0:3]['product_id']

        print("The product IDs with highest prices are:\n")
        for product_id in product_ids:
            print(product_id)

    def question_2(self, fulfillment_status='fulfilled'):
        '''
        This function returns the 3 best selling vendors, in terms of revenue.
        We aggreagte the revenue column and select the vendors with highest revenues.
        
        - Note: the function calculates the revenue only on the "fulfilled" orders.
                If we want the revenue to be calculated on all orders, we can simply
                change the "fulfillment_status" argument.
        '''

        base_df = self.data.orders
        if fulfillment_status=='fulfilled':
            base_df = base_df[base_df['fulfillment_status']=='fulfilled']

        top_vendors = base_df.groupby(['vendor'])['order_revenue'].sum().sort_values(ascending=False)[0:3]

        print("The 3 highest selling vendors are:\n")
        for vendor_name in top_vendors.index:
            print(vendor_name)

    def question_3(self):
        '''
        This function returns the product with most variants
        '''

        product_variants = self.data.orders.groupby(['product_id']).variant_id.nunique()
        print("The product %d has most variants (%d items)." %(product_variants.idxmax(),product_variants.max()))


    def question_4(self, fulfillment_status='fulfilled'):
        '''
        This function calculates the product sold to most unique customers

        - Note: the function calculates the revenue only on the "fulfilled" orders.
                If we want the revenue to be calculated on all orders, we can simply
                change the "fulfillment_status" argument.
        '''

        base_df = self.data.orders
        if fulfillment_status=='fulfilled':
            base_df = base_df[base_df['fulfillment_status']=='fulfilled']

        top_products = base_df.groupby(['product_id'])['customer_id'].nunique()

        print("The product with %d, sold to %d unique customers, is the best selling in that regard." %(top_products.idxmax(),top_products.max()))


    def question_5(self):
        '''
        This function calculates the worst performing day, in terms of revenue

        - Note: for this function, we consider "actual revenue", i.e. if an order
                is not fulfilled, the actual_revenue is considered to be zero.
                Then, the worst day could be a day without any fulfilled orders
        '''
        
        revenue_by_date = self.data.orders.groupby(['processed_at'])['actual_revenue'].sum()

        print("The worst performing date, with %.2f revenue, was %s." %(revenue_by_date.min(),revenue_by_date.idxmin()))


    def question_6(self, fulfillment_status='fulfilled'):
        '''
        This function calculates the order with the most amount of discount

        - Note: the function calculates the revenue only on the "fulfilled" orders.
                If we want the revenue to be calculated on all orders, we can simply
                change the "fulfillment_status" argument.
        '''

        base_df = self.data.orders
        if fulfillment_status=='fulfilled':
            base_df = base_df[base_df['fulfillment_status']=='fulfilled']

        most_discount = base_df.groupby(['order_id'])['discount_amount'].sum()

        print("The order with id %d has the maximum discount of %.2f" %(most_discount.idxmax(),most_discount.max()))


    def question_7(self, fulfillment_status='fulfilled', date_from='2019-12-01', date_to='2020-03-31'):
        '''
        This function calculates the best selling products in the specified range

        - Note: the function calculates the revenue only on the "fulfilled" orders.
                If we want the revenue to be calculated on all orders, we can simply
                change the "fulfillment_status" argument.
        '''

        base_df = self.data.orders
        if fulfillment_status=='fulfilled':
            base_df = base_df[base_df['fulfillment_status']=='fulfilled']

        queried_df = base_df[(base_df['processed_at'] > date_from) & (base_df['processed_at'] < date_to)]

        best_selling_products = queried_df.groupby(['product_id'])['order_revenue'].sum().sort_values(ascending=False)[0:3]

        print("The 3 best selling products in the interval [%s,%s] are:\n" %(date_from,date_to))
        for product_id in best_selling_products.index:
            print(product_id)

    def question_8(self, fulfillment_status='fulfilled'):
        '''
        This function finds out the customer with highest AOV

        - Note: the function calculates the revenue only on the "fulfilled" orders.
                If we want the revenue to be calculated on all orders, we can simply
                change the "fulfillment_status" argument.
        '''

        base_df = self.data.orders
        if fulfillment_status=='fulfilled':
            base_df = base_df[base_df['fulfillment_status']=='fulfilled']

        customers_AOV = base_df.groupby(['customer_id'])['order_revenue'].mean()

        print("The customer with id %d has the maximum AOV of %.2f" %(customers_AOV.idxmax(),customers_AOV.max()))


    def question_9(self, fulfillment_status='fulfilled', date_interval_1=['2019-12-01','2019-12-30'], date_interval_2=['2020-01-01','2020-01-31']):
        '''
        This function returns the 3 products that grew most in revenue in the specified period

        - Note: the function calculates the revenue only on the "fulfilled" orders.
                If we want the revenue to be calculated on all orders, we can simply
                change the "fulfillment_status" argument.
        '''

        base_df = self.data.orders
        if fulfillment_status=='fulfilled':
            base_df = base_df[base_df['fulfillment_status']=='fulfilled']

        product_interval_1 = base_df[(base_df['processed_at'] > date_interval_1[0]) & (base_df['processed_at'] < date_interval_1[1])].groupby(['product_id'])['order_revenue'].sum()
        product_interval_2 = base_df[(base_df['processed_at'] > date_interval_2[0]) & (base_df['processed_at'] < date_interval_2[1])].groupby(['product_id'])['order_revenue'].sum()

        idx = product_interval_1.index.intersection(product_interval_2.index)
        conct_df = pd.concat([product_interval_1.loc[idx].rename('Revenue_1'),product_interval_2.loc[idx].rename('Revenue_2')],axis=1)
        conct_df['growth'] = (conct_df['Revenue_2']-conct_df['Revenue_1'])/conct_df['Revenue_1']
        most_growing_products = conct_df.sort_values(by='growth', ascending=False).iloc[0:3]


        print("The 3 ost growing products in intervals %s to %s are:\n" %(date_interval_1,date_interval_2))
        for product_id in most_growing_products.index:
            print(product_id)



    def question_10(self):
        '''
        This function analyzes previous orders and ranks products based on
        what it assumes to be most-suited to new customers.

        - Note: For this basic "recommendation" system, we only use frequency 
                of the purchased products in the first orders. 
                Obviously, more complicated scenarios can be designed as well, i.e.
                taking into account the season, the price range, etc.
        '''

        base_df = self.data.orders.sort_values(by='processed_at')
        first_orders_df = base_df.groupby(['customer_id']).first()
        ranked_products = first_orders_df.groupby(['product_id'])['quantity'].sum().sort_values(ascending=False)

        return list(ranked_products.index),(ranked_products/sum(ranked_products)).values

