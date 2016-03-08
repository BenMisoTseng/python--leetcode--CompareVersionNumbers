class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def analysis(version):
            """
            解析這串數字
            第一個位置：幾層，後面接著每個層的數字
            """
            print "version",version #
            pointnum = 0                                        #計算幾層
            resultList = []                                     #解析結果
            for n in version:
                print "n", n
                if n == ".":
                    pointnum += 1
                    resultList.append(pointnum)                 #寫入幾層數
            print "resultpointnum", resultList #
            flag = 0                                            #紀錄點點位置
            group = 0                                           #每個層的數字總和
            while (pointnum >= 0 and flag < len(version)):
                if version[flag] == ".":
                    print group #
                    resultList.append(group)                    #寫入每層的數字
                    group = 0
                    pointnum -= 1
                    print "pointnum flag", pointnum, flag #
                    print "result", resultList #
                elif flag == len(version) - 1:
                    resultList.append(group)    ################問題點 最後一個數字如何放進去？？
                    print "result", resultList #
                else:
                    group = group * 10 + int(version[flag])
                    print "group", group #
                flag += 1
            print "result", resultList #
            return resultList [1:]                              #輸出結果
                    
        
        v1 = analysis(version1)
        v2 = analysis(version2)
        print v1, v2 #