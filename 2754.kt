import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))

    var str : String = br.readLine()
    
    when(str[0]){
        'A' -> when(str[1]){
            '+' -> println("4.3")
            '0' -> println("4.0")
            '-' -> println("3.7")
        }
        'B' -> when(str[1]){
            '+' -> println("3.3")
            '0' -> println("3.0")
            '-' -> println("2.7")
        }
        'C' -> when(str[1]){
            '+' -> println("2.3")
            '0' -> println("2.0")
            '-' -> println("1.7")
        }
        'D' -> when(str[1]){
            '+' -> println("1.3")
            '0' -> println("1.0")
            '-' -> println("0.7")
        }
        'F' -> println("0.0")
    }
}

