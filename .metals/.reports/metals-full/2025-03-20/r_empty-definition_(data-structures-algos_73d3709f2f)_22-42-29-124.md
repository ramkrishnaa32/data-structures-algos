error id: scala/Int.MaxValue.
file://<WORKSPACE>/maximun_profit.scala
empty definition using pc, found symbol in pc: scala/Int.MaxValue.
empty definition using semanticdb
|empty definition using fallback
non-local guesses:
	 -Int.MaxValue.
	 -Int.MaxValue#
	 -Int.MaxValue().
	 -scala/Predef.Int.MaxValue.
	 -scala/Predef.Int.MaxValue#
	 -scala/Predef.Int.MaxValue().

Document text:

```scala

/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
*/

object Solution {
  def onePass(prices: List[Int]): Int = {
    var maxProfit = 0
    var minPrice = Int.MaxValue
    for (price <- prices) {
        minPrice = math.min(minPrice, price) // Find the minimum price
        maxProfit = math.max(maxProfit, price - minPrice) // Find the maximum profit
    }
    maxProfit
}

  def main(args: Array[String]): Unit = {
    val prices = Array(7, 6, 4, 3, 1, 9, 10, 11, 12)
    println(s"Maximum profit: ${maximizeProfit(prices)}")
  }
}
```

#### Short summary: 

empty definition using pc, found symbol in pc: scala/Int.MaxValue.