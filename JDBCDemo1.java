// JDBC and Select statement
import java.sql.*;

public class db {
    public static void main(String[] args) {
        Connection conn = null;
        try {
            String dbURL = "jdbc:sqlserver://localhost:1433;databaseName=Student;encrypt=false";
            String user = "student";
            String pass = "student";
            conn = DriverManager.getConnection(dbURL, user, pass);
            System.out.println("Connected.");

            // Create and execute an SQL select statement
            String SQL = "SELECT * FROM aa1";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(SQL);

            // Iterate through the data in the result set and display
            while (rs.next()) {
                System.out.println(rs.getString(1) + ", " + rs.getString(2) + ", " + rs.getString(3));
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
