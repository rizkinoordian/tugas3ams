import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/*
 * Kelas ini untuk merubah data training yang akan di train pada predict.py
 */

public class converter3 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new FileReader("train.gender.data"));
		FileWriter writer = new FileWriter("outputfinaltrain.txt");
		
		String str = "";
		while((str=br.readLine())!=null && str.length()!=0){
			String[] split = str.split(",");
			String output = "";
			if(split[10].equalsIgnoreCase("female")){
				output = 1 + "," + split[1] + "," + split[2] + "," 
			+ split[3] + "," + split[4] + "," + split[5] + "," + split[6]
					+ "," + split[7] + "," + split[8]+ "," + split[9]+ "," + split[10];
			}else{
				output = 2 + "," + split[1] + "," + split[2] + "," 
			+ split[3] + "," + split[4] + "," + split[5] + "," + split[6]
					+ "," + split[7] + "," + split[8]+ "," + split[9]+ "," + split[10];
			}
			
			writer.append(output);
			writer.append("\r\n");
		}
		writer.close();
	}
}
