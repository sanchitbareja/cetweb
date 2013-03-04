from twill.commands import *
import twill
import bs4
from program.models import *

def clean(s):
    """
        Cleans html text of usual tags.
    """
    s2 = s
    s2 = s2.replace("<strong>","")
    s2 = s2.replace("</strong>","")
    s2 = s2.replace("<p>","")
    s2 = s2.replace("</p>","")
    s2 = s2.replace("\n","")
    s2 = s2.replace("&amp;","&")
    s2 = s2.replace("&nbsp;","")
    s2 = s2.replace("&#160;","")
    s2 = s2.replace("...","")
    return s2.strip()

def verify_transcript(username,password):
    b = twill.get_browser() #  make it so that twill can handle xhtml  
    b._browser._factory.is_html = True
    twill.browser = b
    config("acknowledge_equiv_refresh",0) #turn of redirection i think... (https://twill.jottit.com/command)
    b.clear_cookies()
    b.go("https://bearfacts.berkeley.edu/bearfacts/student/academicRecord/grades.do?bfaction=allTermGrades")
    try:
        fv("1","username",username)
        fv("1","password",password)
        submit('0')
        submit('0')
    except:
        print show()
    b.go("https://bearfacts.berkeley.edu/bearfacts/student/academicRecord/grades.do?bfaction=allTermGrades")
    soup = bs4.BeautifulSoup(show())

    gpa = soup.findAll("tr",{"align":"LEFT"})[3].findAll("td",{"align":"LEFT"})[-1].text
    class_names = []
    class_numbers = []
    for row in soup.findAll("tr"):
        if len(row.findAll("td"))>=2:
            class_names.append(clean(row.findAll("td")[0].text))
            class_numbers.append(clean(row.findAll("td")[1].text))
    classes = [" ".join(a).lower() for a in zip(class_names,class_numbers)]
    return (float(gpa),cet_courses_in(classes))

def cet_courses_in(l):
    courses = []
    for course in CETCourse.objects.all():
        if course.name.lower() in l:
            courses.append(course)
    return courses
