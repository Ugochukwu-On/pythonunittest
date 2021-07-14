class Employee:
    """
    Makes and Stores information on employees
      example:
      emp_1 = Employee("OKE", "ONO")
      (emp_1.fullname)
      (emp_1.email)


    """

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = first + ' ' + last
        self.email = first + '' + last + '@gmail.com'




