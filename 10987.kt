import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))
    
    var str : String = br.readLine()
    var cnt : Int = 0

    var myList : List<Char> = listOf('a', 'e', 'i', 'o', 'u')
    
    for(i in 1..str.length){
        when(str[i-1]){
            in myList -> cnt++
        }
    }

    println(cnt)
}

