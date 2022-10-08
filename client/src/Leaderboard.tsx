import Quantities from "./Quantities";
import { useEffect, useState } from "react";

export function Leaderboard(props: {
  topFive: string[];
  localPosition: string[];
  thisRank: number;
}) {
  // interface Building {
  //      name: string;
  //      value: number;
  // }
  // const [topFive, setTopFive] = useState<Building[]>([]);
  // const [localFive, setLocalFive] = useState<Building[]>([]);
  // const [topFiveNames, setTopFiveNames] = useState<string>([])
  // const [topFiveValues, setTopFiveValues] = useState<number>([])
  // const [localFiveNames, setLocalFiveNames] = useState<string>([])
  // const [localFiveValues, setLocalFiveValues] = useState<number>([])
  // const [thisRank, setThisRank] = useState<number>
  // useEffect(() => {
  //      const go = async () => {
  //          const res = await fetch('/top_five_names')
  //          const newTopFiveNames = await res.json()
  //          setTopFiveNames(newTopFiveNames)
  //          const res2 = await fetch('/top_five_values')
  //          const newTopFiveValues = await res2.json()
  //          setTopFiveValues(newTopFiveValues)
  //          const res3 = await fetch('/local_five_names')
  //          const newLocalFiveNames = await res3.json()
  //          setLocalFiveNames(newLocalFiveNames)
  //          const res4 = await fetch('/local_five_values')
  //          const newLocalFiveValues = await res4.json()
  //          setLocalFiveValues(newLocalFiveValues)
  // }
  // }, [])

  const topFive = (
    <div className="leaderboard">
      {props.topFive.map((name, i) => (
        <div className="leaderboardItems" key={i}>
          <span className="dorm-name">{name}</span>
          <span>{100}</span>
        </div>
      ))}
    </div>
  );

  const thisPosition = (
    <ol className="leaderboard" start={props.thisRank - 2}>
      {props.localPosition.map((name, i) => (
        <li className="leaderboardItems" key={i}>
          {name}
        </li>
      ))}
    </ol>
  );

  return (
    <div>
      {topFive}
      {/* <Quantities averageConsumption={[100, 200, 300, 800, 1000]} /> */}
      {/* <div style={{ fontSize: 40, alignContent: "center" }}>---------</div>
      {thisPosition} */}
    </div>
  );
}

export default Leaderboard;
