# osint-itms548
---

This is an OSINT Tool whose aim is to collect data from Twitter and Reddit using their provided API.

### How to use
To get this to work you need to install Python3.7. It wont work without it

Install requirements:
Run the following command:
```txt
pip install -r requirements.txt
```
Copy *hconfig-template.py* and rename it as *hconfig.py*. Modify the values as needed.


### How to run
Run `python app.py` (or `python3 app.py`) in your terminal
Go to ***localhost:5000***


### Twitter
##### Data collected from `Twitter`:
- ID
- Tweet Text
- Author ID
- Date/Time
- Hashtags
- Username

### Reddit
##### Data collected from `Reddit`:
- Post ID
- Username
- Subreddit
- Title
- No. of comments
- Date/Time
