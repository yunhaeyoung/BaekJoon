import java.io.*
import java.util.*

//fun main() = with(Scanner(System.`in`)) {
fun main() = with(Scanner(FileReader("input.txt"))) {    
    var a : String = next() + next()
    var b : String = next() + next()

    println(a.toInt() + b.toInt())

    // var str : List<String> = nextLine().split(' ')
    // println((str[0] + str[1]).toInt() + (str[2] + str[3]).toInt())
}
