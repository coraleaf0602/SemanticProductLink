import React, { useState } from "react";
import { Link } from "react-router-dom";
import { SideBar3Data } from "./SideBar3Data";
import styled from "styled-components";

const SideBarDesign = styled.div`
  background-color: #fffff;
  border-color: #66afe9;
  outline: 0;
  box-shadow: 0px 0px 50px rgba(15, 59, 252, 0.5);
  width: 200px;
  height: 100vh; /* Changed height to viewport height */
  display: flex;
  flex-direction: column; /* Adjusted to column layout */
  align-items: center; /* Center horizontally */
  position: fixed;
  top: 150px;
  overflow-y: auto; /* Added to enable vertical scrolling */
`;

const BarText = styled.div`
  padding: 8px 0px;
  list-style-type: none;
`;

const BarTextA = styled.div`
  text-decoration: none;
  color: white;
  font-size: 18px;
  width: 95%;
  height: 100%;
  display: flex;
  align-items: center;
  padding: 0 16px;
  border-radius: 4px;
`;

const BarItems = styled.div`
  width: 100%;
`;

const ImageContainer = styled.div`
  display: flex;
  align-items: center;
  box-shadow: 0px 0px 25px rgba(0, 0, 0, 0.5);
  left: 0;
  justify-content: center;
  margin-bottom: 5px;
`;

function SideBar3() {
  return (
    <>
      <SideBarDesign>
        <nav className="sidebar">
          <ul className="nav-menu-items">
            {/*<li className="sidebar-toggle">
              <Link to="#" className="menu-bars">
                <AiIcons.AiOutlineClose />
              </Link>
  </li>*/}

            {SideBar3Data.map((item, index) => {
              return (
                <BarText key={index}>
                  <li className={item.className}>
                    <Link to={item.path}>
                      <ImageContainer>
                        <img
                          src={item.image1}
                          alt="Image"
                          width="140px"
                          height="100px"
                        />
                      </ImageContainer>
                      {/*<BarItems>
                        <span> {item.title} </span>
              </BarItems>*/}
                    </Link>
                  </li>
                </BarText>
              );
            })}
          </ul>
        </nav>
      </SideBarDesign>
    </>
  );
}

export default SideBar3;
