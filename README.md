# NintendoSwitch

## Overview
This application(bot) checks Nintendo Online Store whether Nintendo Switch is availabel.
If Switch is on sale, notify you by LINE.
This bot access the web page every `N` sec. 
Lower `N` will allow more accurate stock analyses, but you should be aware that frequent access will overload the web server.
Default `N` is  30.



## 概要
Nintendoオンラインストアにアクセスし、Switchの在庫があるかを確認するボットです。在庫が確認できれば、LINEで通知します。
`N`秒おきにオンラインストアにアクセスします。`N`が小さいほどより頻繁にストアにアクセスすることになり、より正確に在庫状況を知ることができます。
しかし、あまりに小さくすると、それはF5攻撃のようなものになって良くありません。`N = 30`程度が推奨されます。
