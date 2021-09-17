# Created by Marcin "Cozoob" Kozub at 20.04.2021 08:45

def can_construct(target, words):
    memo = [0 for _ in range(len(target) + 1)]
    memo[0] = True

    def rec_can_construct(target, words, memo):
        if target == "":
            return True
        if memo[len(target)] != 0:
            return memo[len(target)]

        for i in range(len(words)):
            word = words[i]
            flag = True
            if word[0] == target[0] and len(word) <= len(target):
                for j in range(1, len(word)):
                    if word[j] != target[j]:
                        flag = False
                if flag == True:
                    curr_target = rec_can_construct(target[len(word):], words, memo)
                    if curr_target == True:
                        memo[len(target)] = True
                        return True

        memo[len(target)] = False
        return False

    return rec_can_construct(target, words, memo)

if __name__ == '__main__':
    # print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
    # print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
    # print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False