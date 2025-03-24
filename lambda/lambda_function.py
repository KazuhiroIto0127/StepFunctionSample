def lambda_handler(event, context):
    input_name = event.get('name', 'World')
    message = f"Hello, {input_name} from AWS Lambda!"
    return {
        'statusCode': 200,
        'body': message
    }
