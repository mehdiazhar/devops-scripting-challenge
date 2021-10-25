# Scripting Challenge #

In this challenge you will be developing a script to extract details from an example git log. 

This challenge is intended to help us understand your scripting abilities and familiarity with git. 

If you are familiar with a scripting language other than python you are welcome to complete this challenge the language of your choice. 

You can spend as much time as you like completing this challenge, however we do not expect you to spend more than an hour.

### Setup ###

Before getting started, please read the instructions carefully and ensure you can execute the provided python script and both bash scripts.

### Challenge Description ###

You have been provided with two existing bash scripts that cannot be altered. 
The `gitlog-oneline.sh` file is to simulate a `git log --oneline` output.
The `release-add-tickets.sh` file is to simulate a potential automated way of adding ticket numbers to a release version.

Your task is to write a python script `test.py` to take output from the `gitlog-oneline.sh` script and process it to then provide input to the `release-add-tickets.sh` script. The input should be an incremented version number string and a list of the filtered ticket numbers.

#### Criteria ####
- Take output from the `gitlog-oneline.sh` command and process it
- Filter and find the appropriate ticket values
- Providing the filtered output to a new command


The list of tickets we want extracted should follow these rules:
- Each ticket number should only be listed once
- We only want the ticket numbers since the last merge

### Submitting ###

To submit this assessment please provide a link to a public repository with the commits you've made.

If you are unable to do this for any reason, feel free to email us with a zip of the entire repository including the .git directory.

Additional Questions

The following additional questions are to get a better insight into how you make software engineering decisions. 
We don't expect more than a short paragraph for each of these questions. 
Please include these questions as part of the submission readme or email:
1. Describe a way you could help protect against regression issues when the associated bash scripts are changed.
2. How would you recommend this python script be utilised?
3. Suggest an alternative approach to achieve a similar result as this script 
