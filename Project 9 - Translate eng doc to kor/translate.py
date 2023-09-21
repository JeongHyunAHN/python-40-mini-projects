import googletrans

translator = googletrans.Translator()

str1 = "행복하세요"
result = translator.translate(str1, dest='en', src='auto')
print(f"행복하세요 => {result.text}")