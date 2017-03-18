import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;


public class converter {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new FileReader("train.gender.data"));
		FileWriter writer = new FileWriter("outputconverttrain.txt");
		
		String str = "";
		while((str=br.readLine())!=null && str.length()!=0){
			String split[] = str.split(",");
			int[] array = new int[26];
			
			for(int i = 0, j = 1; i < split[0].length(); i++, j++){
				if(split[0].substring(i, j).equalsIgnoreCase("A")){
					array[0]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("B")){
					array[1]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("C")){
					array[2]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("D")){
					array[3]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("E")){
					array[4]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("F")){
					array[5]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("G")){
					array[6]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("H")){
					array[7]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("I")){
					array[8]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("J")){
					array[9]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("K")){
					array[10]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("L")){
					array[11]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("M")){
					array[12]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("N")){
					array[13]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("O")){
					array[14]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("P")){
					array[15]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("Q")){
					array[16]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("R")){
					array[17]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("S")){
					array[18]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("T")){
					array[19]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("U")){
					array[20]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("V")){
					array[21]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("W")){
					array[22]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("X")){
					array[23]++;
				}else if(split[0].substring(i, j).equalsIgnoreCase("Y")){
					array[24]++;
				}else{
					array[25]++;
				}
			}
			
			String out = "";
			for(int i = 0; i < 26; i++){
				if(out.equals("")){
					out += array[i];
				}else{
					out += "," + array[i];
				}
			}
			writer.append(out + "," + split[10]);
			writer.append("\r\n");
		}
		writer.close();
	}
}