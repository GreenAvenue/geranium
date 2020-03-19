#!/bin/bash

# Note: 必ずBefore.shの前にセットで呼び指す
function after() {
	cd $execDir
  outputConsoleInfo "finish"
}

after
