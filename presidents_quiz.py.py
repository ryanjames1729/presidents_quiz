import time, config, random
from robobrowser import RoboBrowser

stopwatch1 = time.ctime()
presidents = config.answer_list
questions = config.question_list
correct = [" "," "," "," "," "]
start =[0,0,0,0,0]
end = [1,1,1,1,1]

br = RoboBrowser()

for q in range(5):
    found = False
    n = 0
    random.shuffle(presidents)
    while (n < (len(presidents) - 1)) and not found:
        br.open(config.form_link)
        form = br.get_form()
        form['entry.1991125160'] = "Ava"  #Name
        if q == 0:
            form['entry.1842912509'] = presidents[n]  #Q1
        else:
            form['entry.1842912509'] = correct[0]
        if q == 1:
            form['entry.1693510977'] = presidents[n]  #Q2
        else:
            form['entry.1693510977'] = correct[1]
        if q == 2:
            form['entry.262002855'] = presidents[n]  #Q3
        else:
            form['entry.262002855'] = correct[2]
        if q == 3:
            form['entry.1369130152'] = presidents[n]  #Q4
        else:
            form['entry.1369130152'] = correct[3]
        if q > 3:
            form['entry.250722543'] = presidents[n]  #Q5
        else:
            form['entry.250722543'] = correct[4]

        br.submit_form(form)
        score = str(br.get_link(text = "View your score"))
        beg = score.index("<") + 9
        en = score.index("rel", beg)-2
        score = (score[beg:en])
        br.open(score)

        src = str(br.parsed())
        if q == 0:
            start[0] = int(src.index("Enter your name below:"))
            end[0] = int(src.index("Points received", start[0]))
            substring = src[start[q]:end[q]]
        if q > 0 and q < 4:
            start[q] = end[q-1] + 20
            end[q] = int(src.index("Points received", start[q]))
            substring = src[start[q]:end[q]]
        if q == 4:
            substring = src[end[q-1]:]

        try:
            index = substring.index("Incorrect")
        except ValueError:
            correct[q] = presidents[n]
            found = True
        n = n + 1

stopwatch2 = time.ctime()
print("Start: " + stopwatch1 + ", End: " + stopwatch2)
total_time = int(stopwatch2[14:16])*60 + int(stopwatch2[17:19]) - int(stopwatch1[14:16])*60 - int(stopwatch1[17:19])
print("That was fun. In the past " + str(total_time) + " seconds I learned the following:")
for n in range(5):
    print(questions[n])

quest = ""
while quest != "quit":
    quest = input("> ")
    try:
        find = questions.index(quest)
        print(correct[find])
    except ValueError:
        print("I don't know that yet. Let's try another question.")
