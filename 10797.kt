import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))

    // var str : List<String> = br.readLine().split(' ')
    // println(str[0])
    // //println(br.readLine())

    var cnt : Int = 0
    var str : String = br.readLine()
    var N : Int = Integer.parseInt(str)

    var str2 : List<String> = br.readLine().split(' ')
    
    for(tmp in str2){
        if(N == Integer.parseInt(tmp)){
            cnt++
        }
    }

    println(cnt)
}

