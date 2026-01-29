public class DivisibleNumber{
    public static int divisibleNumber(int[] x, int n) {
        int count = 0;

        for (int i : x) {
            if (i % n == 0 && i != 0) count++;
        }
        return count;
    }



    public static void main(String[] args) {
        int n1=3, n2=2;
        int[] Tab1 = {6, 10, 2, 3, 4, 5, 6,0};
        int[] Tab2 = {1, 2, 3, 0, 5, -6, 995};

        System.out.println("The number of elements divisible by 3 in Tab1 is : " +divisibleNumber(Tab1, n1));
        System.out.println("The number of elements divisible by 2 in Tab2 is : " +divisibleNumber(Tab2, n2));
        System.out.println();
    }

}
