import Chatbot.chatbot as Chatbot

chatter = Chatbot.Chatbot(build_console=True) #default: False

print("Hello, I am Mianbot.")

while True:
    raw = input()
    reply,confidence = chatter.testQuestionAnswering(raw)
    print("%s ,%d" % (reply,confidence))