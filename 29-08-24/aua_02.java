package aula2;
import java.util.Scanner;

public class Aula2 {

    public static void main(String[] args) {
        int x, y, z;

        Scanner stdin = new Scanner(System.in);

        System.out.print("Type X value = ");
        x = stdin.nextInt();

        System.out.print("Type Y value = ");
        y = stdin.nextInt();

        System.out.print("Type Z value = ");
        z = stdin.nextInt();

        if ((x == y) && (y == z)) {
            System.out.println("All are equal (X, Y, Z)");
        } else if ((x > y) && (x > z)) {
            System.out.print("Higher Value (X) ==> " + x);
        } else if (y > z) {
            System.out.print("Higher Value (Y) ==> " + y);
        } else {
            System.out.print("Higher Value (Z) ==> " + z);
        }
    }
}
