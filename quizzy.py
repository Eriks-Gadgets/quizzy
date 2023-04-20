#Quizzy
#(c) Erik's Gadgets
print("Quizzy Event Log")

import PySimpleGUI as sg

sg.theme("DarkPurple4")

sg.Popup("Quizzy\n(c) 2023 Erik's Gadgets")

quizzy_config = sg.Window(title="QUESTION CONFIGURATION", layout=[[sg.Text("QUESTION"), sg.Input(), sg.Button("OK")]])

menu = 0
incorrect = 0
acorrect = 0
answerarray = ["A","B","C","D"]
while True:
    event, values = quizzy_config.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "SUBMIT ANSWER":
        for i in range(0, 3):
            if values[i] == True:
                answer = i
                if answerarray[answer] == correct:
                    acorrect += 1
                else:
                    incorrect += 1
                break
        quizzy_config.close()
        quizzy_config = sg.Window(title=titley, layout=[[sg.Text(question)], [sg.Radio("A", "Answer"), sg.Text(a)],[sg.Radio("B", "Answer"), sg.Text(b)],[sg.Radio("C", "Answer"), sg.Text(c)],[sg.Radio("D", "Answer"), sg.Text(d)], [sg.Button("SUBMIT ANSWER"), sg.Button("STOP")]])
    elif event == "STOP":
        quizzy_config.close()
        sg.Popup(str(acorrect + incorrect) + " answers recieved.")
        sumar = (incorrect + acorrect)
        sg.Popup(str(round(acorrect / sumar * 100,2)) + "% of the answers were Correct.")
    elif event == "OK":
        if menu == 0:
            question = values[0]
            menu = 1
            quizzy_config.close()
            quizzy_config = sg.Window(title="ANSWER CONFIGURATION", layout=[[sg.Text("A"), sg.Input()],[sg.Text("B"), sg.Input()],[sg.Text("C"), sg.Input()],[sg.Text("D"), sg.Input()],[sg.Button("OK")]])
        elif menu == 3:
            menu = 4
            titley = values[0]
            quizzy_config.close()
            quizzy_config = sg.Window(title=titley, layout=[[sg.Text(question)], [sg.Radio("A", "Answer"), sg.Text(a)],[sg.Radio("B", "Answer"), sg.Text(b)],[sg.Radio("C", "Answer"), sg.Text(c)],[sg.Radio("D", "Answer"), sg.Text(d)], [sg.Button("SUBMIT ANSWER"), sg.Button("STOP")]])
        elif menu == 1:
            a = values[0]
            b = values[1]
            c = values[2]
            d = values[3]
            menu = 2
            quizzy_config.close()
            quizzy_config = sg.Window(title="CORRECT ANSWER CONFIGURATION", layout=[[sg.Text("CORRECT ANSWER CONFIGURATION")], [sg.Text("~~~~~~~~~~~~~~~")], [sg.Text(question)],[sg.Button("A"), sg.Text(a)],[sg.Button("B"), sg.Text(b)],[sg.Button("C"), sg.Text(c)],[sg.Button("D"), sg.Text(d)]])
    elif event == "A" or event == "B" or event == "C" or event == "D":
        if menu == 2:
            correct = event
            quizzy_config.close()
            menu = 3
            quizzy_config = sg.Window(title="TITLE CONFIGURATION", layout=[[sg.Input(),sg.Button("OK")]])
quizzy_config.close()
