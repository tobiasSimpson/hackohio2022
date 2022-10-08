import { useEffect, useState } from "react";

function gridlines(dataSize: number) {
  let result: number[] = [];
  for (let i = 0; i <= 1; i += 1 / dataSize) {
    result.push(i);
  }
  return result;
}

const horizontalGridlines = gridlines(12).map((y) => (
  <line x1="0" y1={y} x2="2" y2={y} stroke="#222" strokeWidth="0.003" />
));

const verticalGridlines = gridlines(24).map((x) => (
  <line x1={x * 2} y1="0" x2={x * 2} y2="1" stroke="#222" strokeWidth="0.003" />
));

function range(low: number, high: number) {
  let result = [];
  for (let i = low; i <= high; i++) {
    result.push(i);
  }
  return result;
}

// for (let i = 0; i <= 24; i += 3) {
//     xLabels.push()
// }

// <text x={2 - i * 0.25 - 0.05} y="1.05" style={{ fontSize: "0.04px" }}>
// {s}
// </text>

export function Graph(props: {
  xRange: [number, number];
  yRange: [number, number];
  points: [number, number][];
}) {
  //   const minY = Math.min(...props.points.map(([x, y]) => y)) * 0.9;
  //   const maxY = Math.max(...props.points.map(([x, y]) => y)) * 1.1;

  const minX = props.xRange[0];
  const maxX = props.xRange[1];
  const rangeX = maxX - minX;

  const minY = props.yRange[0];
  const maxY = props.yRange[1];
  const rangeY = maxY - minY;

  let [xOffset, setXOffset] = useState(0);

  let xLabels = range(0, 7).map((i) => (
    <text
      x={(i * 2) / 7 - 0.05}
      y="1.06"
      style={{ fontSize: "0.04px" }}
      fill="white"
    >
      {i == 7 ? "Now" : `-${7 - i}`}
    </text>
  ));

  let yLabels = range(0, 4).map((i) => (
    <text y={i * 0.25} x="-0.1" style={{ fontSize: "0.04px" }} fill="white">
      {Math.round(maxY - (rangeY * i) / 4)}
    </text>
  ));

  const normalizedPoints = props.points.map(([x, y]) => [
    (2 * (x - minX)) / rangeX,
    (y - minY) / rangeY,
  ]);

  function addPoint(p: [number, number]): void {
    const pointsGroup = document.querySelector("#points");
    pointsGroup?.animate(
      [{ transform: "translateX(0px)" }, { transform: "translateX(-0.088px)" }],
      {
        duration: 2000,
        iterations: 1,
        easing: "ease-in-out",
      }
    );
    setTimeout(() => {
      setXOffset(xOffset - 0.088);
      props.points.push(p);
    }, 2000);
  }

  useEffect(() => {
    document.addEventListener("keydown", (e) => {
      if (e.key === " ") {
        addPoint([24, 100]);
      }
    });
  });

  return (
    <div className="graph">
      <svg viewBox={`-0.1 -0.1 2.2 1.2`} width="800px">
        {horizontalGridlines}
        {verticalGridlines}
        <g id="points">
          {normalizedPoints.map(([x1, y1], i) => {
            if (i == normalizedPoints.length - 1) return undefined;
            const [x2, y2] = normalizedPoints[i + 1];
            return (
              <line
                x1={x1 + xOffset}
                y1={y1}
                x2={x2 + xOffset}
                y2={y2}
                stroke="#cf063b"
                strokeWidth="0.01"
                strokeLinecap="round"
              />
            );
          })}
          {/* {normalizedPoints.map(([x, y]) => (
            <circle cx={x + xOffset} cy={y} fill="#b9b9b9" r="0.01" />
          ))} */}
        </g>
        <rect
          className="blocker"
          fill="#111"
          x="-1"
          y="0"
          width="1"
          height="1"
        />
        <line
          x1="0"
          y1="1"
          x2="2.02"
          y2="1"
          stroke="white"
          strokeWidth="0.01"
          strokeLinecap="round"
        />
        <line
          x1="0"
          y1="-0.02"
          x2="0"
          y2="1"
          stroke="white"
          strokeWidth="0.01"
          strokeLinecap="round"
        />
        {xLabels}
        {yLabels}
      </svg>
    </div>
  );
}

export default Graph;
