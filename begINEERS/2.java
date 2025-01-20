

# 2-M(IT)+ (pypy3)

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String s = br.readLine();
            System.out.println(solve(s));
        }
    }
    
    private static String solve(String s) {
        if (s.length() < 3) return "NO";  // Minimum length must be 3 (MIT)
        
        // Check if string can be broken into multiple repetitive strings
        int i = 0;
        while (i < s.length()) {
            // Each part must start with 'M'
            if (s.charAt(i) != 'M') return "NO";
            i++;
            
            // After M, must have at least one IT
            boolean foundIT = false;
            while (i < s.length() - 1) {
                if (s.charAt(i) == 'I' && s.charAt(i + 1) == 'T') {
                    foundIT = true;
                    i += 2;
                } else {
                    break;
                }
            }
            
            if (!foundIT) return "NO";
        }
        
        // If we've consumed the entire string successfully
        return i == s.length() ? "YES" : "NO";
    }
}



// // c 11 hjava

// import java.io.*;
// import java.util.*;
// public class Main {
//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         int t = Integer.parseInt(br.readLine());
//         while (t-- > 0) {
//             int n = Integer.parseInt(br.readLine());
//             String s = br.readLine();
//             System.out.println(solve(s));
//         }
//     }
//     private static String solve(String s) {
//         if (s.length() < 3) return "NO";  // Minimum length must be 3 (MIT)
//         // Check if string can be broken into multiple repetitive strings
//         int i = 0;
//         while (i < s.length()) {
//             // Each part must start with 'M'
//             if (s.charAt(i) != 'M') return "NO";
//             i++;
//             // After M, must have at least one IT
//             boolean foundIT = false;
//             while (i < s.length() - 1) {
//                 if (s.charAt(i) == 'I' && s.charAt(i + 1) == 'T') {
//                     foundIT = true;
//                     i += 2;
//                 } else {
//                     break;
//                 }
//             }
//             if (!foundIT) return "NO";
//         }
//         // If we've consumed the entire string successfully
//         return i == s.length() ? "YES" : "NO";
//     }
// }