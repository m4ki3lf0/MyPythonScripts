
# Captcha Defeater

Here is my Captcha Defeater. Need to bypass any captcha for any reason ? Well here you are ! 

![alt text](https://github.com/m4ki3lf0/MyPythonScripts/blob/main/captcha_defeater/captcha_defeater.png)

## Context
During my studies in Cyber Security studies, one of our class was called entrepreneurship and we needed to successfully manage to have a very large amount of endorsers. We tried contacting the federation of that career path.
Unfortunately, we had 0 answer from them. So, I found a website from which we could found the entire list of email of that profession but we could only make 10 researchers per account.

To lazy to create 156 account manually, I made a bot that would create the account, validate the captcha, then use the PHPSESSID cookie to retrieve the email with python requests library.

You can find in this respository the python code I wrote to bypass de recaptcha.


## Installation

In order for the project to work you have to work with Chrome and Chromedriver from the same version (must be in PATH). 
It is also possible to use it with Firefox, Chrome, Edge and so on but you have to modify the source code.

```bash
    pip install selenium
    pip install requests
    pip install BeautifulSoup
```

## Deployment

To deploy this project modify the API_KEY value for 2captcha in captcha_defeater.py to match yours then run :

```bash
  python3 captcha_defeater.py
```
## Lessons Learned

- I learned how to use selenium
- I revised my regex and learned other ways to match information with bs4. 
## Optimizations

YES ! For real there is always way to improve and if you have any recommendation you can contact me.
## Project Idea

- Instagram unfollow bot

## Authors

- [@m4ki3fl0](https://www.github.com/m4ki3lf0)


## License


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)[MIT](https://choosealicense.com/licenses/mit/)
## Badges


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


