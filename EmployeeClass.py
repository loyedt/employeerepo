class Employee:
	def __init__(self,eid,ename,eloc,esal):
		self.eid=eid
		self.ename=ename
		self.eloc=eloc
		self.esal=esal
	def getemployee(self):
		print("Employee id "+str(self.eid)+" name "+self.ename+" location "+self.eloc+" Salary "+str(self.esal))

