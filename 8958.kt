import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))
    
    var str : String = br.readLine()
    var N : Int = Integer.parseInt(str)
    
    for(i in 1..N){
        var score : Int = 0
        var sum : Int = 0
        
        str = br.readLine()
        for(i in 1..str.length){
            if(str[i-1]=='O'){
                score++
                sum += score
            }else{
                score = 0
            }
        }
        println(sum)
    }
}

