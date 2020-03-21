#!/bin/bash

# Note: 必ずafter.shとのあとにセットで呼び指す
function before() {
  # Note: どのディレクトリからの呼び出しであろうとも
  #       必ずスクリプトの存在するディレクトリでの実装扱いにする
  #       (Path周りの考慮を減らすため)
	readonly execDir=`pwd`
	readonly scriptDir=$(cd $(dirname $0); pwd)
	cd $scriptDir
  outputConsoleInfo "start"
}

before
