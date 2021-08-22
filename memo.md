## やりたいこと
### docker上で動画撮影
### YouTube動画アップロード コマンドライン

## メモ
### ラズパイ上にDokcer環境を構築
 - https://qiita.com/k_ken/items/0f2d6af2618618982723
    ```
    curl -sSL https://get.docker.com | sh
    sudo pip3 install docker-compose
    ```

    - pip3はインストールされていない場合がある？
        > その場合は個別にインストールが必要。

        ```
        sudo apt-get -y install python3-pip
        ```

 - コンテナの起動
 ```
 # docker-compose.yml があるディレクトリで実行する
 sudo docker-compose up
 ```

### Dokcer上からカメラを扱う
 - https://qiita.com/yuyakato/items/f5c2c86754a5b1c9504d