import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))

    // var str : List<String> = br.readLine().split(' ')
    // println(str[0])
    // //println(br.readLine())

    var str : String = br.readLine()
    var N : Int = Integer.parseInt(str)

    println(N - 543)
}

