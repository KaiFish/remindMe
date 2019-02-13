class Task:
    type = "none"

    def __init__(self, description):
        self.description = description

    # this method lets you use print() with Task objects
    def __str__(self):
        if self.type == "none":
            return self.description
        elif self.type == "due":
            return self.description + "    " + "Due on " + self.date

    def setDueDate(self, date):
        self.type = "due"
        self.date = date
