# Enter your code here. Read input from STDIN. Print output to STDOUT
import os

def WordsOrder(listWords):
    
    CountGraph = {}
    for word in listWords:
        if word in CountGraph.keys():
            CountGraph[word] += 1
        else: 
            CountGraph[word] = 1 
    
    print(CountGraph)
         
    words = [ str(num) for num in CountGraph.values()]
    wordsNumber = len(words)

    return str(wordsNumber)," ".join(words)
         
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    words = [input() for i in range(0,n)]
    result1,result2 = WordsOrder(words)
    fptr.write(result1 + '\n')
    fptr.write(result2 + '\n')
    fptr.close()