import java.util.Scanner;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) {
		ArrayList<String> Options = new ArrayList<String>();
		Options.add("add");

		Scanner input = new Scanner(System.in);
		System.out.println("AAAA");

		System.out.println("What operation do you want to use. \n 1) Add");
		String Do = input.nextLine().toLowerCase();
		Calculator calc = new Calculator();

		if (Options.contains(Do)) {
			if (Do.equals("add")) {
				System.out.println("How many elements do you want to add together");
				String StringNumOfElementsToAdd = input.nextLine();
				int NumOfElementsToAdd;
				try {
					NumOfElementsToAdd = Integer.parseInt(StringNumOfElementsToAdd);
				}
				catch (NumberFormatException e) {
					System.out.println("ENTER AS AN INTEGER");
					StringNumOfElementsToAdd = input.nextLine();
					NumOfElementsToAdd = Integer.parseInt(StringNumOfElementsToAdd);
				}
				ArrayList<Integer> ElementsToAdd = new ArrayList<Integer>();
				for (int i = 0; i < NumOfElementsToAdd; i++) {
			  		System.out.println("Input the next integer: " + (NumOfElementsToAdd-i) + " Numbers remain");
			  		String StringElement = input.nextLine();
					int Element;
					try {
						Element = Integer.parseInt(StringElement, 10);
					}
					catch (NumberFormatException e) {
						System.out.println("Enter An INTEGER");
						StringElement = input.nextLine();
						Element = Integer.parseInt(StringElement, 10);

					}
			  		ElementsToAdd.add(Element);
				}
				int result = calc.Add(ElementsToAdd);
				System.out.println(result);
		  	}
		}
		
	}
}