
s = "  -43"
c = ["+","-", "0","1","2","3","4","5","6","7","8","9"]
c1 = ["0","1","2","3","4","5","6","7","8","9"]
s = s.strip()
import numpy as np

c1 = np.array([75,68,81,71,73,78,75,94,86,61,92])
p1 = np.array([2,2,2,1,2,2,2,2,2,2,2])

ans = np.sum(((c1-50)/10)*p1)/np.sum(p1)
print(ans)

c1 = np.array([97,73,85,70,85])
p1 = np.array([1,2,2,2,1])

ans = np.sum(((c1-50)/10)*p1)/np.sum(p1)
print(ans)

