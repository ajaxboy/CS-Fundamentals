/**
 *  Author: CJ Galindo
 *  Merge sort algorigthm
 *  Time complexity: O (n log n)
 *  Best time: Ω (n log n)
 *  Space Complexity: O(n)
 */
function mergeSort (arr) {
  const len = arr.length

  if (len === 1) {
    return arr
  }

  const mid = Math.floor(len / 2)
  const left = mergeSort(arr.slice(0, mid))
  const right = mergeSort(arr.slice(mid))

  return merge(left, right)
}

function merge (left, right) {
  let arr = []
  const lenLeft = left.length
  const lenRight = right.length
  let indexLeft = 0
  let indexRight = 0
  while (indexLeft < lenLeft && indexRight < lenRight) {
    if (left[indexLeft] < right[indexRight]) {
      arr.push(left[indexLeft])
      indexLeft++
    } else {
      arr.push(right[indexRight])
      indexRight++
    }
  }

  while (indexLeft < lenLeft) {
    arr.push(left[indexLeft])
    indexLeft++
  }

  while (indexRight < lenRight) {
    arr.push(right[indexRight])
    indexRight++
  }

  return arr
}


console.log(mergeSort([5,4,3,2,1]))