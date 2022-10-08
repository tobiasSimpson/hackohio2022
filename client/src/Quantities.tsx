export function Quantities(props: { averageConsumption: number[] }) {
  return (
    <div>
      <ul className="quantities">
        {props.averageConsumption.map((quantity, i) => (
          <li className="leaderboardItems" key={i}>
            {quantity}
          </li>
        ))}
      </ul>
      <div style={{ fontSize: 40, alignContent: "center" }}>---------</div>
    </div>
  );
}

export default Quantities;
