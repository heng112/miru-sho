## スクレイピングサイト

### 将棋DB2 
https://shogidb2.com/



### 棋士別

https://shogidb2.com/player/

- 例
``` 
https://shogidb2.com/player/%E8%97%A4%E4%BA%95%E8%81%A1%E5%A4%AA
```

## 環境構築

```
docker-compose up -d

docker-compose exec dev_mirusho bash
```

### ファイル実行
```
poetry run python main.py

poetry run python sheet.py
```


### 依存関係の更新
```
poetry install
```


### ライブラリ追加
```
poetry add [ライブラリ名]
```
