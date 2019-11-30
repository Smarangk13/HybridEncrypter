import random
import math


class shuffle:

    # Function to return number as string with leading 0s
    def neededDigits(self, num, d):
        n = 10 ** d
        n += num
        r = str(n)[1:]
        return r

    def fixShuffle(self, ar, code, wordsize, arrtype='dict'):
        l = len(code)
        i = 0
        pos = 0
        if arrtype == 'dict':
            arr = ar.copy()
        else:
            arr = ar[:]

        # print(arr[3])
        while pos < l:
            n = code[pos:pos + wordsize]
            # n = int(n)
            p = i
            if arrtype == 'dict':
                p = self.neededDigits(i, wordsize)
            else:
                n = int(n)

            arr[p], arr[n] = arr[n], arr[p]
            i += 1
            pos += wordsize

        return arr

    def slide(self, d, s, wordsize = 2):
        deck = {}
        l = len(d)
        s %= l
        for i in d:
            newkey = self.neededDigits((s + int(i)) % l, wordsize)
            deck[newkey] = d[i]

        return deck

if __name__ == "__main__":
    print("hey")
    deck = shuffle()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    print(nums)
    # cards1 = deck.arrShuffle(nums)
    # print(cards1)
    # cards2 = deck.swapShuffle(nums,25)
    # print(cards2)
    # x = deck.randSeq(40,61)
    # print(x)
    swapCode = "1006031207010913"
    res = deck.fixShuffle(nums, swapCode, 2, 0)
    print(res)
