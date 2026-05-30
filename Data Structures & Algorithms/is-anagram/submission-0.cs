public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) 
        {
            return false;
        }
        
        var sArray = s.ToCharArray();
        var tArray = t.ToCharArray();

        Array.Sort(sArray);
        Array.Sort(tArray);

        return sArray.SequenceEqual(tArray);
    }
}
