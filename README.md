# Text in a bottle

text-in-a-bottle is a fast webapp made in Python to create and share text or code snippets. For now it supports basic text creation and sharing.


## TODO

- Rate limiter
- code fomatting (maybe??)
- curl support

## Development

Clone the repo, install the `requirements.txt` via pip and run `app.py`. For database access, create a new collection named `txtbottle`

### Env variable

Create a file `.env` in your root project folder and only put the db secrect like so:

```
FAUNA_SECRET='YOURKEYHERE'
```

You also might need to change the db request domain in line #18 of `app.py` if you chose anything another than US as the db server.
