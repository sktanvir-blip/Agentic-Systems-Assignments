class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            if len(self.marks) < 3:
                raise Exception("Not Enough Marks to Calculate Averagae")
            last_three=self.marks[-3:]
            avg=sum(last_three)/3
            print("Average of last 3 marks is:",avg)
        except Exception as e:
            print(e)

marks=[50,60,70,80,90]

student=StudentMarks(marks)
student.last_three_avg()

            
