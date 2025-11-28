import java.util.ArrayList;

public class Calculator {
    static int Add(ArrayList ToAdd) {
        int Elements = ToAdd.size();
        int result = 0;
        for (int i = 0; i < Elements; i++) {
            result += (int) ToAdd.get(i);
        }
        return result;

    }
}