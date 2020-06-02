"""
http://openaq-data.s3.amazonaws.com/index.html
"""
import boto3
import os
os.environ['HOME']=r'C:\prog'

boto3.set_stream_logger('botocore', level='DEBUG')

s3 = boto3.client('s3')
s3.download_file('openaq-data', '2018-04-04.csv', r'c:\prog\out\test.csv')
