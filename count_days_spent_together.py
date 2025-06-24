class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_arrive_month = int(arriveAlice.split("-")[0])
        alice_arrive_day = int(arriveAlice.split("-")[1])

        alice_leave_month = int(leaveAlice.split("-")[0])
        alice_leave_day = int(leaveAlice.split("-")[1])

        bob_arrive_month = int(arriveBob.split("-")[0])
        bob_arrive_day = int(arriveBob.split("-")[1])

        bob_leave_month = int(leaveBob.split("-")[0])
        bob_leave_day = int(leaveBob.split("-")[1])

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        alice_arrive = sum(months[:int(alice_arrive_month)-1])+alice_arrive_day
        bob_arrive = sum(months[:int(bob_arrive_month)-1])+bob_arrive_day

        alice_leave = sum(months[:int(alice_leave_month)-1])+alice_leave_day
        bob_leave = sum(months[:int(bob_leave_month)-1])+bob_leave_day

        leave = min(alice_leave, bob_leave)
        arrive = max(alice_arrive, bob_arrive)

        if leave == arrive:
            return 1

        result = leave - arrive

        if result <= 0:
            return 0

        return result + 1
