# 1)
# Given the jason file traverse through it and display the employee namd and corresponding project
#input is the data jason 
data = {
    "employees": [
        {
            "employee_id": 1,
            "name": "John Doe",
            "address": {
                "street": "123 Main St",
                "city": "Springfield",
                "state": "IL",
                "postal_code": "62701"
            },
            "skills": ["Python", "Spark", "SQL"],
            "projects": [
                {
                    "project_id": 101,
                    "project_name": "Data Pipeline",
                    "status": "completed"
                },
                {
                    "project_id": 102,
                    "project_name": "Data Lake",
                    "status": "ongoing"
                }
            ]
        },
        {
            "employee_id": 2,
            "name": "Jane Smith",
            "address": {
                "street": "456 Market St",
                "city": "Metropolis",
                "state": "NY",
                "postal_code": "10001"
            },
            "skills": ["Java", "Hadoop", "Kafka"],
            "projects": [
                {
                    "project_id": 103,
                    "project_name": "Streaming Analytics",
                    "status": "completed"
                },
                {
                    "project_id": 104,
                    "project_name": "Cloud Migration",
                    "status": "ongoing"
                }
            ]
        }
    ]
}

# Solution
# Iterating through employees and their projects
for employee in data['employees']:
    print(f"Employee: {employee['name']}")
    for project in employee['projects']:
        print(f" - Project Name: {project['project_name']}, Status: {project['status']}")
    print()  # for better readability
	


# 2)


# WITH OrderedTransactions AS (
#     SELECT
#         transaction_id,
#         merchant_id,
#         credit_card_id,
#         amount,
#         transaction_timestamp,
#         LAG(transaction_timestamp) OVER (PARTITION BY merchant_id, credit_card_id, amount ORDER BY transaction_timestamp) AS prev_transaction_timestamp
#     FROM
#         transactions
# )
# SELECT
#     transaction_id,
#     merchant_id,
#     credit_card_id,
#     amount,
#     transaction_timestamp
# FROM
#     OrderedTransactions
# WHERE
#     prev_transaction_timestamp IS NULL -- First transaction in the partition
#     OR
#     (transaction_timestamp - INTERVAL '10' MINUTE) > prev_transaction_timestamp;


# 3)
# how to create a stored procedure
# # Answer
# CREATE PROCEDURE SelectAllCustomers @City nvarchar(30)
# AS
# SELECT * FROM Customers WHERE City = @City
# GO;