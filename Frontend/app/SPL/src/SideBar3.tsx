
import { Link } from "react-router-dom";
//import { SideBar3Data } from "./SideBar3Data";
import "./styles.css"

function SideBar3({ responseData }:any) {
  return (
    <div className="SideBarDesign">
      <ul className="nav-menu-items">
        {responseData.map((item:any, index:number) => 
          {return (
            <div key={index} className="nav-text">
              <text fontSize={12}>{item.category}</text>
                <Link to={item.link}>
                  <div className="ImageContainer">
                    <img
                      src="./alienware.jpg"
                      alt="Image"
                      width="140px"
                      height="100px"
                    />
                  </div>
                </Link>
            </div>
          )})}
      </ul>
    </div>
  );
}

export default SideBar3;
