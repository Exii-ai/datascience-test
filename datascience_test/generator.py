import pandas as pd
from data import Data


class Generator:
    def __init__(self):

        self.data = Data()

        # Removing duplicated orders, however, in production we need to remove
        # them in data preprocessing module instead of generator.
        self.data.orders.drop_duplicates(
            ["order_id", "product_id", "variant_id"], inplace=True
        )

        # Converting the data type of the processed_at variable. Similarly, in
        # production we need to remove them in data preprocessing module instead
        # of generator.
        self.data.orders["processed_at"] = pd.to_datetime(
            self.data.orders["processed_at"]
        )

        # Merging the orders & customers for future use in question 4, 8, and
        # 10.
        self.merged_data = self.data.orders.merge(
            self.data.customers.drop_duplicates(), on="order_id", validate="m:1"
        )

    def example(self):
        print("We have %s customers" % str(self.data.customers.customer_id.nunique()))

    def question_1(self, average=True):
        """If interested in the individually highest priced product_id set
        average=False function, otherwise to see the average highest priced
        product_id, set average=True (default)."""

        if average:
            return (
                self.data.orders.groupby(["product_id"])["price"]
                .mean()
                .nlargest(3)
                .index.values
            )
        else:
            return self.data.orders.nlargest(3, "price")["product_id"].values

    def question_2(self, criterion="order_revenue"):
        """Choose the criterion for the best selling vendors among price,
        quantitiy, item_spend, or order_revenue (default)."""

        return (
            self.data.orders.groupby(["vendor"])[criterion]
            .sum()
            .nlargest(3)
            .index.values
        )

    def question_3(self):
        """Returns the product_id with most variants."""

        return self.data.orders.groupby(["product_id"])["variant_id"].nunique().idxmax()

    def question_4(self):
        """Returns the product_id sold to the most unique customers."""

        return (
            self.merged_data.groupby(["product_id"])["customer_id"].nunique().idxmax()
        )

    def question_5(self):
        """Returns the worst performing day in terms of revenue."""

        return (
            self.data.orders.groupby(["processed_at"])["order_revenue"]
            .sum()
            .idxmin()
            .strftime("%Y-%m-%d")
        )

    def question_6(self):
        """Returns the order with the most discount to revenue ratio."""

        return (
            self.data.orders.groupby(["order_id"])["discount_amount"].sum()
            / self.data.orders.groupby(["order_id"])["order_revenue"].sum()
        ).idxmax()

    def question_7(self):
        """Returns the top 3 best selling product_id in December 2019 & March
        2020 regarding the revenue, respectively."""

        dec2019 = self.data.orders[
            (self.data.orders["processed_at"].dt.month == 12)
            & (self.data.orders["processed_at"].dt.year == 2019)
        ]
        mar2020 = self.data.orders[
            (self.data.orders["processed_at"].dt.month == 3)
            & (self.data.orders["processed_at"].dt.year == 2020)
        ]

        return (
            dec2019.groupby(["product_id"])["order_revenue"]
            .sum()
            .nlargest(3)
            .index.values,
            mar2020.groupby(["product_id"])["order_revenue"]
            .sum()
            .nlargest(3)
            .index.values,
        )

    def question_8(self):
        """Returns the customer_id with the largest AOV."""

        return (
            self.merged_data.groupby(["customer_id", "order_id"])["item_spend"]
            .sum()
            .groupby(["customer_id"])
            .mean()
            .idxmax()
        )

    def question_9(self):
        """Returns the 3 most growing product_id in terms of revenue from Dec
        2019 to Jan 2020."""

        first_last = (
            self.data.orders[
                self.data.orders["processed_at"].between("2019-12-01", "2020-01-31")
            ]
            .sort_values("processed_at")
            .groupby(["product_id"])["order_revenue"]
            .agg(["first", "last"])
        )

        return (first_last["last"] / first_last["first"]).nlargest(3).index.values

    def question_10(self):
        """Returns the ranking of products based on their appeal to new customers."""

        first_orders = (
            self.merged_data.sort_values("processed_at")
            .groupby(["customer_id"])["order_id"]
            .first()
        )
        first_orders_count = (
            self.merged_data[self.merged_data["order_id"].isin(first_orders)]
            .groupby(["product_id"])["order_id"]
            .count()
        )
        return first_orders_count.rank(method="min", ascending=False).sort_values()
