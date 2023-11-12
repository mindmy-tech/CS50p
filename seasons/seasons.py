from datetime import date, datetime, timedelta
import inflect
import sys

# OOP
class minutesCalculator:
    def __init__(self ,date=None):
        self.dob = self.validate(self.get_dob(date))
        rn = self.time_rn()
        self.td_mins = self.minutes(self.dob, rn)

    def __str__(self) -> str:

        return self.write_lyrics(self.td_mins)

    def write_lyrics(self,td_mins):
        p = inflect.engine()
        lyrics = p.number_to_words(td_mins, andword="")
        lyrics = f"{lyrics} minutes".capitalize()
        return lyrics

    def get_dob(self, date):

        if date == None:
            date = input("Enter Your date of birth [dob format: yyyy-mm-dd] :").strip()

        return date

    def validate(self,date):

        try:
            if date := datetime.strptime(date, "%Y-%m-%d"):
                date = datetime.combine(date, datetime.min.time())
                return date
        except ValueError:
            sys.exit("Invalid Date")

    def time_rn(self):
        time_rn = datetime.combine(date.today(), datetime.min.time())
        return time_rn

    def minutes(self, dob: datetime , rn: datetime) -> int:
        td = rn - dob
        return int(td / timedelta(minutes=1))


def main():
    print(minutesCalculator())




if __name__ == "__main__":
    main()