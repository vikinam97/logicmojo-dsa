class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:

        denom = {5: 0, 10: 0, 20: 0}
        billType = [5, 10, 20]
        bal = 0
        for bill in bills:
            retBal = bill - 5
            denom[bill] += 1
            bal += bill

            if retBal == 0:
                continue

            if bal < retBal:
                return False
            
            i = len(billType)-1
            while retBal > 0 and i >= 0:
                count = retBal // billType[i]
                
                avail = min(count, denom[billType[i]])
                denom[billType[i]] -= avail
                bal -= avail * billType[i]

                retBal -= avail * billType[i]

                i -= 1

            if retBal > 0:
                return False
        
        return True

        