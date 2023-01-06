# Lambda Import Data into RDS

This lambda function reads a CSV file and import it into RDS table.

Since Lambda function must be deployed in a VPC, the VPC must create a VPC endpoint (Gateway) to S3 service.

Pandas now support read from csv file in S3 bucket. But need to have s3fs library install.
