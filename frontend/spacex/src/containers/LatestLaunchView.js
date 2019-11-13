import React from 'react';
import axios from 'axios';
import Launch from '../components/Launch'

class LatestLaunch extends React.Component {
    state = {
        latestLaunch: {}
    }
    
    componentDidMount() {
        axios.get('http://0.0.0.0:8000/api/latest/')
            .then(res => {
                console.log(res.data);
                this.setState({
                    latestLaunch: res.data
                })
            })
    }

    render() {
        return (
            <Launch data={this.state.latestLaunch} />
        );
    }
}
export default LatestLaunch;