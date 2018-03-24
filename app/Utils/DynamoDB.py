import boto3


from app.Utils.Credentials import Creds
session = boto3.Session(
            aws_access_key_id= Creds.getkey(),
            aws_secret_access_key=Creds.getsecret(),
            region_name=Creds.getregion()
        )

dynamodb = session.client('dynamodb')
users_table = "Users"
#dynamodb.put_item(TableName=users_table, Item={'email_id': {'S': "email"}, 'password': {'S': "password"}})


class DynamoDB:
    def __init__(self):
        self.data = []

    def putUser(self, email, password):
        item = {
                'email_id': {'S': email},
                'first_name': {'S': email},
                'password': {'S': password},
                'age': {'N': '20'}
            }
        response = dynamodb.put_item(
            TableName=users_table,
            Item= item
        )

        return response

        #dynamodb.put_item(TableName=users_table, Item={'user': {'S': email}, 'password': {'S': password}})
