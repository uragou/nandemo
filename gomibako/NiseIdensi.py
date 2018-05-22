import random;
import matplotlib.pyplot as plt;
N = 5;
M = 10;
MIN = 0;
MAX = 10;
ans = [];
for lop in range(0,N):
    ans.append(random.randint(MIN,MAX));

class Idensi(object):
    def __init__(self):
        self.Ilist = [];
        self.tekio = 0;
        for lop in range(0,N):
            self.Ilist.append(random.randint(MIN,MAX));
        self.Tekiou();
        
    def Tekiou(self):
        for lop in range(0,N):
            self.tekio += abs( ans[lop] - self.Ilist[lop]);
        if self.tekio == 0:
            self.tekio = 1;
        else:
            self.tekio = 1.0 / self.tekio;
    
    def __str__(self):
        return "サンプル = " + str(self.Ilist) + "\n" + "適応値 = " + str(self.tekio) + "\n";
    
    def Totuzen(self):
        self.Ilist[random.randint(0,N-1)] = random.randint(MIN,MAX);
        self.Tekiou();
        
    def Ukeire(self,other):
        for lop in range(0,N):
            self.Ilist[lop] = other[lop];  
           
def Kobai(B1,B2):
    B3 = [];
    for lop in range(0,N):
        if random.random() < 0.5:
            B3.append(B1[lop]);
        else:
            B3.append(B2[lop]);
    return B3;       
        
def MaxData(S):
    Mnum = 0;
    Mhik = 0;
    for lop in range(0,M):
        if Mnum < S[lop].tekio:
            Mnum = S[lop].tekio;
            Mhik = lop;
    return Mhik;


def Sorter(S):
    ans = S;
    
    for lop in range(0,M):
        Mnum = -1;
        Mhik = -1;
        for lop2 in range(lop,M):
            if Mnum < S[lop2].tekio:
                Mnum = S[lop2].tekio;
                Mhik = lop2;
        if Mnum == -1 or Mhik == -1:
            break;
        else:
            buf = ans[lop];
            ans[lop] = ans[Mhik];
            ans[Mhik] = buf;
        
    return ans;

B = [];
A = [];
Tdata = [];
Lop = [];

for lop in range(0,M):
    B.append(Idensi());
B = Sorter(B);  
for lop in range(0,M):
    print(B[lop]);
  
for lop2 in range(101):
    #-----------------------今一時的に４にしている！！
    for lop in range(0,4):
        A.append(B[lop]);
             
    A.append(Idensi());
    A[4].Ukeire(Kobai(B[0].Ilist,B[1].Ilist));
    A.append(Idensi());
    A[5].Ukeire(Kobai(B[0].Ilist,B[2].Ilist));
    A.append(Idensi());
    A[6].Ukeire(Kobai(B[0].Ilist,B[3].Ilist));
    A.append(Idensi());
    A[7].Ukeire(Kobai(B[1].Ilist,B[2].Ilist));
    A.append(Idensi());
    A[8].Ukeire(Kobai(B[1].Ilist,B[3].Ilist));
    A.append(Idensi());
    A[9].Ukeire(Kobai(B[2].Ilist,B[3].Ilist));

    
    if random.random() < 0.8 :
        A[random.randint(0,M-1)].Totuzen();
    B.clear();
    
    for lop in range(0,M):
        B.append(A[lop]);
        B[lop].Tekiou();
      
    Tdata.append(B[MaxData(B)].tekio);
    Lop.append(lop2);
    B = Sorter(B);
    if lop2%10 == 0:
        print("------------------------------------");
        print(str(lop2) +" 代目の結果(ソート済み)\n");
        for lop in range(0,M):
            print(B[lop]);
        print(str(MaxData(B)) + "  " + str(MaxData(B)));
        print("この時の最高適応値");
        print(B[MaxData(B)]);

    A.clear();
       
print("------------------------------------");     
print(B[MaxData(B)]);
print("答え配列 = " + str(ans) + "\n");

plt.plot(Lop,Tdata);
plt.show();

