use std::cmp::Ordering;

// There should be n! / ((n - k)! * k!) different combinations for each team with n being total and k being size of permutations
/*
0  - Dallas Mavericks - Southwest
1  - Denver Nuggets - Northwest
2  - Golden State Warriors - Pacific
3  - Houston Rockets - Southwest
4  - Los Angeles Clippers - Pacific
5  - Lost Angeles Lakers - Pacific
6  - Memphis Grizzlies - Southwest
7  - Minnesota Timberwolves - Northwest
8  - New Orleans Pelicans - Southwest
9  - Oklahoma City Thunder - Southwest
10 - Phoenix Suns - Pacific
11 - Portland Trail Blazers - Northwest
12 - Sacramento Kings - Pacific
13 - San Antonio Spurs - Southwest
14 - Utah Jazz - Northwest
*/

const TEAMS: [(u8, &str, u8); 15] = [
    (0, "Mavericks", 2),
    (1, "Nuggets", 0),
    (2,  "Warriors", 1),
    (3,  "Rockets", 2),
    (4,  "Clippers", 1),
    (5,  "Lakers", 1),
    (6,  "Grizzlies", 2),
    (7,  "Timberwolves", 0),
    (8,  "Pelicans", 2),
    (9,  "Thunder", 0),
    (10, "Suns", 1),
    (11, "Blazers", 0),
    (12, "Kings", 1),
    (13, "Spurs", 2),
    (14, "Jazz", 0)
];

const _TEST_TEAMS: [(u8, &str, u8); 4] = [
    (0, "Mavericks",0),
    (1, "Spurs", 1),
    (2, "Clippers", 2),
    (3, "Kings", 3)
];

const _PLAY_THREE: u8 = 4;
const PLAY_FOUR: u8 = 6;
const SAME_DIVISION: u8 = 4;

const TEST_ROWS: usize = 15;
fn main() {
    let mut schedule = [[0i8; TEST_ROWS]; TEST_ROWS];
    let result: u64;
    let adj_count: [u8; TEST_ROWS] = [0u8; TEST_ROWS];

    prefill(&mut schedule);
    //_printschedule(schedule);

    // Automate this with user input
    /*
    schedule[0][1] = 4;
    schedule[1][0] = 4;
    schedule[0][2] = 4;
    schedule[2][0] = 4;
    schedule[0][4] = 4;
    schedule[4][0] = 4;
    schedule[0][5] = 4;
    schedule[5][0] = 4;
    schedule[1][2] = 4;
    schedule[2][1] = 4;
    schedule[1][11] = 4;
    schedule[11][1] = 4;
    schedule[1][6] = 4;
    schedule[6][1] = 4;
    */

    result = find_permutation_amount(schedule, 0, adj_count);

    println!("{}", result);
}

fn _printschedule(arr: [[i8; TEST_ROWS]; TEST_ROWS]) {
for i in 0..TEST_ROWS {
        print!("{} ", i);
        for j in 0..TEST_ROWS {
            print!("{} ", arr[i][j]);
        }
        println!("");
    }
    println!("");
}

fn prefill(arr:  &mut [[i8; TEST_ROWS]; TEST_ROWS]) {
    for i in 0..arr.len() {
        let iconference: usize = TEAMS[i].2.into();
        for j in 0..TEST_ROWS {
            if i == j {
                arr[i][j] = -1;
                continue
            }
            let oconference: usize = TEAMS[j].2.into();
            match iconference.cmp(&oconference) {
                Ordering::Less => arr[i][j] = 3,
                Ordering::Greater => arr[i][j] = 3,
                Ordering::Equal => arr[i][j] = 4,
            }
        }
    }
}

