class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sumArr = []
        length = len(nums1)+len(nums2)
        x1=0
        z2=0
        for i in range(length):
            if z2 < len(nums2) and x1 <len(nums1):
                if nums2[z2] > nums1[x1]:
                    sumArr.append(nums1[x1])
                    x1+=1
                else:
                    sumArr.append(nums2[z2])
                    z2+=1
            else:
                if x1 >= len(nums1) :
                    if z2 < len(nums2):
                        sumArr.append(nums2[z2])
                        z2+=1
                else:
                    if  len(nums2) >= z2:
                        sumArr.append(nums1[x1])
                        x1+=1
            

        if length==1:
            return sumArr[0]
        if (z2+x1)%2 ==0:
            return (sumArr[length/2]+sumArr[(length/2)-1])/2.0
        else:
            return sumArr[(z2+x1)/2]
        


        