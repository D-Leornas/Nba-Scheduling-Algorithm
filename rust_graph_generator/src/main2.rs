use std::cmp::Ordering;

//id, team name, division, conference
const _TEST_TEAMS: [(u8, &str, u8); 4] = [
    (0, "Mavericks", 0, 0),
    (1, "Spurs", 0, 0),
    (2, "Clippers", 1, 0),
    (3, "Lakers", 1, 0),
    (4, "Heat", 2, 1)(5, "Magic", 2, 1),
    (6, "Raptors", 3, 1)(7, "Knicks", 3, 1),
];

const SCHEDULE_LENGTH: u8 = 14;
const BACK_TO_BACK_LIMIT: u8 = 1;
const TEST_ROWS: u8 = 8;
const SAME_DIVISION: u8 = 3;
const SAME_CONFERENCE: u8 = 2;
const DIFF_CONFERENCE: u8 = 1;

fn main() {
    let mut schedule = [[0i8; TEST_ROWS]; TEST_ROWS];
    let result: u64;
    let adj_count: [u8; TEST_ROWS] = [0u8; TEST_ROWS];
}
