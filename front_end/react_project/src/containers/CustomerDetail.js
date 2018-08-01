import React from 'react';
import axios from 'axios';
import { Card } from 'antd';

class CustomerDetail extends React.Component {

    state = {
        customer: []
    }

    componentDidMount() {
        const articleID = this.props.match.params.articleID;
        axios.get(`http://127.0.0.1:8000/api/customers/${articleID}`)
        .then( res => {
            this.setState({ customer: res.data })
        })
    }

    render() {
        return(
            <Card>
            <h1>{this.state.customer.first}, {this.state.customer.last}</h1>
            <p>date_created: {this.state.customer.date_created}</p>
            <p>Expiration Date: {this.state.customer.expiration_date}</p>
            </Card>
        )
    }
}

export default CustomerDetail