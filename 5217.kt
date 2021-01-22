import java.io.*
import java.util.*

//fun main() = with(Scanner(System.`in`)) {
fun main() = with(Scanner(FileReader("input.txt"))) {    
    var N : Int = nextInt()
    var isComplete : Boolean
    var isFirst : Boolean

    for(i in 1..N){
        isComplete = false
        isFirst = true
        var tmp : Int = nextInt()

        print("Pairs for $tmp: ")

        var elem1 : Int = 1
        var elem2 : Int = tmp - elem1

        while(elem1 < elem2){
            elem2 = tmp - elem1

            if(tmp - elem1 > elem1){
                if(isFirst == true){
                    print("$elem1 $elem2")
                }else{
                    print(", $elem1 $elem2")
                }
            } 
            elem1++
            isFirst = false;
        }
        isComplete = true

        if(isComplete == true){
            println("")
        }
    }
}
