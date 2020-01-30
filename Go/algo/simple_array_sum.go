
// https://www.hackerrank.com/challenges/simple-array-sum/problem

func simpleArraySum(ar []int32) int32 {
    
    var sum int32 =  0
    for i := 0; i < len(ar); i ++ {
        sum += ar[i]
    }

    return sum
}