fn _test_find_permutations(arr:[[i8; TEST_ROWS]; TEST_ROWS], index: usize, adj_count: [u8; TEST_ROWS]) -> u64 {
    let mut result: u64 = 0;
    let mut count:u8 = 0;
    for x in 0..TEST_ROWS {if arr[index][x] == 4 {count += 1;}}
    count -= SAME_DIVISION;
    let mut s:u8 = 0;
    for y in 0..adj_count.len() {
        s+= adj_count[y];
    }
    //println!("count = {}", count);
    if count < PLAY_FOUR {

        for i in 0..TEST_ROWS {

            if i == index || arr[index][i] == 4 || adj_count[i] == PLAY_FOUR+SAME_DIVISION || adj_count[index] == PLAY_FOUR+SAME_DIVISION {continue;}
            if count == 1 {
                let mut cpy = arr.clone();
                let mut cpy_count = adj_count.clone();
                cpy[index][i] = 4;
                cpy[i][index] = 4;
                cpy_count[index] += 1;
                cpy_count[i] += 1;
                //println!("Index: {}\t{:?}", index, cpy);
                
                if index < TEST_ROWS-1 {
                    result += _test_find_permutations(cpy, index+1, cpy_count);
                }
                else {
                    _printschedule(cpy);
                    result += 1;
                }

                continue;
            }

            for j in i+1..TEST_ROWS {

                if j == index || arr[index][i] == 4 || adj_count[j] == PLAY_FOUR+SAME_DIVISION || adj_count[index] == PLAY_FOUR+SAME_DIVISION {continue;}
                let mut cpy = arr.clone();
                let mut cpy_count = adj_count.clone();
                cpy[index][i] = 4;
                cpy[index][j] = 4;
                cpy[i][index] = 4;
                cpy[j][index] = 4;
                cpy_count[index] += 1;
                cpy_count[i] += 1;
                cpy_count[index] += 1;
                cpy_count[j] += 1;
                //println!("{:?}", cpy);
                
                if index < TEST_ROWS-1 {
                    result += _test_find_permutations(cpy, index+1, cpy_count);
                }
                else {
                    _printschedule(cpy);
                    result += 1;
                }
                continue;
            }
        }
    }
    else if s == TEST_ROWS as u8 * PLAY_FOUR{
        _printschedule(arr);
        result += 1;
    }

    return result;
}

