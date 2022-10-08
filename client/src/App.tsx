import { useEffect } from "react";
import "./App.css";
import Graph from "./Graph";
import Leaderboard from "./Leaderboard";
import Quantities from "./Quantities";

function App() {
  let points: [number, number][] = [];

  for (let i = 0; i < 24 * 7; i++) {
    points.push([
      i,
      i == 0 ? 100 : points[i - 1][1] + (Math.random() - 0.5) * 10,
    ]);
  }

  // let topFive = string[];
  // async function getData() {
  // const res = await fetch('/get_data')
  // topFive = await res.json()
  // }

  return (
    <div className="App">
      <h1
        style={{
          color: "#cf063b",
          justifyContent: "center",
          height: 55,
          fontFamily: "Courier New",
          fontSize: 40,
        }}
      >
        Energy Dashboard
      </h1>
      <div className="flex">
        <Leaderboard
          topFive={["taylor", "lincoln", "busch", "smith-steeb", "baker"]}
          localPosition={["taylor", "lincoln", "busch", "smith-steeb", "baker"]}
          thisRank={17}
        />
        <Graph
          xRange={[0, 24 * 7]}
          yRange={[
            Math.min(...points.map(([x, y]) => y)) * 0.9,
            Math.max(...points.map(([x, y]) => y)) * 1.1,
          ]}
          points={points}
        />
        {/* <Graph xRange={[0, 24]} yRange={[50, 250]} points={points} /> */}
      </div>
    </div>
  );
}

export default App;
