# Install
```
virtualenv -p $(which python3) .
source bin/activate
pip install -r requirements.txt
```

# Run

```
source bin/activate
python topsubreddits.py
python stylesheets.py
zip "stylesheets-$(date +%Y-%m-%dT%H-%M-%S).zip" stylesheets/*.css
```
