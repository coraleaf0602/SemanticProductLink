

import { Link } from "react-router-dom";
//import { SideBar3Data } from "./SideBar3Data";
import "./styles.css"

function SideBar3({dataList}:any) {
  return (
    <ul className="nav-menu-items">
      <div className="text-heading">
        <text fontSize={24}>Suggested Products</text>
      </div>
      {dataList.map((item:any, index:number) => 
        {return (
          <div key={index} className="ImageContainer">
            <text fontSize={12}>{item.category}</text>
              <Link to={item.link}> 
                <div>
                  <img
                      className="Image"
                      src={item.image}
                      width={100}
                      height={100}
                    />
                </div>                 
              </Link>
          </div>
        )})}
    </ul>
  );
}

export default SideBar3;
