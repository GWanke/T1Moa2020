import java.util.*;
import java.lang.*;
import java.io.*;

public class Main  
{ 
	static List<Integer> tabuleiroFinal = new ArrayList<>(List.of(1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7));

    protected static class Peca{
        List<Integer> tabuleiro;
        int f;
        int g;
        int indexZero;
        Peca(List<Integer> tabuleiro, Integer f, Integer g, Integer indexZero){
            this.tabuleiro = tabuleiro;
            this.f=f;
            this.g=g;
            this.indexZero=indexZero;
        }
        List<Integer> getTabuleiro(){
            return this.tabuleiro;
        }
    }

    public static List<Integer> readInput()  
    {   
   		List<Integer> entrada = new ArrayList<Integer>();
    	String  lines = System.console().readLine();    
    	String[] strs = lines.trim().split("\\s+");       
    	for (int i = 0; i < strs.length; i++) {
    		entrada.add(Integer.parseInt(strs[i]));
    	}
    	return entrada;
    }

    public static void main(String[] args){
        List<Integer> tabuleiroInicio = new ArrayList<Integer>();
    	tabuleiroInicio = readInput();
        Peca teste = new Peca(tabuleiroInicio,0,0,2);
        System.out.println(teste.getTabuleiro());
    	//System.out.println(tabuleiroFinal);
    }
}    
