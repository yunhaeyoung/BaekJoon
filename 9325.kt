import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))
    
    var str : String = br.readLine()
    var N : Int = Integer.parseInt(str)

    for(i in 1..N){
        str = br.readLine()
        var price : Int = Integer.parseInt(str)

        str = br.readLine()
        var M : Int = Integer.parseInt(str)

        for(j in 1..M){
            var tmp : List<String> = br.readLine().split(' ')
            price += Integer.parseInt(tmp[0]) * Integer.parseInt(tmp[1])
        }

        println(price)
    }
}

