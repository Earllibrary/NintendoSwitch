# NintendoSwitch

## Overview
This application(bot) checks Nintendo Online Store whether Nintendo Switch is availabel.
If Switch is on sale, notify you by LINE.
This bot access the web page every `N` sec. 
Lower `N` will allow more accurate stock analyses, but you should be aware that frequent access will overload the web server.
Default `N` is  30.

## Dependences
- Python 3.x

## Usage
Before you run the bot, you must get **token** for notification via LINE.  
Registar and get **token** from URL below.  
https://notify-bot.line.me/

Your **token** will be represented like `yourToken = gda73Gyhkxxxxxxxxxxxxxxx`

Then replace `yourToken` with **your own token** in the `SOLDOUT.py`

Now, get ready for running.

Bot will begin scraping with
    
    $python SOLDOUT.py


### Note

- If your Python version is `2.x`, replace all the word `"subprocess"` to `"commands"` in `SOLDOUT.py`.  
`"commands"` is no more supported after Python 3.x.

- You can change `N` parameter to adjust the frequency of access.  
Default frequency is `N = 30` sec.

## 概要
Nintendoオンラインストアにアクセスし、Switchの在庫があるかを確認するボットです。在庫が確認できれば、LINEで通知します。
`N`秒おきにオンラインストアにアクセスします。`N`が小さいほどより頻繁にストアにアクセスすることになり、より正確に在庫状況を知ることができます。
しかし、あまりに小さくすると、それはF5攻撃のようなものになって良くありません。`N = 30`程度が推奨されます。

## 環境
Python 3.x
