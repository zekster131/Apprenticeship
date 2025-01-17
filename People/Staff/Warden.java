package People.Staff;

import People.Prisoners;

public class Warden extends Person {
    public Warden(String name, int age) {
        super(name, age);
    }

    public boolean authoriseRelease(Prisoners prisoner) {
        if (prisoner.getSentence() == 0) {
            System.out.println("The warden, " + name + ", has authorised the release for: " + prisoner.getName());
            return true;
        } else {
            System.out.println("Prisoner " + prisoner.getName() + " must serve " + prisoner.getSentence() + " years before release.");
            return false;
        }
    }
}
