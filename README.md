# AWS Cognito users iterator

### Requirements
1. Python3.8
2. AWS CLI
2. You need to have set valid credentials for AWS to have access to your user pool. This is usually done by running `aws configure` command.

### Warning for users which have multiple Python versions
Be sure to run this script with Python3.8.
If you want to specify Python version, try `python3.8` command instead of `python`

### Usage
1. Run `pip install -r requirements.txt` to install all dependencies
2. Create `.env` file in the root folder
3. Add `USER_POOL_ID` key with a valid value
4. run `python __init__.py`
