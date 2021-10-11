# Text in a bottle

text-in-a-bottle is a fast webapp made in Python to create and share text or code snippets. Made using Flask, MongoDB.

It also has a feature to create super fast web pages with Markdown Support. 

## TODO

- Rate limiter
- support for editing documents
- code fomatting (maybe??)
- curl support
- live markdown editing (done)

## Development

Clone the repo, install the `requirements.txt` via pip and run `app.py`. For database, collection name is `txt`.  

### Env variable

Create a file `.env` in your root project folder and only put the db secrect like below:

```
MONGO_URI='MongoURIHERE'
```

Uncomment the localhost connection section if you wish to test it in local mongodb server, which is preferred for development. I personally use Robo 3T to interface with mongodb servers (local/remote).
