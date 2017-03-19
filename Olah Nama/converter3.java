import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/*
 * Kelas ini untuk merubah data training yang akan di train pada predict.py
 */

public class converter3 {
	public static void main(String[] args) throws IOException{
		BufferedReader br2 = new BufferedReader(new FileReader("train.gender.data"));
		BufferedReader br3 = new BufferedReader(new FileReader("scoreprediksitrain.txt"));
		FileWriter writer = new FileWriter("outputfinaltrain.txt");
		
		String str = "";
		while((str=br3.readLine())!=null && str.length()!=0){
			String str2 = br2.readLine();
			String split1[] = str.split(" ");
			String split2[] = str2.split(",");
			String output = "";
			
			double score = Double.parseDouble(split1[0]) * 100;
			int bulat = (int) score;
			
			for(int i = 1; i < split2.length; i++){
				if(output.isEmpty()){
					output += bulat + "," + split2[i];
				}else{
					output += "," + split2[i];
				}
			}
			
			writer.append(output);
			writer.append("\r\n");
		}
		writer.close();
	}
}
