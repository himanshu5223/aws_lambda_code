import boto3
def lambda_handler(event, context):
    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource('dynamodb')
    # this will search for dynamoDB table
    # your table name may be different
    table = client.Table("task1_table")
    print(table.table_status)
    table.put_item(Item= {'Id': '10415210016','name':  'himanshu'})
    table.put_item(Item= {'Id': '10415210034','name':  'rahul'})
    table.put_item(Item= {'Id': '10415210004','name':  'kapil'})
    table.put_item(Item= {'Id': '10415210045','name':  'negi'})
    table.update_item(
        Key = {
            'Id' : '10415210016',
        }
    UpdateExpression='SET Age = :val1',
                     ExpressionAttributeValues={':val1': '6'})
    table.get_item(
        Key={
            'Id': '10415210016'
        })
    table.delete_item(
        Key = {
            'Id' : '10415210016'
        })