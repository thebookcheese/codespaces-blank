import java.util.Arrays;
import java.util.Scanner;
import java.util.ArrayList;


public class Main {

    static void RockPaperScissors() {
        Scanner scanner = new Scanner(System.in); // used to read inputs
        System.out.println("Rock, Paper, or Scissors");
        String message = scanner.nextLine().toLowerCase();
        

        ArrayList<String> Options = new ArrayList<String>();
        Options.add("rock");
        Options.add("paper");
        Options.add("scissors");

        if (!Options.contains(message)) {
            while (!Options.contains(message)) {
                System.out.println("Rock, Paper, or Scissors");
                message = scanner.nextLine().toLowerCase();
            }
        }

        System.out.println(Options.size());
        int AIGuessIndex = (int)(Math.random() * (Options.size() + 1)); // random number from 1 to 4
        String AIGuess = Options.get(AIGuessIndex - 1); // use the random number to pick one of rock, paper, or scissors
        System.out.println("The AI used " + AIGuess);


        // logic for result
        if (message.equals("rock")) {
            if (AIGuess.equals("scissors")) {
                System.out.println("You Won");
            } else if (AIGuess.equals("paper")) {
                System.out.println("You Lost");
            } else if (AIGuess.equals(message)) {
                System.out.println("It was a draw");
            }
        } else if (message.equals("scissors")) {
            if (AIGuess.equals("rock")) {
                System.out.println("You Lost");
            } else if (AIGuess.equals("paper")) {
                System.out.println("You Won");
            } else if (AIGuess.equals(message)) {
                System.out.println("It was draw");
            }
        } else if (message.equals("paper")) {
            if (AIGuess.equals("rock"))  {
                System.out.println("You Won");
            } else if (AIGuess.equals("scissors")) {
                System.out.println("You Lost");
            } else if (AIGuess.equals(message)) {
                System.out.println("It draw");
            }
        }


    }

    static void Classes() {
        Person name = new Person();
        System.out.println(name.Age);
        System.out.println(name.FirstName);
    }
    public static void main(String[] args) {
        System.out.println("Hello World");
        System.out.println("Bob, I was Bob once, they locked me in a room, a rubber room, a rubber room with rats, rats? I hate rats, rats make me bob.");
        // RockPaperScissors(); // run rock paper scissors
        Classes();
  }
}