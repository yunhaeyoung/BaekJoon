import java.io.*
import java.util.*

//fun main() = with(Scanner(System.`in`)) {
fun main() = with(Scanner(FileReader("input.txt"))) {    
    
    var score : MutableList<Int> = mutableListOf()

    for(i in 1..5){
        var sum : Int = 0

        for(j in 1..4){
            var tmp : Int = nextInt()
            sum+=tmp
        }

        score.add(sum)
    }

    var maxIdx : Int? = score.indexOf(score.maxOrNull()) + 1
    var maxVal : Int? = score.maxOrNull()

    println("$maxIdx $maxVal")
}
