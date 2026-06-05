import boto3

redshift = boto3.client(
    'redshift',
    region_name='us-east-1'
)

response = redshift.create_cluster(
    ClusterIdentifier='telecom-redshift',
    DBName='telecom_dw',
    MasterUsername='admin',
    MasterUserPassword='123456789',
    NodeType='dc2.large',
    ClusterType='single-node',
    IamRoles=[
        'arn:aws:iam::050451400118:role/redshift-s3-role'
    ],
    PubliclyAccessible=True
)

print("Cluster creation started")