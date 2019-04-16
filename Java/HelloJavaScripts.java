/*
inspired from https://docs.oracle.com/javase/tutorial/deployment/jar/manifestindex.html

To run this simple java application, here are some methods:

- execute a class 
1. javac HelloJavaScripts.java
2. java HelloJavaScripts

- execute a jar file
1. javac HelloJavaScripts.java
You have three options here to create a jar file
    1. not specify a manifest file     
    - jar cvf helloJavaScripts.jar HelloJavaScripts.class
    - java -cp helloJavaScripts.jar HelloJavaScripts
    
    2. with external manifest file
    - create the manifest file say - Manifest.txt, which has an explicit `Main-Class` header
    - jar cvfm helloJavaScripts.jar Manifest.txt HelloJavaScripts.class
    - java -jar helloJavaScripts.jar
    
    3. setting an entry point without editing or creating the manifest file
    - jar cvfe helloJavaScripts.jar HelloJavaScripts HelloJavaScripts.class
    - java -jar helloJavaScripts.jar

*/
public class HelloJavaScripts {
    public static void main(String[] args) {
        System.out.println("Hello, Java scripts!");
    }
}