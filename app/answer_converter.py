import sys 
sys.path.insert(1, '/C:/Condom UROP/cross-checker.py')

from cross_checker import cross_check

question_nums = [1,4,9,15,20,23,26,32,36,42,48,64,71,77,83,89,95,101,107,113,120,200,207,212,216,222,230,237,241,245]

def answer_converter(old_or, old_and, output):
    new_or = []
    new_and = []
    new_output = int(output)

    print ("Old or" + old_or)
    print ("Old and" + old_and)

    ors = old_or.split(",")
    ands = old_and.split(",")

    for x in ors:
        if x == " " or x == "," or x == '':
            continue
        else:
            num = int(x)
            qnum = 1
            i = 0
            while i < len(question_nums):
                if question_nums[i] < num:
                    qnum = question_nums[i]
                else:
                    break
                i += 1
            new_or.append((qnum, num))
    if ands:
        for x in ands:
            if x == " " or x == "," or x == '':
                continue
            else:
                num = int(x)
                qnum = 1
                i = 0
                while i < len(question_nums):
                    if question_nums[i] < num:
                        qnum = question_nums[i]
                    else:
                        break
                
                    i += 1
                new_and.append((qnum, num))

    result = []
    result.append(new_or)
    if new_and:
        result.append(new_and)

    

    crossd = cross_check(result, new_output)
    
    results = crossd[1]
    total_number = crossd[2]

    answers = ["" for _ in range(100)]
    i=0

    for result_ in results:
        answers[i] = result_
        i += 1
    
    return (answers, total_number, old_or, old_and, output)



print (answer_converter("38,41", "72,73", "77"))








