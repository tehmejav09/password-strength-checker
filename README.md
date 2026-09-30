# Password Strength Checker

A small Python tool that scores a password from 0 to 5 and explains
why it's weak or strong, instead of just saying pass or fail.

## What it does

- Checks the password's length
- Checks how many types of characters it mixes (lowercase, uppercase,
  numbers, symbols)
- Checks it against a short list of extremely common passwords
- Prints a score and the reasons behind it

## How to run it

    python3 password_checker.py

You'll be asked to type a password, then it prints something like:

    Score: 5/5 (Very strong)
    Why:
      - Good length (12 or more characters).
      - Mixes multiple character types (letters, numbers, symbols).

## Why I built it

Part of a series of small security projects on Cipherora
(cipherora.com), where I write up what I built, what broke, and what
I learned.
