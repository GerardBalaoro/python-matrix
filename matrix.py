class Matrix:

	def __init__(self, rows:int, cols:int):
		if rows < 2:
			raise ValueError('rows must be greater than or equal to 2')
		if cols < 2:
			raise ValueError('cols must be greater than or equal to 2')
		self._numrows = rows
		self._numcols = cols
		self._data = [['' for c in range(cols)] for r in range(rows)]
	
	def get(self, row:int, col:int, default=None):
		if (row >= 0 and col >= 0) and (row < self._numrows and col < self._numcols):
			return self._data[row][col]
		return default

	def set(self, row:int, col:int, value):
		self._data[row][col] = value

	def fillRow(self, row, values:list):
		for col, value in enumerate(values):
			self.set(row, col, value)

	def fillColumn(self, col, values:list):
		for row, value in enumerate(values):
			self.set(row, col, value)

	def getRow(self, row):
		return self._data[row].copy()

	def getColumn(self, col):
		return [row[col] for row in self._data]

	def getDiagonal(self, row, col, forward:bool=False):
		values = []
		def traverse(row, col, ri=1, ci=1):
			while True:
				value = self.get(row, col)
				if value == None:
					break
				yield value
				row += ri
				col += ci
		for val in traverse(row, col, ri=-1, ci=1 if forward else -1):
			values.insert(0, val)
		for val in traverse(row + 1, col + (-1 if forward else 1), ci=-1 if forward else 1):
			values.append(val)
		return values

	def getDiagonals(self, forward:bool=False):
		values = []
		cols = [0, self._numcols] if forward else [self._numcols - 1, -1, -1]
		for c in range(*cols):
			values.append(self.getDiagonal(0, c, forward))
		for r in range(1, self._numrows):
			values.append(self.getDiagonal(
				r, self._numcols - 1 if forward else 0, forward
			))
		return values

	def getRows(self):
		return self._data.copy()

	def getColumns(self):
		return [self.getColumn(i) for i in range(self._numcols)]

	@property
	def numRows(self):
		return self._numrows

	@property
	def numColumns(self):
		return self._numcols
