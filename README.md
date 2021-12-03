# score

## ディレクトリ構成
```
Scoring/
       ├ src/
       ├ files/
       ├ saiten.xlsx
       └ score.py
```

- srcフォルダ
  - 採点用のinput.txtを格納するフォルダ
  - 命名規則: `input{index}.txt`
  - 例: `input1.txt` `input2.txt`
- filesフォルダ
  - moodleからダウンロードしたファイルを格納するフォルダ
- saiten.xlsx
  - 採点結果を入力する用のエクセルファイル
- score.py
  - 採点などを行うpythonファイル
  
## 実行方法

1. moodleから採点したいファイルをダウンロードする
2. `files/`ディレクトリを作成し、ダウンロードしたファイルを入れる
3. エディターの一括検索、置換機能を使いmalloc部分を自分の実行環境に書き換える
  - `s = (char *)malloc((size_t)(size.__pos + 1)*sizeof(char)); -> // s = (char *)malloc((size_t)(size.__pos + 1)*sizeof(char));`
  - `//s = (char *)malloc((size_t)(size + 1)*sizeof(char)); -> s = (char *)malloc((size_t)(size + 1)*sizeof(char));`
  - windowsや64bit linuxの場合は以上の検索置換を行えば良い。(コメントアウトではなく削除されている場合は対応していないので、要注意)
4. `score.py`の11,12行目を変更し、67行目の`rename_files()`のコメントアウトを外し（必要があれば）、71行目の`calc_score()`部分をコメントアウトする
5. `score.py`を実行して`files`に格納されているファイルが`学籍番号.c`の形になっていることを確認する。(moodleの仕様変更があった場合は上手くいかないかも)
6. `score.py`の67行目の`rename_files()`をコメントアウトし、71行目の`calc_score()`部分のコメントアウトを外す
7. 24~29行目のファイル名などを変更する
8. `src/`に入力用のテキストファイルを入れる(複数可能、命名規則に従うこと)
9. `score.py`を実行する
10. excelシートを確認すれば、実行結果が記入されているはず。errorになっていたり、何も記入されていないところは個別で動かして確認してください
