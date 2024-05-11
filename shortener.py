from flask import Flask, request, redirect
import secrets
import sqlite3
def shorten_url(long_url):
  # Generate a random, unique short code
  while True:
    short_code = secrets.token_hex(3)
    # Check if code already exists in database

    if not c.fetchone():
      break

  # Add mapping to database
  c.execute("INSERT INTO urls (long_url, short_url) VALUES (?, ?)", (long_url, short_code))
  conn.commit()

  return short_code
def redirect_to_long_url(short_code):
  # Fetch long URL from database based on short code
  c.execute("SELECT long_url FROM urls WHERE short_url = ?", (short_code,))
  long_url = c.fetchone()

  if long_url:
    return redirect(long_url[0])
  else:
    return "Invalid short code", 404
def handle_shorten():
  long_url = request.form['long_url']
  # Shorten URL and get short code
  short_code = shorten_url(long_url)
  return f"Shortened URL: http://127.0.0.1:5000/{short_code}"

if _name_ == '_main_':
  app.run(debug=True)
