import datetime

def greet_user():
    hour = int(datetime.datetime.now().strftime("%H"))
    if hour>=0 and hour<6:
        return "You should consider going to sleep early.."
    elif hour>=6 and hour<12:
        return "Good Morning!"
    elif hour>=12 and hour<14:
        return "Good Noon"
    elif hour>=14 and hour<16:
        return "Good Afternoon"
    elif hour>=16 and hour<20:
        return "Good Evening"
    elif hour>=20:
        return "Good Night"