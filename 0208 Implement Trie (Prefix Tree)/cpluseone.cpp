struct TrieNode{
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Trie {
private:
    TrieNode* root;
public:
    Trie() {
        root  = new TrieNode();
    }
    
    void insert(const string& word) {
        TrieNode* node = root;
        
        for(char w : word) {
            if(node->children.find(w) == node->children.end()) {
                node->children[w] = new TrieNode();
            }
            node = node->children[w];
        }
        node->isEnd = true;
    }
    
    bool search(const string& word) {
        TrieNode* node = root;

        for(char w : word) {
            if(node->children.find(w) == node->children.end()) {
                return false;
            }
            node = node->children[w];
        }
        return node->isEnd;
    }
    
    bool startsWith(const string& prefix) {
        TrieNode* node = root;

        for(char w : prefix) {
            if(node->children.find(w) == node->children.end()) {
                return false;
            }
            node = node->children[w];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */