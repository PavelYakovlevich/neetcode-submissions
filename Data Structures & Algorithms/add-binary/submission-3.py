class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = [''] * (max(len(a), len(b)) + 1)

        pa = len(a) - 1
        pb = len(b) - 1
        pres = len(res) - 1

        carry = 0
        while pa >= 0 or pb >= 0:
            bit_a = 0 if pa < 0 else int(a[pa])
            bit_b = 0 if pb < 0 else int(b[pb])
            
            res[pres] = str(bit_a ^ bit_b ^ carry)
            pres -= 1
            pa -= 1
            pb -= 1

            carry = ((carry + bit_a + bit_b) & 2) >> 1

        if carry:
            res[pres] = str(carry)

        return ''.join(res)