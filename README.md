# TeleAWS

This package implements method for interaction with Telegram and AWS APIs.

## Build
```bash
git clone <repo_url>
cd teleaws
python -m build
```
## Installation
Install the `whl` file via `pip`

```bash
pip install dist/teleaws-*.whl
```

## Usage

```python
from teleaws.tg.bot import Bot

chatid = 12346789
text = "Hello world!"
bot = Bot("<token>")
bot.send_message(chatid, text)
```
