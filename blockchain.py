import hashlib
import time

# 1. 블록 만들기
class Block():
    def __init__(self, index, timestamp, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = 0
        self.nonce = 0
        self.hash = self.calHash()

    def calHash(self):
        return hashlib.sha256(str(self.index).encode() + str(self.data).encode() +
                            str(self.nonce).encode() + str(self.timestamp).encode() + str(self.previousHash).encode()).hexdigest()

    def mine(self):
        print('previousHash: ', self.previousHash)
        while(str(self.hash)[:5] != "00000"):
            self.nonce += 1
            self.hash = self.calHash()

        self.previousHash = self.hash

        print('hash: ', self.hash)
        print('nonce : ', self.nonce)

        return self.hash


# 2. 체인만들기
class BlockChain:
    def __init__(self, ):
        self.chain = []
        self.difficulty = 5
        self.createGenesis()

    def createGenesis(self):
        self.chain.append(Block(0, time.time(), 'Genesis'))

    def addBlock(self, nBlock):
        nBlock.previousHash = self.chain[len(self.chain)-1].hash
        nBlock.hash = nBlock.mine()
        self.chain.append(nBlock)

cnt = 0
init_block = BlockChain()

while cnt < 3 :
    cnt += 1
    print('{} block ..' .format(cnt))
    start_time = time.time();
    data = "test입니다"
    init_block.addBlock(Block(len(init_block.chain),time.time(), data))
    print('체굴 시간: ', time.time() - start_time)