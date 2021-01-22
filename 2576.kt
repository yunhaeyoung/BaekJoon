import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))

    // var str : List<String> = br.readLine().split(' ')
    // println(str[0])
    // //println(br.readLine())

    var sum : Int = 0
    var min : Int = 101;
    var isEven : Boolean = true

    for(i in 1..7){
        var str : String = br.readLine()
        var N : Int = Integer.parseInt(str)

        if(N % 2 != 0){
            if(N < min){
                min = N;
            }
            sum += N
            isEven = false
        }
    }

    if(isEven == true){
        println("-1")
    }else{
        println(sum)
        println(min)
    }
}

