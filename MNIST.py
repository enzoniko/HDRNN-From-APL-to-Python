from InitNetwork import InitNetwork
import csv
from helpers import gen_chunks
from Equal import Equal
from Product import OuterProduct
from Each import Each
from Table import Table
from ForwardPass import ForwardPass
import LeakyReLU
import MSELoss
from GradeDown import GradeDown
from ReduceFirst import ReduceFirst
from Plus import Plus
from Divide import Divide
from Train import Train
from Over import Over
import pickle

path = './mnistreduced'
net = InitNetwork([64, 16, 16, 10])

def SplitChunk(chunk):
    targets = []
    inputs = []
    for row in chunk:
        targets.append(row[-1])
        inputs.append(row[:-1])
        
    return targets, inputs

def classify(inp):
        print("-", end='')
        return GradeDown(ForwardPass(LeakyReLU, net, Table(inp))[-1])[0]

def lossTEST():
    
    print("Testing...")
    rows = list(csv.reader(open(path + '/test.csv', 'r')))
    rows = [list(map(int, row)) for row in rows]
    outs = []
    
    for i, chunk in enumerate(gen_chunks(rows, 100)):
        print(f'Chunk {i}: ', end='')
        targets, inputs = SplitChunk(chunk)
        resultsMat = []
        for inp in inputs:
            print("-", end='')
            resultsMat.append(ForwardPass(LeakyReLU, net, Table(inp))[-1])
        targetsMat = OuterProduct(targets, list(range(10)), Equal)
        for target, result in zip(targetsMat, resultsMat):

            outs.append(MSELoss.Loss(Table(target), result))
      
        print()
       
    print("Loss: ", Divide(ReduceFirst(Plus, outs), len(outs))[0])
    return 

def accTEST():
  
    print("Testing...")
    rows = list(csv.reader(open(path + '/test.csv', 'r')))
    rows = [list(map(int, row)) for row in rows]
    outs = []
    
    for i, chunk in enumerate(gen_chunks(rows, 200)):
        print(f'Chunk {i}: ', end='')
        targets, inputs = SplitChunk(chunk)
        outs.extend(Equal(Each(classify, inputs), targets))
        print()
        
    print("Accuracy: ", Divide(ReduceFirst(Plus, outs), len(outs))[0])
    return 

def training(target, inp):
    return Train(target, net, [LeakyReLU, MSELoss], inp)

def TRAIN():
    global net
    print("Training...")
    rows = list(csv.reader(open(path + '/train.csv', 'r')))
    rows = [list(map(int, row)) for row in rows]
    for i, chunk in enumerate(gen_chunks(rows, 200)):
        print(f'Chunk {i}: ', end='')
        targetsMat = []
        targets, inputs = SplitChunk(chunk)
        targetsMat = OuterProduct(targets, list(range(10)), Equal)
    
        for target, inp in zip(targetsMat, inputs):  
            net = Over(target, training, Table, inp)
            print(".", end='')
        print()
    print("Training Complete.")
    return

def MNIST():
    
    TRAIN()
    accTEST()
    #lossTEST()
    with open('net.pickle', 'wb') as f:
        pickle.dump(net, f)
    return

if __name__ == '__main__':
    import cProfile
    import pstats
  
    with cProfile.Profile() as pr:
        accTEST()
        MNIST()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
