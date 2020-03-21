
# cli-base-go (オミット)

- このディレクトリは調べた内容をWikiに移したら消し去ります。
- (またの機会にチャレンジしようかな)

## Goの環境構築手順 (TODO: あとでwikiリポジトリでまとめる)

---

### プロジェクトの作成方法

- mac

```bash
# go のインストールと確認
brew install go
which go

# 以下の`GO111MODULEをonにする`コマンドを実行するかログインシェルなどに記載しておく
export GO111MODULE=on

# go のパッケージ管理ファイルの初期化
go mod init
```
- 参考サイト
  - [【golang環境構築】Modulesでpackage管理をする \- Qiita](https://qiita.com/fox777/items/a8cb025df5439902b6c4)

### プロジェクトのディレクトリ構造

- [Golangプロジェクトのディレクトリ構成について考えてみた \- yyh\-gl's Tech Blog](https://yyh-gl.github.io/tech-blog/blog/go_project_template/)

### プロジェクトのディレクトリ構造

- [埋め込み型としての構造体 \( Goは継承を使わない \) \- Qiita](https://qiita.com/keiya01/items/435890473465a9b6c470)

---

## cli-baseの使い方

### 前提

- go コマンドが使用できること

### ビルド&実行

```bash
cd ./geranium/packages/common/cli-base/
go build

./CliBaseClass
```
