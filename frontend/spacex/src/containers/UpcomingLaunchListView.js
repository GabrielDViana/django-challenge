import React from 'react';
import axios from 'axios';
import LaunchList from '../components/LaunchList'

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
            <LaunchList data={this.state.upcomingLaunches} />
        );
    }
}
export default UpcomingLaunchList;