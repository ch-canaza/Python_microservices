import React from 'react'

const Menu = () => {
    return (
        <div>
            <nav id="sidebarMenu" className="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
            <div className="sidebar-sticky pt-3">
              <ul className="nav flex-column">
                <li className="nav-item">
                
                    <a className="nav-link active"  href="# ">
                    <span data-feather="home"></span>
                    Products
                  </a>
                </li>
              </ul>
      
            
            </div>
          </nav>
        </div>
    );
};

export default Menu;
