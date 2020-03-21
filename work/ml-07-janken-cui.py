# -*- coding: utf-8 -*-

import numpy as np
from sklearn.neural_network import MLPClassifier

# じゃんけんの手のベクトル
janken_array = (
    [1, 0, 0],  # グー
    [0, 1, 0],  # チョキ
    [0, 0, 1]   # パー
)

# じゃんけんの手の名称
janken_class = ['グー', 'チョキ', 'パー']

# 過去の手の何回までを記憶するか
n = 3

# じゃんけんの過去の手の初期化
# 過去の手を何回まで記憶するか（3） * 人間とコンピュータ（2） * グー・チョキ・パー（3）
Jprev = np.zeros(3 * n * 2)

# 過去の手（ベクトル形式）をランダムに初期化
for i in range(2 * n):
    j = np.random.randint(0, 3)
    Jprev[3*i: 3*i+3] = janken_array[j]

# 現在の手（0-2の整数）をランダムに初期化
j = np.random.randint(0, 3)

# 過去の手（入力データ）をscikit-learn用の配列に変換
Jprev_set = np.array([Jprev])

# 現在の手（ターゲット）をscikit-learn用の配列に変換
jnow_set = np.array([j])

# ３層ニューラルネットワークの定義
clf = MLPClassifier(hidden_layer_size=(200, ), random_state=None)

# ランダムな入力でオンライン学習を1回行う
# classesは、あり得るターゲットを指定する
clf.partial_fit(Jprev_set, jnow_set, classes=[0, 1, 2])

print('1: グー、2: チョキ、3: パー')

win = 0
draw = 0
lose = 0

try:
    while True:
        try:
            # 入力された手を0-2へ変換する
            j = int(input()) - 1
        except(SyntaxError, NameError, UnicodeDecodeError, ValueError):
            # 例外が発生した場合は再度入力させる
            continue
        # 入力が0-2でなければ再度入力させる
        if j < 0 or j > 2:
            continue

        # じゃんけんの手をnp.array形式へ変換
        Jprev_set = np.array([Jprev])
        jnow_set = np.array([j])

        # コンピューターが、過去の手から人間の現在の手を予測
        jpredict = clf.predict(Jprev_set)

        # 人間の手
        your_choice = j

        # コンピューターの予測の手
        # 人間の手を予測しているため、グーならパー、チョキならグー、パーならチョキへ変換する
        comp_choice = (jpredict[0] + 2) % 3

        # 勝敗結果を表示
        print('あなたの勝ち： {0}、負け：{1}、あいこ：{2}'.format(win, lose, draw))

        # 過去の手（入力データ）と現在の手（ターゲット）でインライン学習
        clf.partial_fit(Jprev_set, jnow_set)

        # 過去の手の末尾に現在のコンピュータの手を追加
        Jprev = np.append(Jprev[3:], janken_array[comp_choice])

        # 過去の手の末尾に人間の手を追加
        Jprev = np.append(Jprev[3:], janken_array[your_choice])

except KeyboardInterrupt:
    pass