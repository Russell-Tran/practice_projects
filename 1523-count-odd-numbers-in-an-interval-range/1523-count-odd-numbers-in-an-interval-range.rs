impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        let mut count = 0;
        let mut bottom = low;
        let mut top = high;
        if bottom % 2 == 1 {
            count += 1;
            bottom += 1;
        }
        if top % 2 == 1 {
            count += 1;
            top -= 1;
        }
        count += (top - bottom) / 2;
        return count;
    }
}

/*
odd minus odd:
7 - 3 = 4 
4 / 2 = 2

yield 3: [3, 5, 7]

even minus even:
6 - 4 = 2
2 / 2 = 1

yield 1: [5]

even minus odd:
10 - 7 = 3
3 / 2 = 1

yield 2: [7, 9]

odd minus even:
15 - 4 = 11
11 / 2 = 5

yield 6: [5, 7, 9, 11, 13]


=====
7 --> 10 : [7, 9]
10 - 7 = 3 --> subtract 1 --> 2 --> divide by 2 --> 1

*/