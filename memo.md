## やりたいこと
### __DONE__ docker上で動画撮影
 - エラー
    > エラーは出るが、画像・動画は作成できているみたい。。  
    ```
    mmal: mmal_vc_shm_init: could not initialize vc shared memory service
    mmal: mmal_vc_component_create: failed to initialise shm for 'vc.camera_info' (7:EIO)
    mmal: mmal_component_create_core: could not create component 'vc.camera_info' (7)
    mmal: Failed to create camera_info component
    ```
### YouTube動画アップロード コマンドライン
 - https://qiita.com/ny7760/items/5a728fd9e7b40588237c
 - 認証情報
    ```
    # クライアントID
    151096037528-h4vrlqsipl1flqbq9scuqplt44lgqgt0.apps.googleusercontent.com

    # クライアントシークレット
    x7z5nw57Y_4g1SEdTH5W8k9d
    ```

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
 >  docker-compose.yml があるディレクトリで実行する  
 ```
 sudo docker-compose up
 ```

### Dokcer上からカメラを扱う
 - https://qiita.com/yuyakato/items/f5c2c86754a5b1c9504d