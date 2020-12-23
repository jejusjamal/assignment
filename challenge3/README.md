# get-nested-kv

## What it does
- Will interate though the given nested object dictionary and return the value. 
- Retrieve the value of a particular data key.
- Eg. 
```
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a
```

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
- Open the `assignment` folder
  - `cd assignment/challenge3`
- Run whichever script you need:
  - `python3 get_nested_kv.py (provide the inputs in the file before running)`
- Unit test cases have been written to test the different inputs and outputs, you can execute them with below command.
  - `python -m unittest test_get_nested_kv.py`



