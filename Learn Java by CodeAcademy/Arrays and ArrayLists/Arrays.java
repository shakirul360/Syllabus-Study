import java.util.Arrays;

public class Classroom {
  
  public static void main(String[] args){
    String[] students = {"Sade", "Alexus", "Sam", "Koma"};
    double[] mathScores = new double[4];
    mathScores[0] = 94.5;
    mathScores[2] = 76.8;
    int numStudents = students.length;
    String message = "The number of students in the class is " + numStudents;
    System.out.println(message);
  }
}
