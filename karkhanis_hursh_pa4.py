answer = 0
for x in range (1, 101):
    answer += 1/x
answer = round(answer, 5)
print(answer)

scores_list = []
#get scores
for x in range(10):
    user_input= input("enter score: ")
    scores_list.append((int(user_input)))


#calculate avg before and print
average_before = int(sum(scores_list))/int(len(scores_list))
print ("average before removing lowest value: ", round(average_before,2))

#remove lowest value
scores_list.remove(min(scores_list))

#calculate avg after and print
average_after = int(sum(scores_list))/int(len(scores_list))
print ("average after removing lowest value: ", round(average_after, 2))


#not sure about problem 3, but this is my logic:
keep_going = True
print("enter student's test scores here.")
print("press 'x' to change student")
print("press 'q' to end program")
print("-------------------------")
#list for scores of the current student
current_student_scores = []

while keep_going == True:
    current_input = input("enter score here: ")
    if (current_input == 'x'):
        student_average = int(sum(current_student_scores))/int(len(current_student_scores))
        print("student average: ", student_average)
        current_student_scores.clear()
        #print currnt student averages and move on to new student
    else:
        if(current_input == 'q'):
            #exit loop
            keep_going = False
        else:
            #add score to current student
            current_student_scores.append(current_input)

    

    



