import googletrans

while True:

    task = input('번역할 문장을 입력하세요: ')

    if task == "끝":
        break

    trans = googletrans.Translator() # 구글 번역 객체 생성
    result1 = trans.translate(task, dest="en")
    result2 = trans.translate(task, dest="ja")
    result3 = trans.translate(task, dest="fr")

    # print(googletrans.LANGUAGES) 번역 언어의 destination 약자 찾기
    print(result1.text)
    print(result2.text)
    print(result3.text)
