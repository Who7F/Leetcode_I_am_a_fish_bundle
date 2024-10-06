func rotate(matrix [][]int)  {
    l := len(matrix)
    for i := range l{
        for j := range i{
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        }
    }
    for i := range l/2{
        for j := range l{
            matrix[j][i], matrix[j][l - i - 1] = matrix[j][l - i - 1], matrix[j][i]
        }
    }
}