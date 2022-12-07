package com.company;

import javax.swing.JOptionPane;

// import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String name = JOptionPane.showInputDialog("Enter your name");
        String surname = JOptionPane.showInputDialog("Enter your surname");
        JOptionPane.showMessageDialog(null, "Welcome " + name + " " + surname);

        int age = Integer.parseInt(JOptionPane.showInputDialog("Enter your age"));
        //JOptionPane.showMessageDialog(null, age);
        if(age<=18){
            JOptionPane.showMessageDialog(null, "Sorry you are young to enter");
        }
        else {
            JOptionPane.showMessageDialog(null, "Welcome " + name);
        }

    //    Scanner scanner = new Scanner(System.in);
    //    System.out.print("Name: ");
    //    String name = scanner.nextLine();
    //    Scanner scanner1 = new Scanner(System.in);
    //    System.out.print("Surname: ");
    //    String surname = scanner.nextLine();
    //    Scanner scanner2 = new Scanner(System.in);
    //    System.out.print("Place: ");
    //    String place = scanner.nextLine();
    //    Scanner scanner3 = new Scanner(System.in);
    //    System.out.print("Age: ");
    //    String age = scanner.nextLine() ;
    //    System.out.println("Hello " + name + " " + surname + " from " + place);



    }
}
