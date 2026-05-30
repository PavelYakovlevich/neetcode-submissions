public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) 
        {
            return false;
        }
        
        var frequencies = new int[26];

        for (var i = 0; i < s.Length; i++)
        {
            frequencies[s[i] - 'a']++;
            frequencies[t[i] - 'a']--;
        }

        return frequencies.FirstOrDefault(frequency => frequency != 0) == 0;
    }
}
