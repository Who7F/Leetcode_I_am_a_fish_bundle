impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        if s1.len() > s2.len(){
            return false
        }

        let (mut cnt_s1, mut cnt_s2) = ([0; 26],[0; 26]);
        let (bite_s1, bite_s2) = (s1.as_bytes(), s2.as_bytes());

        for i in 0..s1.len(){
            cnt_s1[bite_s1[i] as usize - 97] += 1;
            cnt_s2[bite_s2[i] as usize - 97] += 1;
        } 

        if cnt_s1 == cnt_s2{
            return true
        }

        for i in s1.len()..s2.len(){
            cnt_s2[bite_s2[i] as usize - 97] += 1;
            cnt_s2[bite_s2[i - s1.len()] as usize - 97] -= 1;

            if cnt_s1 == cnt_s2{
                return true
            }
        }

        false
    }
}