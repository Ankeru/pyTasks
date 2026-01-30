public class SumCalculator {
    
    /**
     * Складывает два целых числа
     * @param a первое число
     * @param b второе число
     * @return сумма чисел
     */
    public static int sum(int a, int b) {
        return a + b;
    }
    
    /**
     * Складывает массив целых чисел
     * @param numbers массив чисел для сложения
     * @return сумма всех чисел
     * @throws IllegalArgumentException если массив null
     */
    public static int sumArray(int[] numbers) {
        if (numbers == null) {
            throw new IllegalArgumentException("Массив не может быть null");
        }
        
        int result = 0;
        for (int number : numbers) {
            result += number;
        }
        return result;
    }
    
    /**
     * Складывает переменное количество чисел
     * @param numbers числа для сложения
     * @return сумма всех чисел
     */
    public static int sumVarArgs(int... numbers) {
        int result = 0;
        for (int number : numbers) {
            result += number;
        }
        return result;
    }
    
    public static void main(String[] args) {
        // Примеры использования
        System.out.println("Сумма 5 и 3: " + sum(5, 3));
        System.out.println("Сумма массива [1, 2, 3, 4, 5]: " + sumArray(new int[]{1, 2, 3, 4, 5}));
        System.out.println("Сумма переменных аргументов 10, 20, 30: " + sumVarArgs(10, 20, 30));
    }
}
