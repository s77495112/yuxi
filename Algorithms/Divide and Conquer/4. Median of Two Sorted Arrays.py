class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		m, n = len(nums1), len(nums2)
		if(m > n):
			nums1, nums2 = nums2, nums1
			m, n = n, m
		left, right = 0, m
		half = (n + m + 1) >> 1
		while(left <= right):
			i = (left + right) >> 1
			j = half - i 
			if(i < m and nums1[i] < nums2[j-1]):
				left = i + 1
			elif(i > 0 and nums2[j] < nums1[i-1]):
				right = i - 1
			else:
				if(i == 0):
					max_left = nums2[j-1]
				elif(j == 0):
					max_left = nums1[i-1]
				else:
					max_left = max(nums1[i-1], nums2[j-1])
				if(m + n) % 2 == 1:
					return max_left
				if(i == m):
					min_right = nums2[j]
				elif(j == n):
					min_right = nums1[i]
				else:
					min_right = min(nums1[i], nums2[j])
				return (max_left + min_right) / 2.0
