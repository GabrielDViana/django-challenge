import React from 'react';
import axios from 'axios';
import UpcomingLaunch from '../components/UpcomingLaunch'

const listData = [];

class UpcomingLaunchList extends React.Component {
    state = {
        upcomingLaunches: []
    }
    
    componentDidMount() {
        axios.get('http://0.0.0.0:8000/api/upcoming/')
            .then(res => {
                console.log(res.data);
                this.setState({
                    upcomingLaunches: res.data
                })
            })
    }

    render() {
        return (
            <UpcomingLaunch data={this.state.upcomingLaunches} />
        );
    }
}
export default UpcomingLaunchList;