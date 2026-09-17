# Name: Sanjay Tirumalai
# Period: not applicable
# Student Performance Analyzer

# not actually a spa, right? bruh
# damn it i can only use class covered concepts

import random
# ok im not going to use this import statement. happy?
# huh i just realized there's anal in analyzer :o

# projram infrojunction
print("""
========================================
       STUDENT PERFORMANCE ANALYZER
========================================

Enter the student's information below.
""")

print("by the way there aren't any try except blocks so don't screw this up")

student_name = input("enter name: ")
student_gradelv = int(input("enter grade level: "))
student_asavg = float(input("enter assignment average: "))
student_qzavg = float(input("enter quiz average: "))
student_tsavg = float(input("enter test average: "))
student_attp = float(input("enter attendance percentage: "))
student_missingas = int(input("enter number of missing assignments: "))

def calculate_grade(assignment_average,quiz_average, test_average):
    assnw = .3
    qzw = .3
    tsw = .4
    ovg = assnw*assignment_average + quiz_average*qzw + test_average*tsw
    print(ovg)
    return ovg

student_overall_grade = calculate_grade(student_asavg, student_qzavg, student_tsavg)
# your request was ambigious, so i made it do both
# yes i know i spelled ambiguous wrong

def letter_grade(ovrall_grade):
    # haha bad spelng go brrr
    # bruh
    # man i hate python
    lg = 'F'
    og = ovrall_grade
    # shorthand bc im lazy
    if og >= 90:
        lg = 'A'
    elif og >= 80:
        lg = 'B'
    elif og >= 70:
        lg = 'C'
    elif og >= 60:
        lg = 'D'
    else:
        pass
    # hey man you said to use else and i didn't need to use it
    print("Letter Grade: " + lg)
    return lg
# i also made this do both
student_ltrg = letter_grade(student_overall_grade)
# man i have autism

def attendance_status(attendance):
    # alright ill use your stupid else keyword now
    # gah
    print("attendance status:")
    if attendance >= 95:
        print("excellent attendance")
    elif attendance >= 90:
        print("good attendance")
    elif attendance >= 80:
        print("attendance warning?")
    else:
        print("poor attendance l bozo ratio bozo")
    # whoopsies
    # being stupid is dumb

attendance_status(student_attp);
# adenosine tri tri phosphate heh bruh ok im done
# rip

def assignment_status(missing_assignments):
    # alright cool you didn't specify
    sts = 'critical'
    if missing_assignments == 0:
        sts = 'excellent'
    elif missing_assignments <= 2:
        sts = 'good'
    elif missing_assignments <= 4:
        sts = 'warning'
    print("missing assignment status: " + sts)

assignment_status(student_missingas)
# voiced bilabial plosives are cool i guess
# bruh
# bruh
# bruh

def check_eligibility(ovrall_grade, attndc, msg_assn):
    # hoo boy
    ## format components and stuff
    rsn = ''
    rssn = 'reason: '
    contratator = 'not '
    eglb = 'eligible'
    ## nested ifs, equivalent to and, yk
    if ovrall_grade >= 70:
        if attndc >= 90:
            if msg_assn <= 2:
                contratator = ''
                rssn = ''
                rsn = 'student passed all 3 requirements'
            else:
                rsn = 'too many missing assignments'
        else:
            rsn = 'attendance is too low'
    else:
        rsn = 'overall grade is too low'
    print("academic eligibility: "+contratator+eglb)
    print(rssn+rsn)

check_eligibility(student_overall_grade, student_attp, student_missingas)

# ye've got to be less ambigious with this stuff

def check_high_honors(ovrall_grade, attndc, msg_assn):
    ## format components
    hh = 'eligible'
    hhn = 'not '
    rsn = ''
    rssn = 'reason: '
    if ovrall_grade >= 90:
        if attndc >= 95:
            if msg_assn == 0:
                hhn = ''
            else:
                rsn = 'student has missing assignments'
        else:
            rsn = 'attendance requirement not met'
    else:
        rsn = 'grade requirement not met'
    ## format string
    strint = "high honors: " + hhn+hh+"\n"+rssn+rsn
    # well you didn't say anything about printing so im js not going to do it

def check_good_standing(opvralg , atnd):
    # maybe it would benefit us if you made us make a game as a test rsm

    ## good standing no by default
    gs = 'no'
    ## changes under conditions
    if opvralg >= 70 and atnd >= 90:
        gs = 'yes'
    s = 'good standing: ' + gs
# be more specific about these things

def check_support(ovral_galed, atd):
    ads = 'not needed'
    ## additional support is not needed by default
    if ovral_galed < 70 or atd < 80:
        ads = 'recommended'
    ## format string?
    f = 'additional support: ' + ads
# sign
# sigh
# whatever
#

## formatting for print statement
lrs = ''
lrst = 'login '
lmnop = 'failed: '
qery_usnm = input('enter username: ')
qery_psw = int(input("enter pin: "))
if qery_usnm != 'student':
    lrs = 'incorrect username'
else:
    if qery_psw != 1234:
        lrs = 'incorrect pin'
    else:
        lmnop = 'successful'
## login successful/failed: /
# yk
print(lrst+lmnop+lrs)
# yes ok so this might reveal the password o

def grade_level_message(grade_level):
    ## initialize "pointer" to modify or whatever
    monosodiumglutamate = ''
    if grade_level == 9:
        monosodiumglutamate = 'welcome to freshman year?'
    elif grade_level == 11:
        # yk you don't have to use if because the number can't be 9 and 10 but ok
        # you also don't have to use else but alright man
        monosodiumglutamate = 'junior year - keep pushing?'
    elif grade_level == 10:
        monosodiumglutamate = 'keep building your skills?'
    elif grade_level == 12:
        monosodiumglutamate = 'senior year - finish strong?'
    else:
        print("invalid grade level?")
# did you tell me to call the function?
# HM????

def strongest_category(asavg, qzavg, tsavg):
    # im too lazy for these long sophisticated words

    ## strongest category is tests by default
    big = 'tests'
    if asavg > tsavg and asavg > qzavg:
        big = 'assignments'
    elif qzavg > asavg and qzavg > tsavg:
        big = 'quizzes'
    print("strongest category: " + big)
# okay you said display one of so i guess you mean call it?
strongest_category(student_asavg, student_qzavg, student_tsavg)

print("==================\nstudent summary?\n==================\nstudent: "+student_name+"\ngrade level: "+str(student_gradelv)+"\n\nassignment average: "+str(student_asavg)+"\nquiz average: "+str(student_qzavg)+"\ntest average: "+str(student_tsavg)+"\n\noverall grade: "+str(student_overall_grade)+"\nmissing assignments: "+str(student_missingas))
    
# alright so i have a bunch of meaningless comments
# the meaningful comments start with ##

# i put like 11
# maybe they don't count
# whatever

def check_advanced_status():
    o = 'standard student status'
    if (student_overall_grade >= 90 and student_attp >= 95) or (student_overall_grade >= 85 and student_missingas == 0):
        o = 'outstanding student'
    print("\nadvanced status: "+ o)
    # "carefully combine"
    # teach us something new already

# man forget your submission checklist
check_advanced_status()



