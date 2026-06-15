# Numbers Conversion: Solution

## **Decimal to Binary**

- **Convert 25 (decimal) to binary.**
  - **Answer:** **11001**
  - **Explanation:** We use the "division by 2" method. We repeatedly divide the number by 2 and record the remainders until the quotient is 0. The binary number is the remainders read from bottom to top.
    - $25 \div 2 = 12$ remainder **1**
    - $12 \div 2 = 6$ remainder **0**
    - $6 \div 2 = 3$ remainder **0**
    - $3 \div 2 = 1$ remainder **1**
    - $1 \div 2 = 0$ remainder **1**
    - Read remainders from bottom to top

- **Convert 100 (decimal) to binary.**
  - **Answer:** **1100100**
  - **Explanation:** Following the same "division by 2" method:
    - $100 \div 2 = 50$ remainder **0**
    - $50 \div 2 = 25$ remainder **0**
    - $25 \div 2 = 12$ remainder **1**
    - $12 \div 2 = 6$ remainder **0**
    - $6 \div 2 = 3$ remainder **0**
    - $3 \div 2 = 1$ remainder **1**
    - $1 \div 2 = 0$ remainder **1**
    - Read remainders from bottom to top

- **Convert 47 (decimal) to binary.**
  - **Answer:** **101111**
  - **Explanation:**
    - $47 \div 2 = 23$ remainder **1**
    - $23 \div 2 = 11$ remainder **1**
    - $11 \div 2 = 5$ remainder **1**
    - $5 \div 2 = 2$ remainder **1**
    - $2 \div 2 = 1$ remainder **0**
    - $1 \div 2 = 0$ remainder **1**
    - Read remainders from bottom to top

---

## **Binary to Decimal**

- **Convert 101101 (binary) to decimal.**
  - **Answer:** **45**
  - **Explanation:** We multiply each binary digit by 2 raised to the power of its position (starting from 0 on the right) and sum the results.
    - $(1 \times 2^5) + (0 \times 2^4) + (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$
    - $= 32 + 0 + 8 + 4 + 0 + 1 = 45$

- **Convert 1110001 (binary) to decimal.**
  - **Answer:** **113**
  - **Explanation:**
    - $(1 \times 2^6) + (1 \times 2^5) + (1 \times 2^4) + (0 \times 2^3) + (0 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$
    - $= 64 + 32 + 16 + 0 + 0 + 0 + 1 = 113$

- **Convert 10010 (binary) to decimal.**
  - **Answer:** **18**
  - **Explanation:**
    - $(1 \times 2^4) + (0 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$
    - $= 16 + 0 + 0 + 2 + 0 = 18$

---

## **Decimal to Hexadecimal**

- **Convert 255 (decimal) to hexadecimal.**
  - **Answer:** **FF**
  - **Explanation:** Similar to the binary conversion, we repeatedly divide by the base, which is **16**. We convert remainders of 10-15 to their letter equivalents (A-F).
    - $255 \div 16 = 15$ remainder **15 (F)**
    - $15 \div 16 = 0$ remainder **15 (F)**

- **Convert 64 (decimal) to hexadecimal.**
  - **Answer:** **40**
  - **Explanation:**
    - $64 \div 16 = 4$ remainder **0**
    - $4 \div 16 = 0$ remainder **4**

- **Convert 202 (decimal) to hexadecimal.**
  - **Answer:** **CA**
  - **Explanation:**
    - $202 \div 16 = 12$ remainder **10 (A)**
    - $12 \div 16 = 0$ remainder **12 (C)**

---

## **Hexadecimal to Decimal**

- **Convert A3 (hex) to decimal.**
  - **Answer:** **163**
  - **Explanation:** We multiply the value of each hex digit by 16 raised to the power of its position (starting from 0 on the right). Remember A = 10.
    - $(10 \times 16^1) + (3 \times 16^0) = 160 + 3 = 163$

- **Convert 1F (hex) to decimal.**
  - **Answer:** **31**
  - **Explanation:** Remember F = 15.
    - $(1 \times 16^1) + (15 \times 16^0) = 16 + 15 = 31$

- **Convert C9 (hex) to decimal.**
  - **Answer:** **201**
  - **Explanation:** Remember C = 12.
    - $(12 \times 16^1) + (9 \times 16^0) = 192 + 9 = 201$

---

## **Binary to Hexadecimal (and vice versa)**

- **Convert 11011110 (binary) to hexadecimal.**
  - **Answer:** **DE**
  - **Explanation:** The easiest way is to group the binary number into chunks of 4 bits from right to left, then convert each chunk to its hex equivalent.
    - `1101` `1110`
    - `1101` = 13 = **D**
    - `1110` = 14 = **E**

- **Convert 7B (hex) to binary.**
  - **Answer:** **01111011**
  - **Explanation:** This is the reverse. Convert each hex digit into its 4-bit binary equivalent.
    - `7` = **0111**
    - `B` (which is 11) = **1011**

- **Convert 10010110 (binary) to hexadecimal.**
  - **Answer:** **96**
  - **Explanation:** Group the binary number into 4-bit chunks.
    - `1001` `0110`
    - `1001` = 9 = **9**
    - `0110` = 6 = **6**
