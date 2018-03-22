# Switch_notify_me

## Overview
This bot checks Nintendo Online Store whether Nintendo Switch is availabel.
If Switch is on sale, it notifies you by LINE.


## Dependences
- Python 3.x

## Usage
Before you run the bot, you have to have **token** for notification via LINE.  
Please registar and get **token** from following URL:

https://notify-bot.line.me/

Your **token** will be represented like `yourToken = gda73GyhiYuiklJ8fJ983`

Then replace `yourToken` with **your own token** in the `SOLDOUT.py`

Now, get ready for running.

Bot will begin scraping with
    
    $python SOLDOUT.py


### Note

- If your Python version is `2.x`, replace all the word `"subprocess"` to `"commands"` in `SOLDOUT.py`.  
`"commands"` is no more supported after Python 3.x.

- You can change `N` parameter to adjust the frequency of access.  
Default frequency is `N = 30` sec.  
Lower `N` will allow more accurate stock analyses, but you should be aware that frequent access will overload the web server.


***
# Switch_notify_me(日本語)

## 概要
Nintendoオンラインストアにアクセスし、Switchの在庫があるかを確認するボットです。在庫が確認できれば、LINEで通知します。

## 環境
Python 3.x

## 使い方
まず、LINE通知するために必要なトークンなるものを取得します。  
LINEを使って通知を行うために、LINE NotifyというLINEが提供しているサービスを利用する必要があります。  
ここで、あなたが通知サービスを開発するためのキーが必要となります、それが**トークン**です。（便宜的にそのようなものだとしておきます）  

さて、このトークンの取得手続きは以下のリンクから行うことができます。

https://notify-bot.line.me/

登録が終わり、トークンが次のようなランダムな文字列の形式で表示されます。これをメモしてください。  

`yourToken = gda73GyhiYuiklJ8fJ983`

トークンは一度表示されたら二度と表示されないので、メモし損ねたらまた取得してください。  

ここで取得したトークンを、`SOLDOUT.py`中の`yourToken`に代入します。

これで準備ができました。

つぎのコマンドで動かします。

    $python SOLDOUT.py
    
## 備考
- `N` の値を小さくするほどより頻繁にアクセスするようになりますが、あまりに小さくするとF5攻撃のような、ある種のサービス妨害攻撃になりかねません。適切な調整をおねがいします。
- Python 2.x 系では`subprocess`が使えないので、代わりに`commands`パッケージを使います。  
`SOLDOUT.py`中の`subprocess`を`commands`で置換するだけで2.x系にも対応できるようになります。
