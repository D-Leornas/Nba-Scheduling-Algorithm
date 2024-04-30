mod main2;

use std::fmt;

const SCHEDULE_LENGTH: usize = 14;
const BACK_TO_BACK_LIMIT: u8 = 1;
const TEST_ROWS: usize = 8;
const INTRADIVISION: u8 = 3;
const INTRACONFERENCE: u8 = 2;
const INTERCONFERENCE: u8 = 1;

struct Team {
    id: u8,
    name: String,
    division: u8,
    conference: u8,
    intradivision_games: u8,
    intraconference_games: u8,
    interconference_games: u8,
    back_to_backs: u8
}

impl fmt::Display for Team {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}, {}, {}, {}", self.id, self.name, self.division, self.conference)
    }
}

const TEST_TEAMS: [(u8, &str, u8, u8); 8] = [
    (0, "Mavericks", 0, 0),
    (1, "Spurs", 0, 0),
    (2, "Clippers", 1, 0),
    (3, "Lakers", 1, 0),
    (4, "Heat", 2, 1),
    (5, "Magic", 2, 1),
    (6, "Raptors", 3, 1),
    (7, "Knicks", 3, 1),
];

fn main() {
    let mut schedule = [[0i8; TEST_ROWS]; SCHEDULE_LENGTH];
    let result: u64;

    let mut teams: Vec<Team> = Vec::new();
    for team in TEST_TEAMS {
        teams.push(build_team(team.0, team.1.into(), team.2, team.3));
    }

    /*
    for team in teams {
        println!("{}", team.name);
    }
     */


}

fn build_team(id: u8, name: String, division: u8, conference: u8) -> Team {
    Team {
        id,
        name,
        division,
        conference,
        intradivision_games: INTRADIVISION,
        intraconference_games: INTRACONFERENCE,
        interconference_games: INTERCONFERENCE,
        back_to_backs: BACK_TO_BACK_LIMIT
    }
}