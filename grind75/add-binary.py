class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        total = []
        while i>=0 or j >=0 or carry:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            char_sum = x + y + carry
            carry = char_sum // 2
            total.append(str(char_sum%2))

            i-=1
            j-=1

        return "".join(total[::-1])
