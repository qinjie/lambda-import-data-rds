import csv
from sqlalchemy import create_engine, types
import pandas as pd
import boto3
import pymysql

pymysql.install_as_MySQLdb()

s3_client = boto3.client('s3')


def read_data_from_s3(event):
    """
    Read CSV file content from S3 bucket
    """
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]
    resp = s3_cient.get_object(Bucket=bucket_name, Key=s3_file_name)

    data = resp['Body'].read().decode('utf-8')
    data = data.split("\n")
    return data


def lambda_handler(event, context):
    """
    Main handler
    """
    # csv_file = 'MOCK_DATA.csv'
    csv_file = 's3://temp-460453255610/MOCK_DATA.csv'
    rds_endpoint = "database-3.cluster-c3bottoj4h9o.ap-southeast-1.rds.amazonaws.com"
    username = "admin"
    password = "Qwer!234"  # RDS mysql password
    db_name = "dev"  # RDS db name
    table_name = "test"  # RDS table name

    # enter your password and database names here
    conn_str = f'mysql://{username}:{password}@{rds_endpoint}/{db_name}'
    engine = create_engine(conn_str)

    # Replace Excel_file_name with your excel sheet name
    df = pd.read_csv(csv_file, sep=',',
                     quotechar='\'', encoding='utf8')

    # Replace Table_name with your sql table name
    response = df.to_sql(table_name, con=engine,
                         index=False, if_exists='append')
    print(response)

    return {"count": response}
