func searchMatrix(matrix [][]int, target int) bool {
    m, n := len(matrix), len(matrix[0])
    lit, big := 0, m * n - 1
    for lit <= big{
        mid := lit + (big - lit) / 2
        midVal := matrix[mid/n][mid%n]
        if midVal == target{
            return true
        }else if midVal < target{
            lit = mid + 1 
        }else{
            big = mid - 1
        }
    }
    
    return false
}