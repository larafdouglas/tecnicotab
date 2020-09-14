import math

class PontoMath():
	def __init__ (self, fs=0, fm = 0, fi = 0, alfa_grau=0,alfa_min=0,alfa_segundo=0):
		self.fs = fs
		self.fm = fm
		self.fi = fi
		self.alfa_grau = alfa_grau
		self.alfa_min = alfa_min
		self.alfa_segundo = alfa_segundo

	def degree_to_int(self):
		minutes = (self.alfa_segundo/60) + self.alfa_min
		grau= (self.alfa_grau) + (minutes/60)
		return grau


	def calc_dist(self):
		d=100*(self.fs-self.fi)*(math.cos(math.radians(self.degree_to_int())))**2
		return d