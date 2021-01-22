import java.io.*
import java.util.*

//fun main() = with(Scanner(System.`in`)) {
fun main() = with(Scanner(FileReader("input.txt"))) {    
    var N : Int = nextInt()
    
    for(i in 1..9){
        println("$N * $i = ${N*i}")
    }
}
