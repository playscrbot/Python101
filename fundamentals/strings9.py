data = "John,25,Billing"
parts = data.split(",")

sentence = “Hello, John!”
words = sentence.split(“,”)
print(words)

sentence = "Python makes boring work easier"
words = sentence.split()
print(words)

words = [“Hello,”, “John!”, "Python", "makes", "work", "easier"]
sentence = " ".join(words)
print(sentence)