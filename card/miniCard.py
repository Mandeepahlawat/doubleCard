class MiniCard:
	def __init__(self):
		self.cell = None

	def set_color(self, color):
		self.color = color

	def set_text(self, text):
		self.text = text
		
	def set_cell(self, cell):
		self.cell = cell
		cell.miniCard = self
		# self.cell.set_miniCard(self) 

	def __str__(self):
		return "%s(%s)" % (self.text, self.color)