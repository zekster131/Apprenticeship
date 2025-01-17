package People;

import People.Staff.Person;
import java.util.List;
import java.util.Scanner;

public class Prisoners extends Person {
    public enum Risk {
        HIGH, MED, LOW
    }

    private Risk risk;
    private String crime;
    private int sentence;
    private List<String> contraband;
    private int hungerLevel;
    private int tirednessLevel;

    public Prisoners(String name, int age, int hungerLevel, int tirednessLevel, Risk risk, String crime, int sentence, List<String> contraband) {
        super(name, age);
        this.hungerLevel = hungerLevel;
        this.tirednessLevel = tirednessLevel;
        this.risk = risk;
        this.crime = crime;
        this.sentence = sentence;
        this.contraband = contraband;
    }

    public void serveTime() {
        Scanner scanner = new Scanner(System.in);
        boolean validInput = false;

        while (!validInput) {
            System.out.println("Current sentence for " + getName() + ": " + sentence + " years.");
            System.out.print("How much do you want to reduce the sentence by? ");
            int reduction = scanner.nextInt();

            if (reduction == 0) {
                System.out.println("Prisoner's sentence has not been reduced.");
                validInput = true;
            }
            else if (reduction <= sentence) {
                sentence -= reduction;
                System.out.println("Sentence reduced to: " + sentence + " years.");
                validInput = true;
            } 
            else {
                System.out.println("Reduction must not be higher than the current sentence. Please enter a valid reduction amount.");
            }
        }
    }

    public List<String> getContraband() {
        return contraband;
    }

    public Risk getRisk() {
        return risk;
    }

    public String getCrime() {
        return crime;
    }

    public int getSentence() {
        return sentence;
    }

    public int getHungerLevel() {
        return hungerLevel;
    }

    public int getTirednessLevel() {
        return tirednessLevel;
    }
}
