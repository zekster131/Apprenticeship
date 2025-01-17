package People.Staff;

public abstract class Staff extends Person {
    protected int wage;
    protected int hoursWorked;

    public Staff(String name, int age, int wage, int hoursWorked) {
        super(name, age);
        this.wage = wage;
        this.hoursWorked = hoursWorked;
    }

    public void getPaid() {
        System.out.println("Getting paid: " + wage);
    }

    public abstract void onDuty();
}
