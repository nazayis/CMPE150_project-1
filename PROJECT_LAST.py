## DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

# returns value of stress for given emotion (fear, worry or restlessness)
def return_value(given_emotion):
    value = 0
    if given_emotion == "NO":
        value = 0
    elif given_emotion == "MILD":
        value = 1
    elif given_emotion == "MODERATE":
        value = 2
    elif given_emotion == "SEVERE":
        value = 3
    return value

def compute_avg_stress():
    total_stress = 0
    for i in range(N):
        worry, restlessness, fear, gender = input().strip().split()
        total_stress += return_value(worry) + return_value(restlessness) + return_value(fear)
    stress_average = total_stress / N
    return stress_average

def compute_max_stress():
    maxvalue = 0
    for i in range(N):
        line = input().strip().split()
        value = count_stress(line)
        if value > maxvalue:
            maxvalue = value
    return maxvalue

def identify_gender_w_max(given_emotion):
    max_value = 0
    max_gender = None
    for i in range(N):
        worry, restlessness, fear, gender = input().strip().split()
        if given_emotion == "FEAR":
            value = return_value(fear)
            if value > max_value:
                max_gender = gender
                max_value = value
        elif given_emotion == "WORRY":
            value = return_value(worry)
            if value > max_value:
                max_gender = gender
                max_value = value
        elif given_emotion == "RESTLESSNESS":
            value = return_value(restlessness)
            if value > max_value:
                max_gender = gender
                max_value = value
    return max_gender

# counts total stress of given participant
def count_stress(input_line):
    value = 0
    for j in range(3):
        if input_line[j] == "NO":
            value += 0
        elif input_line[j] == "MILD":
            value += 1
        elif input_line[j] == "MODERATE":
            value += 2
        elif input_line[j] == "SEVERE":
            value += 3
    return value

def find_min_stresses():
    minvalue = None
    second_minvalue = None
    for i in range(N):
        line = input().strip().split()
        value = count_stress(line)
        if i == 0:
            minvalue = value
        if i == 1:
            second_minvalue = value
        else:
            if value < minvalue:
                second_minvalue = minvalue
                minvalue = value
    return minvalue, second_minvalue

def count_genders_higher(limit):
    count_female = 0
    count_male = 0
    for i in range(N):
        line = input().strip().split()
        value = count_stress(line)
        if value > limit:
            if line[3] == "F":
                count_female += 1
            elif line[3] == "M":
                count_male += 1
    return count_female, count_male

## DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

TASK = input().strip()
N = int(input())

if TASK == 'AVERAGE_STRESS':
    print('%.2f' % compute_avg_stress())
elif TASK == 'MAX_STRESS':
    print('%.2f' % compute_max_stress())
elif TASK == 'GENDER_MAX':
    emotion = input() # emotion must be one of 'FEAR', 'WORRY', or 'RESTLESSNESS'
    gender_high_emotion = identify_gender_w_max(emotion)
    print(gender_high_emotion)
elif TASK == 'MIN_STRESSES':
    lowest, second_lowest = find_min_stresses()
    print('%.2f %.2f' % (lowest, second_lowest))
elif TASK == 'COUNT_GENDER_HIGHER':
    threshold = float(input())
    female_count, male_count = count_genders_higher(threshold)
    print(female_count, male_count)
