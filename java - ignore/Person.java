public class Person {
    public int Age = 5;
    public Faker GetName = new Faker();
    public String FirstName = GetName.first_name();
};