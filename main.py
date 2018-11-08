class HashTableNode:
    def __init__(self,key,value):
        self.pairs=[[key,value]]
    def getValue(self,key):
        for pair in self.pairs:
            if(pair[0]==key):
                return pair[1]
    def getKey(self,i):
        return pairs[i][0]
    def addValue(self,key,value):
        for i in self.pairs:
            if(i[0]==key):
                i[1]=value#overwrite the value if it is the same as another key
                return
        self.pairs.append([key,value])
    def __repr__(self):
        return str(self.pairs)

class HashTable:
    def __init__(self, capacity):
        self.dict=[None]*capacity
    def hashCode(self,key):
        sum=0;
        for i in range(len(key)):
            sum+=ord(key[i])*pow(2,i)
        return sum%len(self.dict)
    def getFilledSlots(self):
        n=0;
        for slot in self.dict:
            if(slot!=None):
                n+=1;
        return n
    def put(self,key,value):
        h=self.hashCode(key)
        if(self.dict[h]==None):
            self.dict[h]=HashTableNode(key,value);
        else:
            self.dict[h].addValue(key,value)
        if(self.getFilledSlots()/len(self.dict)>0.8):
            self.resize(len(self.dict)*2)

    def get(self,key):
        if(self.dict[self.hashCode(key)]==None):
            return None
        return self.dict[self.hashCode(key)].getValue(key)
    def resize(self,newSize):
        data=[];
        for i in range(0,len(self.dict)):
            if(self.dict[i]!=None):
                data.append(self.dict[i])

        self.dict=[None]*newSize
        for item in data:
            #print(item.pairs[0])
            for pair in item.pairs:
                self.put(pair[0], pair[1])


h=HashTable(10)

h.put("i",1)
h.put("eeee",2)# these two values should have a collision

h.put("j",3)
print(h.dict)

print("should be 1:"+str(h.get("i")))
print("should be 2:"+str(h.get("eeee")))
print("should be none:"+str(h.get("notAValidKey")))

#test resize
h.resize(7);
print("should be 7:"+str(len(h.dict)))
print(h.dict)

#make sure the keys are still in place
print("should be 1:"+str(h.get("i")))
print("should be 2:"+str(h.get("eeee")))


# add values to make sure it doubles in size
print("should be 7:"+str(len(h.dict)))
for i in range(0,10):
    h.put(str(i),1)
print("should be 14:"+str(len(h.dict)))
print(h.dict)


"""
h=HashTable(10)
print(h.dict)
h.resize(15)
print(h.dict)
h=HashTable(15)
h.put("a","a")
h.put("b","b")
h.put("c","c")
h.put("d","d")
h.put("h","h")
h.put("i","i")
h.put("eeee","hi")
h.put("key3","val")
print(h.dict)
h.resize(10)
print(h.dict)
try:
    h.put("ab","hi")
except:
    print("succesfully failed")
print(h.get("a"))
print(h.get("i"))
print(h.get("eeee"))
print(h.get("not defined"))


print(len(h.dict))
for i in range(0,10):
    h.put(str(i),1)
print(len(h.dict))
"""
