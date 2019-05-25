class TimeSpan(object):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    @property
    def total_seconds(self):
        return self._hours*3600 + self._minutes*60 + self._seconds

    def __add__(self, other):
        new_timepan = TimeSpan(self._hours, self._minutes, self._seconds)
        new_timepan.add_seconds(other.total_seconds)

        return new_timepan

    def __sub__(self, o):
        inverted_other = TimeSpan(-o._hours, -o._minutes, -o._seconds)
        return self.__add__(inverted_other)

    def __str__(self):
        return f"{self._hours:02}:{self._minutes:02}:{self._seconds:02}"

    def __eq__(self, other):
        return self._hours == other._hours and self._minutes == other._minutes and self._seconds == other._seconds

    def __ne__(self, value):
        return not self.__eq__(value)

    def __le__(self, other):
        return self.total_seconds <= other.total_seconds

    def __lt__(self, other):
        return self.total_seconds < other.total_seconds

    def __ge__(self, other):
        return self.total_seconds >= other.total_seconds

    def __gt__(self, other):
        return self.total_seconds > other.total_seconds

    def add_seconds(self, value):
        total = self.total_seconds + value
        minutes, self._seconds = divmod(total, 60)
        hours, self._minutes = divmod(minutes, 60)
        _, self._hours = divmod(hours, 24)

    def add_minutes(self, minutes):
        self.add_seconds(minutes*60)

    def add_hours(self, hours):
        self.add_seconds(hours*60*60)


timespan = TimeSpan()

timespan.add_seconds(65)
timespan.add_seconds(12065)

timespan2 = TimeSpan()

timespan2.add_seconds(12065)

print(timespan < timespan2)
print(timespan <= timespan2)
print(timespan >= timespan2)
print(timespan > timespan2)
print(timespan == timespan2)
print(timespan != timespan2)

print(timespan - timespan2)
print(timespan + timespan2)
