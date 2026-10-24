class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:
        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)

        if arrive > leave:
            return 0

        days_in_month = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

        def day_of_year(date):
            month, day = map(int, date.split('-'))
            return sum(days_in_month[:month - 1]) + day

        return day_of_year(leave) - day_of_year(arrive) + 1