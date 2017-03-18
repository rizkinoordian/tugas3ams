import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/*
 * Kelas ini untuk merubah data testing yang akan di test pada predict.py
 */

public class converter2 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new FileReader("outputconverttest.txt"));
		BufferedReader br2 = new BufferedReader(new FileReader("test.gender.nolabel.data"));
		FileWriter writer = new FileWriter("outputfinaltest.txt");
		
		String str = "";
		while((str=br.readLine())!=null && str.length()!=0){
			String str2 = br2.readLine();
			String split[] = str2.split(",");
			String cat = "";
			String output = "";
			
			if(str.equalsIgnoreCase("female")){
				cat = "1";
			}else{
				cat = "2";
			}
			
			for(int i = 1; i < split.length; i++){
				if(output.isEmpty()){
					output += cat + "," + split[i];
				}else{
					output += "," + split[i];
				}
			}
			
			writer.append(output);
			writer.append("\r\n");
		}
		writer.close();
	}
}
