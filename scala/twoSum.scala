
/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
*/

object TwoSum {
  def HashMap(nums: List[Int], target: Int): List[Int] = {
    val numsDict = scala.collection.mutable.Map[Int, Int]()
    for ((value, index) <- nums.zipWithIndex) {
        val difference = target - value
        if (numsDict.contains(difference)) {
            return List(numsDict(difference), index)
        }
        numsDict(value) = index
    }
    List()
}

  def main(args: Array[String]): Unit = {
    val nums = Array(7, 6, 4, 3, 1, 9, 10, 11, 12)
    val target = 23
    if (HashMap(nums.toList, target).isEmpty) {
        println("No solution found")
    } else 
    println(s"Index: ${HashMap(nums.toList, target)}")
}
}