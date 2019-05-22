import re
import datetime as dt
template = "Hello <<name>>, We have your full name as <<full name>> in our system."\
           "your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification" \
           " Thank you BridgeLabz 01/01/2016"
try:
    name = input("Enter Your Name : ")
    fullname = input("Enter Your Full Name : ")
    mobile = input("Enter Your Mobile Number : ")

    if not name.isalpha() or not mobile.isdigit() or not len(str(mobile)) == 10:
        raise ValueError
    else:
        print()
        cr_date = dt.datetime.now()
        cr_date = cr_date.strftime("%d/%m/%Y")
        template = re.sub("<<name>>", name.upper(), template)
        template = re.sub("<<full name>>", fullname.upper(), template)
        template = re.sub("xxxxxxxxxx", mobile, template)
        template = re.sub("01/01/2016", cr_date, template)
        print(template)
except ValueError:
    print("\nYou Entered Wrong Data..!")


