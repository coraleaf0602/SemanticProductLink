import { Link } from "react-router-dom";
//import { SideBar3Data } from "./SideBar3Data";
import "./styles.css";
// Maybe we could have more consice labels in ai for frontend benefit,
// the longer labels mess up images atm

function SideBar3({ dataList }: any) {
  return (
    <ul className="nav-menu-items">
      <div className="text-heading">
        <text fontSize={40}>Suggested Products</text>
      </div>
      {dataList.map((item: any, index: number) => {
        if (index < 7) {
          return (
            <div key={index} className="ImageContainer">
              <text
                fontSize={12}
                fontFamily="Roboto, Cordia New, Microsoft Sans Serif"
              >
                {item.category}
              </text>
              <Link to={item.link}>
                <div>
                  <img className="Image" src={item.image} width={100} />
                </div>
              </Link>
            </div>
          );
        }
      })}
    </ul>
  );
}

export default SideBar3;
