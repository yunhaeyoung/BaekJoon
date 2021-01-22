import java.io.*
import java.util.*

//fun main() = with(Scanner(System.`in`)) {
fun main() = with(Scanner(FileReader("input.txt"))) {    
    var N : Int = nextInt()

    var tmp : Int = nextInt()

    var min : Int = tmp
    var max : Int = tmp

    for(i in 1..N-1){
        tmp = nextInt()

        if(tmp < min){
            min = tmp
        }else if(tmp > max){
            max = tmp
        }
    }

    println("$min $max")
}