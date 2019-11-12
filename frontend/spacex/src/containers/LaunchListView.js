import React from 'react';
import axios from 'axios';
import Launch from '../components/Launch'

const listData = [];

class LaunchList extends React.Component {
    state = {
        upcomingLaunch: []
    }
    
    componentDidMount() {
        axios.get('http://0.0.0.0:8000/api/upcoming/')
            .then(res => {
                console.log(res.data);
                this.setState({
                    upcomingLaunch: res.data
                })
            })
    }

    render() {
        return (
            <Launch data={this.state.upcomingLaunch} />
        );
    }
}
export default LaunchList;