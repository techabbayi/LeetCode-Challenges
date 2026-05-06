1class Solution {
2    public int addDigits(int num) {
3        if (num == 0) {
4            return 0;
5        }
6        return 1 + (num - 1) % 9;
7    }
8}