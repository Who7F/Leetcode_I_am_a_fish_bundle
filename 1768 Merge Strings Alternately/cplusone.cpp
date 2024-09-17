class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string anc = "";
        int minLen = word1.length();
        if(minLen > word2.length()){
            minLen = word2.length();
        }
        for(int i = 0; i < minLen; i++){
            anc += word1[i];
            anc += word2[i];
        }

        return anc + word1.substr(minLen) + word2.substr(minLen);
    }
};