import java.util.Scanner;
public class Sample1 {
    public static void main(String[] args) {
        Sample1 sample = new Sample1();
        sample.readNames();
    }

    public void readNames() {
        int i = 0;
        String name;
        Scanner input = new Scanner(System.in);
        System.out.println("Type your name: ");
        while (i < 2) {
            name = input.nextLine();
            System.out.println("You entered: " + name);
            i++;
        }
       input.close();
    }
}

public class Sample1 {

    public static void main(String[] args) {
        int x, y, z;

        Scanner input = new Scanner(System.in);

        System.out.print("Type X value = ");
        x = stdin.nextInt();

        System.out.print("Type Y value = ");
        y = stdin.nextInt();

        System.out.print("Type Z value = ");
        z = stdin.nextInt();


        if ((x == y) && (y == z)) {
            System.out.print("All are equal (X, Y, Z)");
        } else if ((x > y) && (x > z)) {
            System.out.print("Higher Value (X) ==> " + x);
        } else if (y > z) {
            System.out.print("Higher Value (Y) ==> " + y);
        } else {
            System.out.print("Higher Value (Z) ==> " + z);
        }
    }
}