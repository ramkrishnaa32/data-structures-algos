/*
Given a string s consisting of words and spaces, return the length of the last word in the string.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
*/

object LastWord {
  def lengthOfLastWord(s: String): Int = {
    val words = s.trim.split("\\s+")
    println(s"String: '$s', Words: [${words.mkString(", ")}]")
    words.last.length
  }

  def main(args: Array[String]): Unit = {
    val s = "   fly me   to   the moon  "
    val result = lengthOfLastWord(s)
    println(s"Length of last word: $result")
  }
}