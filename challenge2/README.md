# get-ec2-metadata

## What it does
- Query the metadata of an ec2 instance within AWS and provide a json formatted output. 
- Retrieve the value of a particular data key.

## How to install
- [Create an EC2 Linux instance on AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [SSH into the instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
- Install Python 3 and git on your instance 
    - `sudo yum install python3 git`
- Clone this repository
  - `git clone https://github.com/jejusjamal/assignment`
- Install pipenv
  - `sudo pip3 install pipenv`
- Open the repository on your instance
  - `cd assignment`
- Install project dependancies
  - `pipenv install`


## How to run
- Open the `challenge2` folder
- Run whichever script you need:
  - `python3 get_ec2_metadata.py`
  - `in the prompt it will display metadata in json format and will ask you to fetch the key, input the key you wanted to find eg. instance-id

## How it works
- It makes use boto library to fetch the metadata
- See [AWS user guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) for more info on the instance metadata API.
