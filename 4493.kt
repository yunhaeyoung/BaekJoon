import java.io.*

fun main(){
    //val br = BufferedReader(InputStreamReader(System.`in`))
    val br = BufferedReader(FileReader("input.txt"))
    
    var str : String = br.readLine()
    var N : Int = Integer.parseInt(str)
    
    for(i in 1..N){
        var win1 : Int = 0
        var win2 : Int = 0
    
        str = br.readLine()
        var M = Integer.parseInt(str)
        for(j in 1..M){
            var tmp : List<String> = br.readLine().split(' ')
            when(tmp[0]){
                "R" -> when(tmp[1]){
                    "P" -> win2++
                    "S" -> win1++
                }
                "P" -> when(tmp[1]){
                    "R" -> win1++
                    "S" -> win2++
                }
                "S" -> when(tmp[1]){
                    "R" -> win2++
                    "P" -> win1++
                }
            }
        }
        if(win1 > win2){
            println("Player 1")
        }else if(win1 == win2){
            println("TIE")
        }else{
            println("Player 2")
        }
    }
}

