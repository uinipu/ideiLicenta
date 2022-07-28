import pyttsx3
import easyocr

ts = pyttsx3.init()
reader = easyocr.Reader(['en'])

results = reader.readtext("C:/Users/RaulB/Downloads/naproza.jpeg")
read = [""]
for word in results:
    if len(word) == 6:
        (one, two, three, four, important, six) = word
    elif len(word) == 5:
        (one, two, three, important, six) = word
    elif len(word) == 4:
        (one, two, important, six) = word
    elif len(word) == 3:
        (one, important, six) = word
    read.append(important)
print(results)
ts.say(read)
ts.runAndWait()