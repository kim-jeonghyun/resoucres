# boto3 
 AWS SDK for Python (Boto3) which help to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3)

## documentation
- [Uploading files](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html)
- [Download files](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html)

## Environments
- python: 3.9.12
- python-dotenv: 0.21.0
- boto3: 1.24.89

## Install
```shell
$ pip install -r requirements.txt
```

## Run

Please create an .env file in the root directory of your project.

And then write like below.
```
AWS_ACCESS_KEY_ID=Input your access key id here!
AWS_SECRET_ACCESS_KEY=Input your secret access key here!
```

And run upload_to_s3.py!
```shell
$ python upload_to_s3.py
```

You can see the file on S3 like below:

![Uploaded file](./screenshots/uploaded_file.png)

And run download_from_s3.py!
```shell
$ python download_from_s3.py
```

You can see the file 'hello_world_from_s3.txt' on your directory.
