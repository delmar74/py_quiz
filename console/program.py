import json

class Quiz():
	
	def __init__(self, theme, description):
		self.theme=theme
		self.description=description
		self.questions=[]

	def add_question(self, statement, answer):
		self.questions.append({"statement": statement, "answer": answer})

	def get_result(self): 
		return json.dumps(vars(self), indent=2)

###################
quiz1=Quiz("RHEL", "Certification Linux")
quiz1.add_question("Расскажи о systemd", "подсистема инициализации Linux — демон для запуска других демонов в Linux и управления ими в процессе работы системы, разработанная взамен используемого ранее демона init ")
print(quiz1.get_result())
