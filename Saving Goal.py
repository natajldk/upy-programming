class SavingGoal:
    def __init__(self, goal, monthly):
        self.goal = goal
        self.monthly = monthly
    def months_to_goal (self):
        saving=0
        months=0
        while saving < self.goal:
            saving= saving + self.monthly
            months= months + 1
        return months
print(SavingGoal(1000,250).months_to_goal())