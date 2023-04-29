class Movie:
    def __init__(self,name,year):
        self.name = name
        self.year = year
matrix = Movie('matrix',1994)
print(matrix.name)
print(Movie('matrix',1994).year)