fn find_permutation_amount(arr:[[i8; TEST_ROWS]; TEST_ROWS], index: usize, adj_count:[u8; TEST_ROWS]) -> u64 {
    //for i in 0..arr.len() {
    let mut result: u64 = 0;
    let mut count:u8 = 0;
    for x in 0..TEST_ROWS {if arr[index][x] == 4 {count += 1;}}
    count -= SAME_DIVISION;
    let mut s:u8 = 0;
    for y in 0..adj_count.len() {
        s+= adj_count[y];
    }

    //println!("count = {}", count);
    if count < PLAY_FOUR {

        for i in 0..TEST_ROWS {

            if i == index || arr[0][i] == 4 || adj_count[i] == PLAY_FOUR+SAME_DIVISION || adj_count[index] == PLAY_FOUR+SAME_DIVISION {continue;}
            if count == 5 {
                let mut cpy = arr.clone();
                let mut cpy_count = adj_count.clone();
                cpy[index][i] = 4;
                cpy[i][index] = 4;
                cpy_count[index] = PLAY_FOUR-count;
                cpy_count[i] += 1;
                //println!("{:?}", cpy);
                
                if index < TEST_ROWS-1 {
                    result += find_permutation_amount(cpy, index+1, cpy_count);
                }
                else {
                    result += 1;
                }

                continue;
            }

            for j in i+1..TEST_ROWS {

                if j == index || arr[0][i] == 4 || adj_count[j] == PLAY_FOUR+SAME_DIVISION || adj_count[index] == PLAY_FOUR+SAME_DIVISION {continue;}
                if count == 4 {
                    let mut cpy = arr.clone();
                    let mut cpy_count = adj_count.clone();
                    cpy[index][i] = 4;
                    cpy[index][j] = 4;
                    cpy[i][index] = 4;
                    cpy[j][index] = 4;
                    cpy_count[index] = PLAY_FOUR-count;
                    cpy_count[i] += 1;
                    cpy_count[j] += 1;
                    
                        //println!("{:?}", cpy);
                    
                    if index < TEST_ROWS-1 {
                        result += find_permutation_amount(cpy, index+1, cpy_count);
                    }
                    else {
                        result += 1;
                    }

                    continue;
                }

                for k in j+1..TEST_ROWS {

                    if k == index || arr[0][i] == 4 || adj_count[k] == PLAY_FOUR+SAME_DIVISION || adj_count[index] == PLAY_FOUR+SAME_DIVISION {continue;}
                    if count == 3 {
                        let mut cpy = arr.clone();
                        let mut cpy_count = adj_count.clone();
                        cpy[index][i] = 4;
                        cpy[index][j] = 4;
                        cpy[index][k] = 4;
                        cpy[i][index] = 4;
                        cpy[j][index] = 4;
                        cpy[k][index] = 4;
                        cpy_count[index] = PLAY_FOUR-count;
                        cpy_count[i] += 1;
                        cpy_count[j] += 1;
                        cpy_count[k] += 1;
                        //println!("{:?}", cpy);

                        if index < TEST_ROWS-1 {
                            result += find_permutation_amount(cpy, index+1, cpy_count);
                        }
                        else {
                            result += 1;
                        }

                        continue;
                    }

                    for l in k+1..TEST_ROWS {

                        if l == index || arr[0][i] == 4 || adj_count[l] == PLAY_FOUR+SAME_DIVISION || adj_count[index] == PLAY_FOUR+SAME_DIVISION {continue;}
                        if count == 2 {
                            let mut cpy = arr.clone();
                            let mut cpy_count = adj_count.clone();
                            cpy[index][i] = 4;
                            cpy[index][j] = 4;
                            cpy[index][k] = 4;
                            cpy[index][l] = 4;
                            cpy[i][index] = 4;
                            cpy[j][index] = 4;
                            cpy[k][index] = 4;
                            cpy[l][index] = 4;
                            cpy_count[index] = PLAY_FOUR-count;
                            cpy_count[i] += 1;
                            cpy_count[j] += 1;
                            cpy_count[k] += 1;
                            cpy_count[l] += 1;
                            //println!("{:?}", cpy);

                            if index < TEST_ROWS-1 {
                                result += find_permutation_amount(cpy, index+1, cpy_count);
                            }
                            else {
                                result += 1;
                            }

                            continue;
                        }

                        for m in l+1..TEST_ROWS {

                            if m == index || arr[0][i] == 4 || adj_count[m] == PLAY_FOUR+SAME_DIVISION || adj_count[index] == PLAY_FOUR+SAME_DIVISION{continue;}
                            if count == 1 {
                                let mut cpy = arr.clone();
                                let mut cpy_count = adj_count.clone();
                                cpy[index][i] = 4;
                                cpy[index][j] = 4;
                                cpy[index][k] = 4;
                                cpy[index][l] = 4;
                                cpy[index][m] = 4;
                                cpy[i][index] = 4;
                                cpy[j][index] = 4;
                                cpy[k][index] = 4;
                                cpy[l][index] = 4;
                                cpy[m][index] = 4;
                                cpy_count[index] = PLAY_FOUR-count;
                                cpy_count[i] += 1;
                                cpy_count[j] += 1;
                                cpy_count[k] += 1;
                                cpy_count[l] += 1;
                                cpy_count[m] += 1;
                                //println!("{:?}", cpy);

                                if index < TEST_ROWS-1 {
                                    result += find_permutation_amount(cpy, index+1, cpy_count);
                                }
                                else {
                                    result += 1;
                                }

                                continue;
                            }

                            for n in m+1..TEST_ROWS{

                                if n == index || arr[0][i] == 4 || adj_count[n] == PLAY_FOUR+SAME_DIVISION || adj_count[index] == PLAY_FOUR+SAME_DIVISION {continue;}

                                let mut cpy = arr.clone();
                                let mut cpy_count = adj_count.clone();
                                cpy[index][i] = 4;
                                cpy[index][j] = 4;
                                cpy[index][k] = 4;
                                cpy[index][l] = 4;
                                cpy[index][m] = 4;
                                cpy[index][n] = 4;
                                cpy[i][index] = 4;
                                cpy[j][index] = 4;
                                cpy[k][index] = 4;
                                cpy[l][index] = 4;
                                cpy[m][index] = 4;
                                cpy[n][index] = 4;
                                cpy_count[index] = PLAY_FOUR-count;
                                cpy_count[i] += 1;
                                cpy_count[j] += 1;
                                cpy_count[k] += 1;
                                cpy_count[l] += 1;
                                cpy_count[m] += 1;
                                cpy_count[n] += 1;
                                //println!("{:?}", cpy);
                                if index < TEST_ROWS-1 {
                                    result += find_permutation_amount(cpy, index+1, cpy_count);
                                }
                                else {
                                    result += 1;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    else if s == TEST_ROWS as u8 * PLAY_FOUR{
        _printschedule(arr);
        result += 1;
    }

    //if index < TEST_ROWS-1 {
        //find_permutation_amount(arr, index+1);
    //}
    return result;
}
