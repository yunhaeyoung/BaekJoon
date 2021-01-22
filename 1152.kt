import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))

    var str : List<String> = br.readLine().split(' ')
    var cnt : Int = 0

    for(tmp in str){
        if(tmp != ""){
            cnt++
        }
    }

    println(cnt)
}

