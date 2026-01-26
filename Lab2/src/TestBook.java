public class TestBook {
    public static void main(String[] args) {
        Book book1 = new Book("J.K Rowling", "Harry Potter & the Philosopher's Stone");

        book1.display(); // Ex1 a)
        System.out.println(book1); // Ex1 b) (same as doing toString(book1));
    }
}
