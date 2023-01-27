def Pascal(n):
    nums = [[1]]
    if n <= 0:
        print("Enter a valid value")
    elif n == 1:
        print(nums[0][0])
    elif n > 1:
        for i in range(1, n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(nums[i - 1][j - 1] + nums[i - 1][j])

            nums.append(row)
            '''
            space = n-i - 1
            for j in range(space): print(' ', end = '')
            for j in row: print(j, end = ' ')
            print()
            '''
        # this code doesnt works for double digit or greater ints, so have to create another loop
        last_row = ' '.join(map(str, nums[n - 1]))
        max_chr = len(last_row)
        for i in nums:
            chrs = ' '.join(map(str, i))
            space = (max_chr - len(chrs)) // 2
            for j in range(space): print(' ', end='')
            for j in i: print(j, end=' ')
            print()


Pascal(int(input('Enter number of rows: ')))
