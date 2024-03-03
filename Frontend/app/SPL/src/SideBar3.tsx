
import { Link } from "react-router-dom";
import { SideBar3Data } from "./SideBar3Data";
import "./styles.css"

function SideBar3() {
  return (
    <div className="SideBarDesign">
      <ul className="nav-menu-items">
        {SideBar3Data.map((item, index) => 
          {return (
            <div key={index} className={item.className}>
                <Link to={item.path}>
                  <div className="ImageContainer">
                    <img
                      src={item.image1}
                      alt="Image"
                      width="140px"
                      height="100px"
                    />
                  </div>
                  {/* {<BarItems>
                    <span> {item.title} </span>
          </BarItems>} */}
                </Link>
            </div>
          )})}
      </ul>
    </div>
  );
}

export default SideBar3;
