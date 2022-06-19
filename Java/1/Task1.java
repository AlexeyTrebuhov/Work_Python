package lesson1;

public class Task1 {

    public static void main(String[] args) {

        System.out.println(pow(3, 2));
        System.out.println(pow(2, -2));
        System.out.println(pow(3, 0));
        System.out.println(pow(0, 0));

        System.out.println("-----");

        System.out.println(powReq(3, 2));
        System.out.println(powReq(2, -2));
        System.out.println(powReq(3, 0));
        System.out.println(powReq(0, 0));

        System.out.println("-----");

        System.out.println(powIter(3, 2));
        System.out.println(powIter(2, -2));
        System.out.println(powIter(3, 0));
        System.out.println(powIter(0, 0));

    }

    public static double pow(double num, int pow) {
        if (pow == 0 || num == 1) {
            return 1;
        }

        if (pow < 0) {
            pow = -pow;
            num = 1 / num;
        }

        double result = 1;

        for (int i = 0; i < pow; i++) {
            result *= num;
        }
        return result;
    }

    public static double powReq(double num, int pow) {
        if (pow == 0) {
            return 1;
        }

        if (pow < 0) {
            return powReq(1 / num, -pow);
        }

        double result = powReq(num, pow / 2);

        return pow % 2 == 0 ? result * result : result * result * num;
    }

    public static double powIter(double num, int pow) {
        if (pow == 0) {
            return 1;
        }

        if (pow < 0) {
            pow = -pow;
            num = 1 / num;
        }

        double result = 1;

        while (pow > 0) {
            if (pow % 2 == 1) {
                result = result * num;
            }

            num = num * num;
            pow = pow / 2;

        }

        return result;
    }

}