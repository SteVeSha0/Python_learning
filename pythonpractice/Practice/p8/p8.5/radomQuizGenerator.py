'''
生成随机的测验试卷文件
1.创建35份不同的测验试卷
2.为每份试卷创建50个多重选择题，次序随机
3.为每个问题提供一个正确答案和3个随机错误答案，次序随机
4.将测验试卷写到35个文本文件中
5.将答案写到35个文本文件中
    代码要做的事情：
    1.将州和他们的首府保存在一个字典中。
    2.针对测验文本文件和答案文本文件，调用open()、write()和close()
    3.利用radom.shuffle()随机调整问题和多重选项的次序
'''

#! python3

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'SPringfield', 
            'Indiana':'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 
            'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 
            'Michigan':'Lansing', 'Minnesota':'Saint paul', 'Mississippi':'Jackson', 'Missouri':'Jefferson City', 
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 
            'New Jersey': 'Trenton', 'New Mexico':'Santa Fe', 'New York': 'Albany', 'North Carolina':'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon':'Salem', 
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'providence','South Carolina': 'Columbia', 
            'South Dakota': 'pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    #  Create the quiz and answer key files.
    quizFile = open('Capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFlie = open('Capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    
    #  Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #  Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO : Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]

        wrongAnwers = list(capitals.values())

        del wrongAnwers[wrongAnwers.index(correctAnswer)]
        wrongAnwers = random.sample(wrongAnwers, 3)
        answerOptions = wrongAnwers + [correctAnswer]
        random.shuffle(answerOptions)
    #写入试卷
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s . %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        answerKeyFlie.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFlie.close()