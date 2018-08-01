import React from 'react';
import { Route } from 'react-router-dom';
import CustomerList from './containers/CustomerList';
import CustomerDetail from './containers/CustomerDetail';



const BaseRouter = () => (
    <div>
        <Route exact path='/' component={CustomerList} />
        <Route exact path='/:articleID' component={CustomerDetail} />
    </div>
);

export default BaseRouter