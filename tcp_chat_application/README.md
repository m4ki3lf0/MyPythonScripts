
# tcp_chat_application

I made this project in order to better understand how socket worked. The next step of this project is to implement SSL so that everything we say is perfectly safe. 

After that, I would love to develop a command and control server with what i learned.


## Deployment

To deploy this project modify the IP address in client.py to match your server's one then run :

```bash
  python3 server.py
```

To connect the client run :
```bash
  python3 client.py
```
## Lessons Learned

Syncing server side and client side is not that easy. I am not a develloper only a cyber security student and this project allowed me to build something with what i've learned so far. I will push it further by implementing SSL.
## Optimizations

Meh, I did not optimize that much. I played with threading so that the server wouldn't block on receiving a message.


![alt text](https://github.com/m4ki3lf0/tcp_chat_application/blob/main/src/tcpChatApp.png)

## Roadmap

- Keep input at the bottom of the page clientside.

- SSL Implementation

- HTTPS Command & Control 

## Authors

- [@m4ki3fl0](https://www.github.com/m4ki3lf0)


## License


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[MIT](https://choosealicense.com/licenses/mit/)
## Badges
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

