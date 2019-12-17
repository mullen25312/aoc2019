#from d01.d01 import d01 as dailyPuzzle
from d02.d02 import d02 as dailyPuzzle

def main():
    m_dailyPuzzle = dailyPuzzle()

    # day1
    #m_dailyPuzzle.readData()
    #print(m_dailyPuzzle.solvePartOne())
    #print(m_dailyPuzzle.solvePartTwo())

    # day2
    m_dailyPuzzle.readData()
    print(m_dailyPuzzle.solvePartOne())
    print(m_dailyPuzzle.solvePartTwo(90,74))
  
if __name__== "__main__":
    main()