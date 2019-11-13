import React from 'react';
import axios from 'axios';
import Launch from '../components/Launch'

class LatestLaunch extends React.Component {
    state = {
        latestLaunches: {}
    }
    
    componentDidMount() {
        axios.get('http://0.0.0.0:8000/api/latest/')
            .then(res => {
                console.log(res.data);
                this.setState({
                    latestLaunches: res.data
                })
            })
    }

    render() {
        return (
            <Launch data={this.state.latestLaunches} />
        );
    }
}
export default LatestLaunch;