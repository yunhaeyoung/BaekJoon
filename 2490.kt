import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))

    // var str : List<String> = br.readLine().split(' ')
    // println(str[0])
    // //println(br.readLine())

    for(i in 1..3){
        var zero : Int = 0
        var one : Int = 0

        var str : List<String> = br.readLine().split(' ')
        for(tmp in str){
            if(Integer.parseInt(tmp) == 0){
               zero++
            }else{
               one++
            }
        }

        when(zero){
            0 -> println("E")
            1 -> println("A")
            2 -> println("B")
            3 -> println("C")
            4 -> println("D")
        }
    }
}

