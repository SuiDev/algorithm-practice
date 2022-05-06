## 実行例

### コンテナを作成する
```
docker-compose up -d --build
```

### Pythonファイルを実行する
```
docker-compose exec python python (ファイルパス)
ex) docker-compose exec python python /src/number/prime_number.py
```
