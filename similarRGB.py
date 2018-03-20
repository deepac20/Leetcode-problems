class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        out = '#'
        i=1
        code = '0123456789abcdef'
        cod = ''
        while i!= len(color):
            diff = sys.maxint
            num='0x'
            num += str(color[i])+str(color[i+1])
            if color[i] == color[i+1]:
                out+=str(color[i])+str(color[i+1])
            else:
                num_int = int(num,16)
                for j in code:
                    temp = '0x'+(j*2)
                    temp_int = int(temp,16)
                    temp_diff = hex(num_int - temp_int)
                    temp_diff_sq = int(temp_diff,16)**2
                    if temp_diff_sq < diff:
                        diff = temp_diff_sq
                        cod = j*2
                out += str(cod)
            i+= 2
        return out
