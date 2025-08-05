# race_laptime_tracker

Hokuyo 2D LiDARを使用したRCカーレース向けのラップタイム計測システムです。

![画面](doc/screen.png)

---

## ✅ 概要

#### 機能
- 1周あたりのラップタイムを計測
- Web上のUIページにタイムをランキング形式で表示
- 再起動後もデータを保持
#### UI表示項目
- 走行中の経過タイム
- 過去のラップタイム一覧
- 日時
- ドライバー名（UI上で編集可能）
- 削除ボタン

---

## 🔧 動作環境

- Ubuntu 22.04
- ROS 2 Humble
- Hokuyo URG (UST-20LX)

---

## 🖥️ 使用技術

#### バックエンド (pixkit_dashboard.py)
- Flask
- SocketIO
#### フロントエンド (index.html)
- HTML/CSS/JavaScript
- Socket.IO

---

## 📦 インストール

```bash
cd ~/ros2_ws/src

# 本リポジトリを追加
git clone https://github.com/iASL-Gifu/race_laptime_tracker.git

mkdir hokuyo_urg

cd hokuyo_urg/

# LiDARドライバを追加
git clone https://github.com/ros-drivers/urg_node.git -b ros2-devel
git clone https://github.com/ros/diagnostics.git -b ros2
git clone https://github.com/ros-perception/laser_proc.git -b ros2-devel
git clone https://github.com/ros-drivers/urg_c.git -b ros2-devel
git clone https://github.com/ros-drivers/urg_node_msgs.git -b master

cd ~/ros2_ws

colcon build
```

---

## 🚀 起動方法

### 1. 接続
- LiDARをPCに接続する。

### 2. プログラムの実行
#### ターミナル1
```bash
source install/setup.bash
ros2 run urg_node urg_node_driver --ros-args -p ip_address:="192.168.0.10"
```
#### ターミナル2
```bash
source install/setup.bash
ros2 run laser_processor laser_processor
```
#### ターミナル3
```bash
source install/setup.bash
ros2 run lap_recorder lap_timer_node
```
#### ターミナル4
```bash
source install/setup.bash
ros2 run lap_recorder web_publisher_node
```
#### ターミナル5
```bash
python3 ~/ros2_ws/src/race_laptime_tracker/laptime_webui/laptime_webui/app.py
```

### 3. UIページの起動
- Webブラウザで `localhost:5000` にアクセスする。

---

## 💡 トラブルシューティング



---

## ⚙ オプション設定とカスタマイズ



---

## 👤 開発者

#### 岐阜大学 工学部 アレックス研究室 (iASL)
- Site: https://www.iasl.info.gifu-u.ac.jp/  
- Github: https://github.com/iASL-Gifu/

---

## ライセンス

本プロジェクトは Apache License 2.0 の下でライセンスされています。  
詳細は [LICENSE](./LICENSE) ファイルをご覧ください。

### Apache License 2.0（概要）

このライセンスの下では、以下のことが許可されています：

- 商用利用
- 修正
- 配布
- 特許使用
- 私的使用

ただし、以下の義務があります：

- 元のライセンス文の保持（著作権表示とライセンスの明記）
- 改変の有無を記載
- 商標の使用制限

このライセンスは「現状のまま（AS IS）」で提供されており、  
いかなる保証もなく、作者は一切の責任を負いません。

