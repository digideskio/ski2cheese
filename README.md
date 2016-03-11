# 純粋関数型言語「さけるチーズ」
[裂けてるさけるチーズを裂けて避けるチーズが載ってる裂けてる地図を裂けて避けるチーズ](http://togetter.com/li/946530) のネタを元に、Lazy Kをベースに作った言語「さけるチーズ」とLazy Kとの相互翻訳器です。
詳しくは（ブログ記事URL）をご覧下さい。

## 使い方
Lazy Kからさけるチーズへ：

```
echo 'SKI' | python ski2cheese.py
# => 「「さけるチーズを避けるチーズ」と「裂けてるチーズ」と地図のある地、伊豆」
```

さけるチーズからLazy Kへ：

```
echo 'さけるチーズを避けるチーズ' | python cheese2ski.py
# => (K)
```

## 参考文献

- [http://togetter.com/li/946530](http://togetter.com/li/946530)
- [https://tromp.github.io/cl/lazy-k.html](https://tromp.github.io/cl/lazy-k.html) 
- [http://d.hatena.ne.jp/rst76/20121204/1354629448](http://d.hatena.ne.jp/rst76/20121204/1354629448)
- [http://blog.livedoor.jp/dankogai/archives/51524324.html](http://blog.livedoor.jp/dankogai/archives/51524324.html)
- [http://irori.hatenablog.com/entry/20130706/LazykPlayground](http://irori.hatenablog.com/entry/20130706/LazykPlayground)
- [http://lazy-k.appspot.com/](http://lazy-k.appspot.com/)
- [https://ja.wikipedia.org/wiki/Lazy_K](https://ja.wikipedia.org/wiki/Lazy_K)
- [https://en.wikipedia.org/wiki/Combinatory_logic](https://en.wikipedia.org/wiki/Combinatory_logic)
- [https://ja.wikipedia.org/wiki/B,C,K,W%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0](https://ja.wikipedia.org/wiki/B,C,K,W%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0)
- [http://ledyba.org/2012/07/03184840.php](http://ledyba.org/2012/07/03184840.php)
- [http://people.cs.uchicago.edu/~odonnell/Teacher/Lectures/Formal_Organization_of_Knowledge/Examples/combinator_calculus/](http://people.cs.uchicago.edu/~odonnell/Teacher/Lectures/Formal_Organization_of_Knowledge/Examples/combinator_calculus/)