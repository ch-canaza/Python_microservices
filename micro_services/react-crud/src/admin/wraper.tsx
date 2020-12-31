import React, { PropsWithChildren } from 'react';
import Menu from './components/menu';
import Nav from './components/nav';


const Wraper = (props: PropsWithChildren<any>) => {
    return (
        <div>
            <Nav />

            <div className="container-fluid">
                <div className="row">

                    <Menu />

                    <main className="col-md-9 ml-sm-auto col-lg-10 px-md-4">
                        {props.children}
                    </main>
                </div>
            </div>
        </div>
    );

};

export default Wraper;
