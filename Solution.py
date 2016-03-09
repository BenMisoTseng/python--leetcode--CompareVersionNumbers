class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ##########################################################
        ###########                                   ############
        ########### !!!!!搞不懂他比大小的邏輯啊!!!!!! ############
        ###########                                   ############
        ##########################################################
        def analysis(version):
            """
            解析這串數字
            第一個位置：幾層，後面接著每個層的數字
            """
            #print "version",version #
            pointnum = 0                                        #計算幾層
            resultList = []                                     #解析結果
            for n in version:
                #print "n", n #
                if n == ".":
                    pointnum += 1
            pointnum += 1
            resultList.append(pointnum)                 #寫入幾層數
            #print "resultpointnum", resultList #
            flag = 0                                            #紀錄點點位置
            group = 0                                           #每個層的數字總和
            while (pointnum >= 0 and flag < len(version)):
                if version[flag] == ".":
                    #print group #
                    resultList.append(group)                    #寫入每層的數字
                    group = 0
                    pointnum -= 1
                    #print "pointnum flag", pointnum, flag #
                    #print "result", resultList #
                elif flag == len(version) - 1:
                    group = group * 10 + int(version[flag])
                    resultList.append(group)    ################問題點 最後一個數字如何放進去？？ 已解決ˊˇˋ
                    #print "result", resultList #
                else:
                    group = group * 10 + int(version[flag])
                    #print "group", group #
                flag += 1
            #print "result", resultList #
            return resultList                                   #輸出結果
        
        def fill(lastnum, version):                             #填補空缺的部分
            for n in range(lastnum - len(version) + 1):
                    version.append(0)                           #空缺的部分為0
            return version
            
        v1 = analysis(version1)                                 #載入第一個變數
        v2 = analysis(version2)                                 #載入第二個變數
        #print v1, v2 #
        lastnum = max(v1[0], v2[0])
        #print lastnum #
        v1fill = fill(lastnum, v1)
        v2fill = fill(lastnum, v2)
        #print v1fill, v2fill #
        count = 1
        while(count <= lastnum):                                #比較每一層的大小
            if v1fill[count] > v2fill[count]:
                return 1
            elif v1fill[count] < v2fill[count]:
                return -1
            elif count == lastnum:                              #最後一層還是一樣的話 回傳相等
                return 0
            count += 1