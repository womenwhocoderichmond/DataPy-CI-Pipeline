import sys
import boto3


def main():
    args_len = len(sys.argv)
    if args_len < 3:
        print('Usage: hello_boto.py <bucket_name> <object_name>.')
    else:
        s3 = boto3.resource('s3')
        bucket_name = sys.argv[1]
        object_name = sys.argv[2]

        with open(object_name, 'rb') as object_file:
            try:
                response = s3.Object(bucket_name, object_name).put(Body=object_file)
                print(response)
            except Exception as error:
                print(error)


if __name__ == '__main__':
    main()
