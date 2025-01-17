package People.Staff;

public class Guard extends Staff {
    public Guard(String name, int age, int wage, int hoursWorked) {
        super(name, age, wage, hoursWorked);
    }

    @Override
    public void onDuty() {
        System.out.println("");
        System.out.println("Guards on duty:");
        System.out.println(name + " is currently guarding the prison.");
    }

}
