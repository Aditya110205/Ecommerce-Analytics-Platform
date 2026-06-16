from faker import Faker
import pandas as pd

fake = Faker()


def generate_customers(num_customers=100):

    customers = []

    for customer_id in range(1, num_customers + 1):

        customers.append(
            {
                "customer_id": customer_id,
                "name": fake.name(),
                "email": fake.email(),
                "city": fake.city()
            }
        )

    return pd.DataFrame(customers)


if __name__ == "__main__":

    df = generate_customers()

    print(df.head())