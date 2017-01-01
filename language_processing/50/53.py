#!/usr/bin/env python3
# coding: UTF-8

import os
import subprocess
import xml.etree.ElementTree as ET

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'

def parse_nlp():
    '''
    nlp.txtをStanford Core NLPで解析しxmlファイルへ出力
    すでに結果ファイルが存在する場合は実行しない
    '''
    if not os.path.exists(fname_parsed):
        # Stanford Core NLP実行、標準エラーはparse.outへ出力
        subprocess.run(
            'java -cp "/usr/local/lib/stanford-corenlp-full-2016-10-31/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + fname + ' 2>parse.out',
            shell=True,     # shellで実行
            check=True      # エラーチェックあり
        )

def main():
    # nlp.txtを解析
    parse_nlp()

    # 解析結果のxmlをパース
    root = ET.parse(fname_parsed)

    # wordのみ取り出し
    for word in root.iter('word'):
        print (word.txt)

if __name__ == '__main__':
    main()

