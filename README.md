# Tamga multipage Flask site

## Run locally
```bash
pip install -r requirements.txt
python app.py
```

## Deploy on Render
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

## Important
- Replace the placeholder Telegram link in `app.py`:
  ```python
  TELEGRAM_LINK = 'https://t.me/'
  ```
- The contact form is currently visual only. In `contacts()` you can later connect real email sending.
