package main;

import People.*;
import People.Staff.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Creating instances
        Prisoners prisoner = new Prisoners("John Doe", 30, 5, 5, Prisoners.Risk.MED, "Theft", 5, Arrays.asList("Knife", "Phone"));
        Guard guard = new Guard("Zeki Gurler", 30, 2000, 40);
        Warden warden = new Warden("Chris Reeves", 30);

        // Simulating operations
        prisoner.serveTime();
        warden.authoriseRelease(prisoner);
        guard.onDuty();
    }
}
