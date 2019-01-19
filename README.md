# toitta

twitterのクローンを作りながら、

* クリーンアーキテクチャ
* Datastoreでのモデリング
* GAE 2nd Gen/Python3
* vuex

あたりを勉強する

# 実行方法

```
export DATASTORE_DATASET=local-gcp-dev
export DATASTORE_EMULATOR_HOST=localhost:8081
export DATASTORE_EMULATOR_HOST_PATH=localhost:8081/datastore
export DATASTORE_HOST=http://localhost:8081
export DATASTORE_PROJECT_ID=local-gcp-dev
gcloud auth application-default login
python main
```
